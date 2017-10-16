from django.db import models

class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=60)
    state_province=models.CharField(max_length=30)
    country=models.CharField(max_length=50)
    website=models.URLField()

    def __str__(self):      # __unicode__() 方法可以进行任何处理来返回对一个对象的字符串表示
        return self.name

    class Meta:     #以在任意一个 模型 类中使用 Meta 类，来设置一些与特定模型相关的选项
        ordering=['name']       #Publisher对象的相关返回值默认地都会按 name 字段排序

class Author(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email=models.EmailField(blank=True,verbose_name='e-mail')   #自定义字段标签
    #email = models.EmailField('e-mail', blank=True) 亦可

    def __str__(self):
        return u'%s %s' % (self.first_name,self.last_name)

class Book(models.Model):
    title=models.CharField(max_length=100)
    authors=models.ManyToManyField(Author)
    publisher=models.ForeignKey(Publisher)
    publication_date=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.title