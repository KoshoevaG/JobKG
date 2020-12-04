from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from main.views import ProductsList, ProductDetails, CreateProduct, UpdateProduct, DeleteProduct
from rest_framework.routers import DefaultRouter

from jobs.views import JobViewSet

router = DefaultRouter()
router.register('job', JobViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('account.urls')),
    path('', include(router.urls))
    # path('products/', ProductsList.as_view()),
    # path('products/create/', CreateProduct.as_view()),
    # path('products/update/<int:pk>/', UpdateProduct.as_view()),
    # path('products/delete/<int:pk>/', DeleteProduct.as_view()),
    # path('products/<int:pk>/', ProductDetails.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)