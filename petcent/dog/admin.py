from django.contrib import admin
from .models import Dog,Review
# Register your models here.

# class DogAdmin(admin.ModelAdmin):
#     list_display=('title','description')
#     search_fields=['title','description']
#     list_editable=('description',)
admin.site.register(Dog)
admin.site.register(Review)
