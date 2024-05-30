from django.contrib import admin
from .models import Main_Recipe,Recepi_Comment,Recepi_Ingredient,Recepi_Rating
# Register your models here.

admin.site.register(Main_Recipe)
admin.site.register( Recepi_Ingredient)
admin.site.register( Recepi_Rating)
admin.site.register( Recepi_Comment)
