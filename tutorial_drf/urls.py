## tutorial 1
# from django.conf.urls import url, include


# urlpatterns = [
#     url(r'^', include('snippets.urls')),

#     ## tutorial 4
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
#     ##
# ]
##


## tutorial 6
from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
# router = DefaultRouter()
## tutorial 7
router = DefaultRouter(schema_title='Pastebin API')
##

router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
##