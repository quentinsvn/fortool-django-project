from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from . import views
from .views import Landing, Content, Tipeeestream, Offerwalls, Coinflip, Loterie, Upgrade, Shop, Commands, Leaderboard, Informations, AssociatedAccounts, Security, Payments, History, Login, Register

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', Landing.as_view(), name='landing'),
    path('home/', Content.as_view(), name='content'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('win/tipeeestream/', Tipeeestream.as_view(), name='tipeeestream'),
    path('win/offerwalls/', Offerwalls.as_view(), name='offerwalls'),
    path('games/coinflip/', Coinflip.as_view(), name='coinflip'),
    path('games/loterie/', Loterie.as_view(), name='loterie'),
    path('games/upgrade/', Upgrade.as_view(), name='upgrade'),
    path('leaderboard/', Leaderboard.as_view(), name='leaderboard'),
    path('shop/catalog', Shop.as_view(), name='shop'),
    path('shop/commands', Commands.as_view(), name='commands'),
    path('settings/informations', Informations.as_view(), name='informations'),
    path('settings/associated-accounts', AssociatedAccounts.as_view(), name='associatedaccounts'),
    path('settings/security', Security.as_view(), name='security'),
    path('settings/payments', Payments.as_view(), name='payments'),
    path('settings/history', History.as_view(), name='history'),
    path('docs/', schema_view),
]
