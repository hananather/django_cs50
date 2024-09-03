from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name = "index"),
	path("hanan", views.hanan, name="hanan"), # the url should be "../hanan"
	path("<str:name>", views.greet, name="greet") # 
]
