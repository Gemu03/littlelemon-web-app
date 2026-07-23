from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Set up DRF router for BookingViewSet
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    # Static HTML pages views (served by Django)
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('menu/', views.menu, name='menu'),

    # Menu API endpoints
    path('api/menu-items/', views.MenuItemsView.as_view(), name='menu_items'),
    path('api/menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),

    # Booking API endpoints (supports both /api/booking/tables/ and fallback /api/bookings/)
    path('api/booking/', include(router.urls)),
    path('api/bookings/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='bookings_list'),
    path('api/bookings/<int:pk>/', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='bookings_detail'),
]
