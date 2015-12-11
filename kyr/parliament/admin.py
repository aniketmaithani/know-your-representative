from django.contrib import admin
from .models import MemberOfParliament


class MemberOfParliamentAdmin(admin.ModelAdmin):

    '''
    Admin View For Member Of MemberOfParliament
    '''
    list_display = ('name_of_the_mp', 'state', 'photo_of_the_mp', 'constituency', 'attendance_percent',
                    'debates_total', 'no_of_questions_asked', 'private_member_bill_asked',)
    list_filter = ('name_of_the_mp',)
    search_fields = ('name_of_the_mp', 'state', 'constituency')

    def photo_of_the_area(self, obj):
        if obj.photo:
            return '<img src="%s"/>' % obj.photo.thumbnail['100x100'].url
        return '(None)'
    photo_of_the_area.allow_tags = True


admin.site.register(MemberOfParliament, MemberOfParliamentAdmin)
