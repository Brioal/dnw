from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

class SimpleMiddleware(MiddlewareMixin):
    def process_response(self, request, response):

        # if request.path != '/login/' and request.path != '/Web/CheckCode/':
        #     if  request.session.get('user',None):
        #         pass
        #     else:
        #         return HttpResponseRedirect('/login/')
        # if request.path == '/admin/users/myuser/add/':
        #     try:
        #         # email = request.POST['email']
        #         # parent_id = request.user.id
        #         # admin_level = 2
        #         # if request.user.admin_level < 2:
        #         #     admin_level = request.user.admin_level + 1
        #
        #
        #     except:
        #         pass

        return response

