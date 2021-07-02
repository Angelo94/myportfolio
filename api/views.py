from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer


class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(template_name='index.html')
