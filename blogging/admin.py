from django.contrib import admin

# a new import
from blogging.models import Post, Category
# and a new admin registration
# class Categorydmin(admin.ModelAdmin):
#     model = Category
#     exclude = ['posts']
class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)