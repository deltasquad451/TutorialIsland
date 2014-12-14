from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from quickstart import views
'''
Because we're using viewsets instead of views, we can automatically generate the URL conf for our API,
by simply registering the viewsets with a router class.
Again, if we need more control over the API URLs we can simply drop down to using regular class based views, 
and writing the URL conf explicitly.
Finally, we're including default login and logout views for use with the browsable API. 
That's optional, but useful if your API requires authentication and you want to use the browsable API.
'''


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups',views.GroupViewSet)
router.register(r'consuming',views.consumeViewSet)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TutorialIsland.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
)
