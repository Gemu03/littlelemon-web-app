from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Django HTML templates views
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')

def menu(request):
    menu_data = Menu.objects.all().order_by('title')
    return render(request, 'menu.html', {'menu': menu_data})

# DRF REST API views
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all().order_by('title')
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('booking_date')
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
