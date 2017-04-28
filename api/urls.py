from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt import views as jwt_views
from djoser import views as djoser_views
from rest_framework.schemas import get_schema_view
from api import views as api_views

schema_view = get_schema_view(title='Rasterbucket API')
swagger_view = get_swagger_view(title='Rasterbucket API')

urlpatterns = [
    url(r'^schema/$',
        schema_view,
        name="schema"),
    url(r'^docs/',
        swagger_view,
        name="docs"),

    # Security
    url(r'^auth/signup/$',
        api_views.UserView.as_view(),
        name="signup"),
    url(r'^auth/$',
        jwt_views.obtain_jwt_token,
        name='login'),
    url(r'^auth_verify/$',
        jwt_views.verify_jwt_token),
    url(r'^auth/login',
        jwt_views.obtain_jwt_token,
        name='API login'),  # using JSON web token
    url(r'^auth/me',
        djoser_views.UserView.as_view(),
        name='API user'),
    url(r'^auth/register',
        djoser_views.RegistrationView.as_view(),
        name='API register'),
    url(r'^auth/activate',
        djoser_views.ActivationView.as_view(),
        name='API activate'),
    url(r'^auth/password/reset',
        djoser_views.PasswordResetView.as_view(),
        name='API password reset'),
    url(r'^auth/password/reset/confirm',
        djoser_views.PasswordResetConfirmView.as_view(),
        name='API password reset confirmation'),
    url(r'^passwordless/',
        include('drfpasswordless.urls')),
    url(r'^auth/social/',
        include('rest_framework_social_oauth2.urls')),

    # Rasterbucket
    url(r'^rasterbuckets/$',
        api_views.RasterbucketCreateView.as_view(),
        name='api.rasterbuckets'),
    url(r'^rasterbuckets/(?P<pk>[0-9]+)/$',
        api_views.RasterbucketDetailsView.as_view(),
        name="api.rasterbuckets.details"),

    url(r'^rasterbuckets/(?P<pk>[0-9]+)/services/$',
        api_views.RasterbucketServiceCreateView.as_view(),
        name="api.rasterbuckets.services"),
    url(r'^rasterbuckets/(?P<pk>[0-9]+)/services/(?P<pk_service>[0-9]+)/$',
        api_views.RasterbucketServiceDetailView.as_view(),
        name="api.rasterbuckets.services.details"),

    url(r'^rasterbuckets/(?P<pk>[0-9]+)/services/(?P<pk_service>[0-9]+)/maps/$',
        api_views.GEEMapServiceCreateView.as_view(),
        name="api.rasterbuckets.services.geemapservices.create"),
    url(r'^rasterbuckets/(?P<pk>[0-9]+)/services/(?P<pk_service>[0-9]+)/maps/(?P<pk_map>[0-9]+)/$',
        api_views.MapServiceDetailView.as_view(),
        name="api.rasterbuckets.services.mapservice.detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)
