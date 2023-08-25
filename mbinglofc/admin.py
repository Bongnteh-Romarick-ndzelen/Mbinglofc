from django.contrib import admin
from .models import Profile, BlogPost, Contact, UpcomingMatches, Results

# Register your models here.
class MatchesAdmin(admin.ModelAdmin):
    list_display = ('team1','team2','match_date', 'time')
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'date_send')
class ResultAdmin(admin.ModelAdmin):
    list_display = ('competition_name','date','scores')

admin.site.register(Profile)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(UpcomingMatches, MatchesAdmin)
admin.site.register(Results, ResultAdmin)