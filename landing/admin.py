from django.contrib import admin
from .models import *


class SubscriberAdmin (admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Subscriber._meta.fields]
   # list_filter = ['name',]
    search_fields = ['name', 'email']



# class Houses(admin.ModelAdmin):
#     list_display = [field.name for field in Subscriber._meta.fields]
#     search_fields = ['har', 'http', 'price']

   # fields = ["email"]

    # exclude = ["email"]
	# inlines = [FieldMappingInline]
	# fields = []
    # #exclude = ["type"]
	# #list_filter = ('report_data',)
	# search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = Subscriber
        model = Marks
        model = Pass
        model = Schedule
        model = Teachers
        model = Pupil
        model = Subjects
        model = Employee
        # model = Users
        # model = Houses

admin.site.register(Subscriber, SubscriberAdmin)
# admin.site.register(Houses)