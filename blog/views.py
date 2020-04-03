from django.views import generic
from django.views.generic import TemplateView


class Landing(TemplateView):
    template_name = 'landing.html'


class Content(TemplateView):
    template_name = 'content.html'


class Tipeeestream(TemplateView):
    template_name = 'win/tipeeestream.html'


class Offerwalls(TemplateView):
    template_name = 'win/offerwalls.html'


class Coinflip(TemplateView):
    template_name = 'games/coinflip.html'


class Loterie(TemplateView):
    template_name = 'games/loterie.html'


class Upgrade(TemplateView):
    template_name = 'games/upgrade.html'


class Shop(TemplateView):
    template_name = 'shop/catalog.html'


class Commands(TemplateView):
    template_name = 'shop/commands.html'


class Leaderboard(TemplateView):
    template_name = 'leaderboard.html'


class Informations(TemplateView):
    template_name = 'settings/informations.html'


class AssociatedAccounts(TemplateView):
    template_name = 'settings/associated-accounts.html'


class Security(TemplateView):
    template_name = 'settings/security.html'


class Payments(TemplateView):
    template_name = 'settings/payments.html'


class History(TemplateView):
    template_name = 'settings/history.html'


class Login(TemplateView):
    template_name = 'account/login.html'


class Register(TemplateView):
    template_name = 'account/register.html'

