from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name: str = "home.html"

class AboutPageView(TemplateView):
    template_name: str = "about.html"