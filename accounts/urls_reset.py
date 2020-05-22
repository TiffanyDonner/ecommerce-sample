# from django.urls import re_path, reverse_lazy
# from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# urlpatterns = [
#     re_path('^$', PasswordResetView(), {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
#     re_path(r'^done/$', PasswordResetDoneView(), name='password_reset_done'),
#     re_path(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView(),
#         {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
#     re_path('^complete/$', PasswordResetCompleteView(), name='password_reset_complete')
# ]

from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url(r'^complete/$', password_reset_complete, name='password_reset_complete'),
]
