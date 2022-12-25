from django.contrib import admin

from apps.models import Skills, Facts, Education, ProfessionalExperience, Services, Testimonials, User, Project, Photo, \
    Portfolio, ContactEmails


@admin.register(Skills)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)
    exclude = []


class PhotoAdmin(admin.StackedInline):
    model = Photo


@admin.register(Project)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('name', 'url',)
    exclude = ['slug']
    inlines = [PhotoAdmin]


@admin.register(ContactEmails)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'subject', 'message')


@admin.register(Portfolio)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('project', 'category',)
    exclude = []


@admin.register(User)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name',)
    exclude = []


@admin.register(Facts)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('projects', 'happy_clients', 'hours_of_support', 'hard_workers')
    exclude = []


@admin.register(Education)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('bachelor', 'master',)


@admin.register(ProfessionalExperience)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'years',)
    exclude = []


@admin.register(Services)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('title', 'about',)
    exclude = []


@admin.register(Testimonials)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('author', 'testimonial',)
