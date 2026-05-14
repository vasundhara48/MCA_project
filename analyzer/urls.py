from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('remove-skill/<int:skill_id>/', views.remove_skill, name='remove_skill'),
    path('set-target-role/', views.set_target_role, name='set_target_role'),
    path('analyze/', views.analyze, name='analyze'),
    path('results/<int:analysis_id>/', views.results, name='results'),
    path('roadmap/<int:analysis_id>/', views.roadmap, name='roadmap'),
]