from django.contrib.auth.models import User
from django.db import models
from functools import reduce
from django.db.models import Sum
from .fields import BasicDecimalField, BasicCharField


class AbstractModel(models.Model):
    create_dttm = models.DateTimeField(auto_now_add=True)
    update_dttm = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_create_user', verbose_name='creador')
    update_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_update_user', verbose_name='Actualizado por')
    class Meta:
        abstract = True

    def set_user_attributes(self, from_object):
        self.create_user = from_object.update_user
        self.update_user = from_object.update_user

    def set_attributes_and_save(self, from_object):
        self.set_user_attributes(from_object)
        self.save()


class AbstractNamedModel(AbstractModel):
    name = BasicCharField('Nombre')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class AggregateModel(AbstractModel):
    amount = BasicDecimalField()
    is_dirty = models.BooleanField()

    class Meta:
        abstract = True
    
    @classmethod
    def get_total_by_category(cls, *args):
        aggregations = cls.objects.filter(**cls._dict(cls.time_grouping_fields(), args))
        dirty_aggregations = aggregations.filter(is_dirty=True)
        if dirty_aggregations.exists():
            cls.reaggregate(dirty_aggregations)

        return aggregations

    @classmethod
    def map_transactions_to_aggregations(cls, dirty_aggregations, grouped_trans):
        for transaction in grouped_trans:
            agg = dirty_aggregations.get(**cls.base_fields(*map(lambda field: transaction[field], cls.related_model_class().aggregate_fields_names())))
            agg.amount = transaction['total']
            agg.is_dirty = False
            agg.save()

    @classmethod
    def aggregate(cls, transaction):
        if transaction.base_fields_changed:
            old_agg = cls.objects.get(**cls.get_old_base_fields(transaction))
            old_agg.is_dirty = True
            old_agg.update_user = transaction.update_user
            old_agg.save()

        agg = cls.objects.filter(**cls.get_base_fields(transaction)).first()
        if agg:
            agg.is_dirty = True
        else:
            agg = cls(**cls.get_base_fields(transaction), amount=transaction.amount, is_dirty=False)
        agg.set_attributes_and_save(transaction)

    @classmethod
    def reaggregate(cls, dirty_aggregations):
        grouped_trans = cls.related_model_class().objects.filter(**cls.get_values_for_filter(dirty_aggregations)).values(*cls.related_model_class().aggregate_fields_names()).annotate(total=Sum('amount'))
        cls.map_transactions_to_aggregations(dirty_aggregations, grouped_trans)
        dirty_aggregations.filter(is_dirty=True).delete()

    @classmethod
    def get_values_for_filter(cls, dirty_aggregations):
        result = dict()
        for dirty_agg in dirty_aggregations.values(*cls.base_field_names()):
            for field_name in cls.base_field_names():
                result.setdefault(field_name, []).append(dirty_agg[field_name])
        
        final_list = []
        for value in cls.base_field_names():
            final_list.append(result[value])

        return cls._dict(cls.related_model_class().aggregate_fields_names_in(), final_list)

    @classmethod
    def get_old_base_fields(cls, transaction):
        return cls.base_fields(*transaction.get_old_base_field_values())

    @classmethod
    def get_base_fields(cls, transaction):
        return cls.base_fields(*transaction.get_base_field_values())

    @classmethod
    def base_fields(cls, *args):
        return cls._dict(cls.base_field_names(), args)

    @classmethod
    def base_field_names(cls):
        return cls.time_grouping_fields() + cls.non_time_grouping_fields()

    def time_grouping_fields():
        raise NotImplementedError('Subclass of AggregateModel must implement time_grouping_fields')
    
    def non_time_grouping_fields():
        raise NotImplementedError('Subclass of AggregateModel must implement non_time_grouping_fields')
    
    def related_model_class():
        raise NotImplementedError('Subclass of AggregateModel must implement related_model_class')

    def _dict(l1, l2):
        return dict(zip(l1, l2))

class Aggregable(AbstractModel):
    LOADED = 'loaded_'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.__class__.fields_names():
            setattr(self, self.__class__.LOADED+field, None)

    @property
    def base_fields_changed(self):
        cls = self.__class__
        #returns true if any of the base fields has changed: self._loaded_[name] and self._loaded_[name] != self.[name]
        return reduce(lambda acum, field: acum or (getattr(self, cls.LOADED+field) and getattr(self, cls.LOADED+field) != getattr(self, field)), cls.fields_names(), False)

    @classmethod
    def aggregate_fields_names_in(cls):
        #adds im clause to query multiple values
        return map(lambda field: field+'__in', cls.aggregate_fields_names())

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        for field in cls.fields_names():
            setattr(instance, cls.LOADED+field, getattr(instance, field))
        return instance

    def get_old_base_field_values(self):
        raise NotImplementedError('Subclass of Aggregable must implement get_old_base_field_values')

    def get_base_field_values(self):
        raise NotImplementedError('Subclass of Aggregable must implement get_base_field_values')

    def fields_names():
        raise NotImplementedError('Subclass of Aggregable must implement fields_names')

    def aggregate_fields_names():
        raise NotImplementedError('Subclass of Aggregable must implement aggregate_fields_names')

    class Meta:
        abstract = True
