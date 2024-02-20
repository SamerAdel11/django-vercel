from product.viewsets import ProductViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("product-abc",ProductViewSet,basename='products')
urlpatterns = router.urls
for url in urlpatterns:
    print(url,end='\n')