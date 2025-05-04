from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date'
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date'
    )
    class Meta:
        abstract = True

class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text = '',
    )
    parameter = models.CharField(
        default='',
        blank=True,
        verbose_name='Parameter',
        help_text = '',
    )


    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name', )

class ImageSetting(AbstractModel):
        name = models.CharField(
            default='',
            max_length=254,
            blank=True,
            verbose_name='Name',
            help_text='This is variable of the setting.',
        )
        description = models.CharField(
            default='',
            max_length=254,
            blank=True,
            verbose_name='Description',
            help_text='',
        )
        file =  models.ImageField(
            default='',
            blank=True,
            verbose_name='Image',
            help_text='',
            upload_to='images/',
        )


        def __str__(self):
            return f'Image Setting: {self.name}'

        class Meta:
            verbose_name = 'Image Setting'
            verbose_name_plural = 'Image Settings'
            ordering = ('name',)

class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(50), MaxValueValidator(100)],
    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)

class Resume(AbstractModel):
    Degree_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Degree Name',
    )
    start_date= models.DateField(
        verbose_name='Start Date',
    )
    end_date= models.DateField(
        default='None',
        null=True,
        blank=True,
        verbose_name='End Date',
    )
    school_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='School Location',
        help_text='School Name , Location',
    )
    parameter = models.CharField(
        default='',
        blank=True,
        verbose_name='Parameter',
        help_text='',
    )

    def __str__(self):
        return f'Resume: {self.Degree_name}'

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'
        ordering = ('-start_date',)

class Sumary(AbstractModel):
    name_surname= models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name Surname',
        help_text='This is variable of the setting.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text = '',
    )
    parameter = models.CharField(
        default='',
        blank=True,
        verbose_name='Parameter',
        help_text = '',
    )
    sumary_location= models.CharField(
        default='',
        blank=True,
        max_length=254,
        verbose_name='Location',
        help_text='',
    )
    sumary_email= models.CharField(
        default='',
        blank=True,
        max_length=254,
        verbose_name='Email',
        help_text='',
    )
    def __str__(self):
        return f'Sumary: {self.name_surname}'

    class Meta:
        verbose_name = 'Sumary'
        verbose_name_plural = 'Sumaries'

class Project(AbstractModel):
    Project_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Project',
    )

    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )

    parameter = models.CharField(
        default='',
        blank=True,
        verbose_name='Parameter',
        help_text='',
    )
    def __str__(self):
        return f'Project: {self.Project_name}'

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

class Certificate(AbstractModel):
    Certificate_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Certificate',
    )

    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )

    parameter = models.CharField(
        default='',
        blank=True,
        verbose_name='Parameter',
        help_text='',
    )
    def __str__(self):
        return f'Certificate: {self.Certificate_name}'

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'