from django.contrib import admin
from server.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'time']

admin.site.register(Person, PersonAdmin)