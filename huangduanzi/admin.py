from django.contrib import admin
# 在后台注册类
# from models import Huangduanzi
# admini.site.register(Huangduanzi)
# Register your models here.
'''
在admin后台 显示丰富的内容 如其他的字段
class HuangduanziAdmin(admin.ModelAdmin):
    list_display=('id','title','date')
    list_fiter =('date',)
admini.site.register(HuangduanziAdmin)
'''