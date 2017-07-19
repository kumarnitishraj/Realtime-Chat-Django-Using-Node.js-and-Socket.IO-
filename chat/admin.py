from django.contrib import admin
from .models import Comments
from django.contrib.auth.models import Group

class CommentModelAdmin(admin.ModelAdmin):
	list_display = ['__str__']

	class Meta:
		model = Comments


admin.site.register(Comments, CommentModelAdmin)
admin.site.unregister(Group)


# Register your models here.
