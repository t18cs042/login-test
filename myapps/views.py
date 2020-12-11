from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView):
    template_name = "myapps/index.html"
    
class TestView(LoginRequiredMixin,TemplateView):
    template_name = "myapps/test.html"
    login_url='/login/'