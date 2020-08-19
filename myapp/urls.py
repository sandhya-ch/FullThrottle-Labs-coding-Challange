from rest_framework import routers
from myapp.views import Userviewset,ActivityPeriodviewset

router=routers.SimpleRouter()
router.register(r'users',Userviewset)
router.register(r'active',ActivityPeriodviewset)
urlpatterns=router.urls