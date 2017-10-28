from django.contrib import admin
from .models import Assignments,Lab_Manuals,Reference_Material,Sample_Papers,Timetable
# Register your models here.
class assgnAdmin(admin.ModelAdmin):
	class Meta:
		model = Assignments
admin.site.register(Assignments,assgnAdmin)

class assgnAdmin1(admin.ModelAdmin):
	class Meta:
		model = Lab_Manuals
admin.site.register(Lab_Manuals,assgnAdmin1)

class assgnAdmin2(admin.ModelAdmin):
	class Meta:
		model = Reference_Material
admin.site.register(Reference_Material,assgnAdmin2)

class assgnAdmin3(admin.ModelAdmin):
	class Meta:
		model = Sample_Papers
admin.site.register(Sample_Papers,assgnAdmin3)

class assgnAdmin4(admin.ModelAdmin):
	class Meta:
		model = Timetable
admin.site.register(Timetable,assgnAdmin4)

