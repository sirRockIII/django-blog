from django.contrib import admin

# a new import
from blogging.models import Post, Category

# and a new admin registration
class CategoryInline(admin.TabularInline):
    model = Category
    exclude = ['description']


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)