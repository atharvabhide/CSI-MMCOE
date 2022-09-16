from django.shortcuts import render
from .models import Member

def about(request):
    members = list(Member.objects.all())
    return render(request, 'about.html', { 'member_list' : members })