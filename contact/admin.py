from django.contrib import admin
from contact.models import Contact,Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = 'name',
    list_display_links = 'id', 'name'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email',
    ordering = 'first_name',
    list_filter = 'created_date',
    search_fields = 'id','first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 50
    list_editable = 'email',
    list_display_links = 'id','first_name',