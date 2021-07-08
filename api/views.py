from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.core.mail import send_mail
from myportfolio.settings import EMAIL_SEND_TO


class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(template_name='index.html')


class SendMessage(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def post(self, request):
        send_mail(subject='MyPortfolio',
                  message='{} {} {}'.format(request.data['name'], request.data['phone'], request.data['message']),
                  from_email=request.data['email'],
                  recipient_list=[EMAIL_SEND_TO],
                  fail_silently=False)

        return redirect('portfolio-home')