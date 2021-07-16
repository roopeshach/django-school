from django.contrib import admin

# Register your models here.
from .models import school_info , Admin , Session , Department , Class , Section , Course , Teacher, Student


admin.site.register(school_info)
admin.site.register(Admin)
admin.site.register(Session)
admin.site.register(Department)
admin.site.register(Class)
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
