from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'
    # Overriding the context variable to be used in the {% for group in group_list %} block
    # instead of {% group in object_list %}
    context_object_name = 'group_list'
