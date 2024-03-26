from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=('title','group','user','complete','create')
    list_filter=('group','complete')
    search_fields=('title','description')
    ordering=('-create',)
    fields=['title','description','group','complete']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['group'].widget.can_add_related=False
        return form

admin.site.register(Task, TaskAdmin)