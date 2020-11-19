from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):            # Clase para extender las funcionalidades del panel de admin
    readonly_fields = ('created','updated')

admin.site.register(Project, ProjectAdmin)

