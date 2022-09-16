from django.shortcuts import render
from .models import Member
def about(request):

    members = list(Member.objects.all())
    # member_list: list[tuple] = []
    # members_tuple = []
    # for cnt, member in enumerate(members):
    #     if (cnt+1)%4 != 0:
    #         members_tuple.append(member)
    #     else:
    #         member_list.append(members_tuple)
    #         members_tuple = []
    # member_list.append(members_tuple)
    return render(request, 'about.html', { 'member_list' : members })