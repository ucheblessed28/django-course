from django.contrib import admin
from .models import MyModel # Import your models

# Register your models here.
@admin.register(MyModel)

# Register the model so it appears in the admin interface
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') # Display these fields in the admin list view
    search_fields = ('name',) # Enable searching for these fields
    list_filter = ('name',) # Enable filtering by these fields

