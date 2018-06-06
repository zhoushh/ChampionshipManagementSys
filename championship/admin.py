from django.contrib import admin
from .models import Championship, Match, Team, TimetableForLeague
# Register your models here.

admin.site.register(Championship)
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(TimetableForLeague)