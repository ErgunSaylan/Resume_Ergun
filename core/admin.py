from django.contrib import admin
from core.models import *
# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']
    class Meta:
        model = GeneralSetting

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']
    class Meta:
        model = ImageSetting

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['order', 'name', 'percentage']
    class Meta:
        model = Skill

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'Degree_name', 'start_date', 'end_date', 'school_location', 'parameter', 'updated_date', 'created_date',]
    search_fields = ['Degree_name','school_location']
    list_editable = ['Degree_name', 'start_date', 'end_date', 'school_location', 'parameter']
    class Meta:
        model = Resume

@admin.register(Sumary)
class SumaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_surname', 'description', 'parameter', 'sumary_location', 'sumary_email', 'updated_date', 'created_date',]
    search_fields = ['name_surname','sumary_location']
    list_editable = ['name_surname', 'description', 'parameter', 'sumary_location', 'sumary_email']
    class Meta:
        model = Sumary

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'Project_name', 'description', 'parameter']
    search_fields = ['Project_name', 'description', 'parameter']
    list_editable = ['Project_name','description', 'parameter']
    class Meta:
        model = Project

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'Certificate_name', 'description', 'parameter']
    search_fields = ['Certificate_name', 'description', 'parameter']
    list_editable = ['Certificate_name','description', 'parameter']
    class Meta:
        model = Certificate

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'link', 'icon']
    search_fields = ['link', 'icon']
    list_editable = ['order', 'link', 'icon']
    class Meta:
        model = SocialMedia

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'slug', 'button_text', 'file']
    search_fields = ['slug', 'button_text']
    list_editable = ['order', 'slug', 'button_text', 'file']
    class Meta:
        model = Document

@admin.register(Ergun)
class ErgunAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'parameter']
    list_editable = ['name', 'parameter']
    class Meta:
        model = Ergun

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parameter','icon', 'updated_date', 'created_date']
    search_fields = ['name', 'parameter','icon']
    list_editable = ['name', 'parameter','icon']
    class Meta:
        model = Activity