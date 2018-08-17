from django.shortcuts import render

# Create your views here.
from indexpage.models import Notice
from users.models import MyUser


def index_page(request):
    admin_user = request.user
    back_notice_message = ""
    if(request.user.job == 4):
        num = 0
        back_notice_message = ", 您今天有" + str(num) + "位用户待回访"

    if (request.user.admin_level == 2):
        admin_user = MyUser.objects.get(id=request.user.parent_id)
    message_list = Notice.objects.values_list('message', flat=True)
    context = {
        'admin_user': admin_user,
        'back_notice_message': back_notice_message,
        'message_list': message_list,
    }

    return render(request, 'indexpage/index.html', context)