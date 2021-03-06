import logging

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from users.services import get_info

logger = logging.getLogger(__name__)


def has_info(function):
    """Check if user has a developer info, if not move them to info form"""

    def wrap(request, *args, **kwargs):
        try:
            get_info(
                request.session['token'],
                request.session['dev_id']
            )
            return function(request, *args, **kwargs)
        except Exception as e:
            messages.warning(
                request,
                _('This is your first bot. Before publishing this to our store '
                    'we need to collect some developer details.')
            )
            return HttpResponseRedirect(
                '{path}?next={next}'.format(
                    path=reverse('users:info'),
                    next=request.path_info
                )
            )

    return wrap
