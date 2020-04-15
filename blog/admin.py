from django.contrib import admin
#from markdownx.admin import MarkdownxModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Tag

#admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)


# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Post, PostAdmin)