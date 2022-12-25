from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, TextField, DateField, URLField, BooleanField, EmailField, IntegerField, \
    ImageField, TextChoices, ForeignKey, SlugField
from django.utils.text import slugify
from django_resized import ResizedImageField


class User(AbstractUser):
    about = TextField(blank=True, null=True)
    age = IntegerField()
    degree = CharField(max_length=255)
    workspace = CharField(max_length=255, blank=True)
    gender = CharField(max_length=15, null=True, blank=True)
    address = CharField(max_length=255, null=True, blank=True)
    phone = CharField(max_length=15, null=True, blank=True)
    email = EmailField(unique=True, blank=True, max_length=254, verbose_name='email address')
    image = ImageField(null=True, blank=True, default='background_2.jpg',
                       upload_to='authors')
    profile_image = ImageField(null=True, blank=True, default='profile_image.jpg',
                               upload_to='authors')
    is_freelancer = BooleanField(default=True)
    address_url = URLField(null=True, blank=True)
    facebook_url = URLField(null=True, blank=True)
    twitter_url = URLField(null=True, blank=True)
    instagram_url = URLField(null=True, blank=True)
    linkedIn_url = URLField(null=True, blank=True)


class Skills(models.Model):
    name = CharField(max_length=255, null=True, blank=True)
    image = ImageField(null=True, blank=True, upload_to='%m')


class Facts(models.Model):
    happy_clients = IntegerField(null=True, blank=True)
    projects = IntegerField(null=True, blank=True)
    hours_of_support = IntegerField(null=True, blank=True)
    hard_workers = IntegerField(null=True, blank=True)


class Education(models.Model):
    bachelor = CharField(max_length=255, null=True, blank=True)
    years_of_bachelor = CharField(max_length=255, null=True, blank=True)
    bachelor_address = CharField(max_length=255, null=True, blank=True)
    about_bachelor = CharField(max_length=255, null=True, blank=True)

    master = CharField(max_length=255, null=True, blank=True)
    years_of_master = CharField(max_length=255, null=True, blank=True)
    master_address = CharField(max_length=255, null=True, blank=True)
    about_master = CharField(max_length=255, null=True, blank=True)


class ProfessionalExperience(models.Model):
    job_title = CharField(max_length=255, null=True, blank=True)
    about = TextField(null=True, blank=True)
    address = CharField(max_length=255, null=True, blank=True)
    years = CharField(max_length=50, null=True, blank=True)


class Services(models.Model):
    title = CharField(max_length=255, null=True, blank=True)
    about = CharField(max_length=255, null=True, blank=True)
    image = ImageField(default='default_service.jpg')


class Testimonials(models.Model):
    author = CharField(max_length=255)
    author_image = ResizedImageField(null=True, blank=True)
    testimonial = TextField()
    author_job = CharField(max_length=255, null=True, blank=True)


class Project(models.Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    category = CharField(max_length=255)
    client = CharField(max_length=255)
    date = DateField()
    url = URLField()
    about = TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if not self.slug:
            while Project.objects.filter(slug=self.slug).exists():
                slug = Project.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

        super().save(*args, **kwargs)


class Photo(models.Model):
    project = ForeignKey(Project, on_delete=models.CASCADE, related_name='photos')
    photo = ImageField(upload_to='photos/')


class Portfolio(models.Model):
    class CategoryChoice(TextChoices):
        ALL = 'all', 'xamasi'
        APPS = 'apps', 'applar'
        WEB = 'web', 'web'
        CARD = 'card', 'kartalar'

    category = CharField(max_length=55, choices=CategoryChoice.choices, default=CategoryChoice.ALL)
    project = ForeignKey(Project, models.CASCADE)


class ContactEmails(models.Model):
    author = CharField(max_length=255)
    email = EmailField(max_length=255)
    subject = CharField(max_length=255, blank=True)
    message = TextField()
