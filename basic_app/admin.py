from django.contrib import admin


class AbstractAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.create_user = request.user

        obj.update_user = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()

        for instance in instances:
            if instance in formset.new_objects:
                instance.create_user = request.user
            instance.update_user = request.user
            instance.save()