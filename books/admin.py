from django.contrib import admin
from books.models import Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):        #能按照姓氏或名字来排序
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)        #按publication_date降序排
    #fields = ('title', 'authors', 'publisher','publication_date')  #编辑表单将按照指定的顺序显示各字段。 它看起来自然多了——作者排在书名之后
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)     #用AuthorAdmin选项注册Author模块
admin.site.register(Book,BookAdmin)
