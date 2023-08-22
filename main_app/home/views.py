""" Home views"""

# Django
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """ Home View """

    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        """ Handle GET requests """
        context = self.get_context_data(**kwargs)
        context["user"] = request.user

        return self.render_to_response(context)
