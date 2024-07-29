from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Cart/', include('Cart.urls')),
    path('', include('Product.urls')),
    path('Account/', include('Account.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
