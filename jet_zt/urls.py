from django.conf.urls import *

import jet_zt.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'jet_zt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', jet_zt.views.home),

]
