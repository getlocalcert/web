from . import views
from django.urls import path

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("accounts/login/", views.login_page, name="login"),
    path("list-zones", views.list_zones, name="list_zones"),
    path(
        "register-subdomain",
        views.register_subdomain,
        name="register_subdomain",
    ),
    path(
        "instant-subdomain",
        views.instant_subdomain,
        name="create_instant_subdomain",
    ),
    path("describe-zone", views.describe_zone, name="describe_zone"),
    path(
        "add-record",
        views.add_record,
        name="add_record",
    ),
    path(
        "delete-record",
        views.delete_record,
        name="delete_record",
    ),
    path(
        "create-zone-api-key",
        views.create_zone_api_key,
        name="create_zone_api_key",
    ),
    path(
        "delete-zone-api-key",
        views.delete_zone_api_key,
        name="delete_zone_api_key",
    ),
    path(
        "stats",
        views.show_stats,
        name="stats",
    ),
    # API paths are versioned
    path(
        "api/v1/health",
        views.api_health,
        name="api_health",
    ),
    path(
        "api/v1/check",
        views.api_check_key,
        name="api_check_key",
    ),
    path(
        "api/v1/register",
        views.api_instant_subdomain,
        name="api_instant_subdomain",
    ),
    # ACME DNS APIs are namespaced
    path(
        "api/v1/acme-dns-compat/health",
        views.acmedns_api_health,
        name="acmedns_api_health",
    ),
    path(
        "api/v1/acme-dns-compat/update",
        views.acmedns_api_update,
        name="acmedns_api_update",
    ),
    path(
        "api/v1/acme-dns-compat/register",
        views.acmedns_api_register,
        name="acmedns_api_register",
    ),
]
