from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


schema_view = get_schema_view(
    openapi.Info(
        title="Invent API",
        default_version="v8",
        description="Invent API Documentation ",
        terms_of_service="https://www.invent.com/policies/terms/",
        contact=openapi.Contact(email="invent@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Swagger Wrapper
def swagger_default_wrapper(fields):
    documentation = swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={field: openapi.Schema(type=fields[field]) for field in fields},
        )
    )
    return documentation

page = openapi.Parameter("page", openapi.IN_QUERY, type=openapi.TYPE_STRING)