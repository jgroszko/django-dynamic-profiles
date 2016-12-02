from django.contrib import admin
from dynamicprofiles.models import Profile, ProfileDataGroup, ProfileDataField, ProfileData, ProfileTextData

admin.site.register(Profile)

admin.site.register(ProfileDataGroup)
admin.site.register(ProfileDataField)
admin.site.register(ProfileData)
admin.site.register(ProfileTextData)
