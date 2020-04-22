from django.db import models

DECIMAL_TOTAL = 15
DECIMAL_PLACES =  4
VARCHAR_LENGTH = 50

class BasicForeignKey(models.ForeignKey):
	def __init__(self, model_name, verbose_name, cascade=False, **kwargs):
		self.model_name = model_name
		self.verbose_name = verbose_name
		kwargs['verbose_name'] = verbose_name
		kwargs['on_delete'] = models.CASCADE if cascade else models.PROTECT
		kwargs['to'] = model_name
		super().__init__(**kwargs)

	def deconstruct(self):
		name, path, args, kwargs = super().deconstruct()
		args.append(self.model_name)
		args.append(self.verbose_name)
		del kwargs["verbose_name"]
		del kwargs["on_delete"]
		return name, path, args, kwargs

class BasicCharField(models.CharField):
	def __init__(self, field_name, **kwargs):
		self.field_name = field_name
		kwargs = kwargs
		kwargs['verbose_name'] = field_name
		kwargs['max_length'] = VARCHAR_LENGTH
		super().__init__(**kwargs)

	def deconstruct(self):
		name, path, args, kwargs = super().deconstruct()
		args.append(self.field_name)
		del kwargs["max_length"]
		del kwargs["verbose_name"]
		return name, path, args, kwargs

class BasicDecimalField(models.DecimalField):
	def __init__(self, field_name=None, **kwargs):
		if not kwargs:
			kwargs = dict()
		if field_name:
			kwargs['verbose_name'] = field_name
		kwargs['max_digits'] = DECIMAL_TOTAL
		kwargs['decimal_places'] = DECIMAL_PLACES
		super().__init__(**kwargs)

	def deconstruct(self):
		name, path, args, kwargs = super().deconstruct()
		del kwargs["max_digits"]
		del kwargs["decimal_places"]
		kwargs.pop("verbose_name", None)
		return name, path, args, kwargs

class BasicBooleanField(models.BooleanField):
	def __init__(self, field_name, default=False):
		self.field_name = field_name
		kwargs = dict()
		kwargs['verbose_name'] = field_name
		kwargs['default'] = default
		super().__init__(**kwargs)

	def deconstruct(self):
		name, path, args, kwargs = super().deconstruct()
		del kwargs["default"]
		del kwargs["verbose_name"]
		args.append(self.field_name)
		return name, path, args, kwargs
