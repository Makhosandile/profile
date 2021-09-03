from django.urls import path, include
from projects import views

urlpatterns = [
    path("", views.ProjectList.as_view()),
    #path("<int:pk>/", views.project_detail, name="project_detail"),
    path('list/', views.APIList.as_view()),
    path('details/<int:pk>/', views.ProjectDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
