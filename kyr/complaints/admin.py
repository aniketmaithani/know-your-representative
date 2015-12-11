# Third Party Stuff
from django.contrib import admin

from .models import Complaints


class ComplaintsAdmin(admin.ModelAdmin):

    '''
    Admin View for Complaints
    '''
    list_display = ('name_of_the_complainee', 'phone_number_of_the_complainee', 'photo_of_the_area',
                    'description_of_the_problem', 'name_of_the_mp_for_problem_redressal', 'unique_complain_id')
    list_filter = ('unique_complain_id', )
    search_fields = ['name_of_the_complainee', 'phone_number_of_the_complainee',
                     'description_of_the_problem', 'name_of_the_mp_for_problem_redressal', 'unique_complain_id', ]


    def photo_of_the_area(self, obj):
        if obj.photo:
            return '<img src="%s"/>' % obj.photo.thumbnail['100x100'].url
        return '(None)'
    photo_of_the_area.allow_tags = True


admin.site.register(Complaints, ComplaintsAdmin)
