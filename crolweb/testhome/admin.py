from django.contrib import admin
from testhome.models import Testhome


class TesthomeAdmin(admin.ModelAdmin):
    list_display = ['title','tid','tdate','tdata']


admin.site.register(Testhome, TesthomeAdmin)