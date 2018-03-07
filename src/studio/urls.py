"""
    console top URL Configuration

    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/1.11/topics/http/urls/

    Examples:

    Function views
        1. Add an import:  from studio import views
        2. Add a URL to urlpatterns:  url('', views.home, name='home')

    Class-based views
        1. Add an import:  from studio.views import Home
        2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')

    Including another URLconf
        1. Import the include() function: from django.conf.urls import url, include
        2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""

from django.urls import path, re_path

from django.views.generic.base import RedirectView

from studio.views import (
    AICreateView,
    AIListView,
    AIDetailView,
    AIUpdateView,
    EntitiesUpdateView,
    EntitiesView,
    IntegrationFacebookView,
    IntegrationView,
    IntentsUpdateView,
    IntentsView,
    ProxyAiExportView,
    ProxyAiView,
    EntityDeleteView,
    IntentDeleteView,
    ProxyRegenerateWebhookSecretView,
    RetrainView,
    SkillsView,
    TrainingView,
    IntegrationFacebookView,
    FacebookIntegrationCustomiseView,
    InsightsView,
    ProxyInsightsLogsView,
    ProxyInsightsChartView
)

app_name = 'studio'

urlpatterns = [

    # Always use a path, explicit is better than implicit
    path(
        '',
        RedirectView.as_view(pattern_name='studio:summary'),
        name='index'
    ),

    # Summary page of studio app
    path(
        'summary',
        AIListView.as_view(),
        name='summary'
    ),

    # Create a new AI
    path(
        'bots/add',
        AICreateView.as_view(),
        name='add_bot'
    ),

    # Edit an existing AI
    path(
        'bots/edit/<uuid:aiid>',
        AIDetailView.as_view(),
        name='edit_bot'
    ),

    # Update training of an existing AI
    path(
        'bots/edit/<uuid:aiid>/training',
        TrainingView.as_view(),
        name='training'
    ),

    # Restart training of an AI
    path(
        'bots/edit/<uuid:aiid>/retrain',
        RetrainView.as_view(),
        name='retrain'
    ),

    # Update skills of an existing AI
    path(
        'bots/edit/<uuid:aiid>/skills',
        SkillsView.as_view(),
        name='skills'
    ),

    # Update entities of an existing AI
    path(
        'bots/edit/<uuid:aiid>/entities',
        EntitiesView.as_view(),
        name='entities'
    ),

    # Update an Entity of an existing AI
    path(
        'bots/edit/<uuid:aiid>/entities/<slug:entity_name>',
        EntitiesUpdateView.as_view(),
        name='entities.edit'
    ),

    # Update Intents of an existing AI
    path(
        'bots/edit/<uuid:aiid>/intents',
        IntentsView.as_view(),
        name='intents'
    ),

    # Update an Intent of an existing AI
    path(
        'bots/edit/<uuid:aiid>/intents/<slug:intent_name>',
        IntentsUpdateView.as_view(),
        name='intents.edit'
    ),

    # List the integration options for an existing AI
    path(
        'bots/edit/<uuid:aiid>/integrations',
        IntegrationView.as_view(),
        name='integrations'
    ),

    # List or update facebook integration for this AI
    re_path(
        r'^bots/edit/(?P<aiid>[0-9a-f-]+)/integrations/facebook/(?P<action>get|page|disconnect)/(?P<id>[0-9]*)$',
        IntegrationFacebookView.as_view(),

        name='integrations_facebook'
    ),

    # save customisations to facebook integration
    path(
        'bots/edit/<uuid:aiid>/integrations/facebook/customise',
        FacebookIntegrationCustomiseView.as_view(),
        name='integrations_facebook_customise'
    ),

    # Insights: download chat logs for an existing AI
    path(
        'bots/edit/<uuid:aiid>/insights/logs',
        ProxyInsightsLogsView.as_view(),
        name='insights_log_data'
    ),

    # Insights: download chart data for an existing AI
    path(
        'bots/edit/<uuid:aiid>/insights/chart',
        ProxyInsightsChartView.as_view(),
        name='insights_chart_data'
    ),

    # Display insights of an existing AI
    path(
        'bots/edit/<uuid:aiid>/insights',
        InsightsView.as_view(),
        name='insights'
    ),

    # Update settings of an existing AI
    path(
        'bots/edit/<uuid:aiid>/settings',
        AIUpdateView.as_view(),
        name='settings'
    ),

    # Proxy ajax AI calls
    path(
        'proxy/ai/<uuid:aiid>',
        ProxyAiView.as_view(),
        name='proxy.ai'
    ),

    path(
        'proxy/ai/<uuid:aiid>/export',
        ProxyAiExportView.as_view(),
        name='proxy.ai.export'
    ),

    path(
        'proxy/ai/<uuid:aiid>/regenerate_webhook_secret',
        ProxyRegenerateWebhookSecretView.as_view(),
        name='proxy.ai.regenerate_webhook_secret'
    ),

    # Remove an intent
    path(
        'intent/delete/<uuid:aiid>/<slug:intent_name>',
        IntentDeleteView.as_view(),
        name='intent.delete'
    ),

    # Remove an intent
    path(
        'entity/delete/<uuid:aiid>/<slug:entity_name>',
        EntityDeleteView.as_view(),
        name='entity.delete'
    ),
]
