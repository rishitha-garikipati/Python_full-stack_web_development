from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Hotel

from django.shortcuts import render, redirect
from .models import Hotel

def add_hotel(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        rating = request.POST.get('rating')
        room_type = request.POST.get('room_type')
        price_per_night = request.POST.get('price_per_night')
        number_of_rooms = request.POST.get('number_of_rooms')
        wifi_available = request.POST.get('wifi_available', False) == 'true'  # Convert to boolean
        pool_available = request.POST.get('pool_available', False) == 'true'  # Convert to boolean
        gym_available = request.POST.get('gym_available', False) == 'true'  # Convert to boolean
        Laundry_facilities = request.POST.get('Laundry_facilities', False) == 'true'
        Parking = request.POST.get('Parking', False) == 'true'
        Restaurant = request.POST.get('Restaurant', False) == 'true'
        image = request.FILES.get('image')

        # Create a new Hotel object with the provided data
        hotel = Hotel.objects.create(
            name=name,
            location=location,
            rating=rating,
            room_type=room_type,
            price_per_night=price_per_night,
            number_of_rooms=number_of_rooms,
            wifi_available=wifi_available,
            pool_available=pool_available,
            gym_available=gym_available,
            image=image
        )
        # Set additional facilities if they are provided
        if hasattr(hotel, 'Laundry_facilities'):
            hotel.Laundry_facilities = Laundry_facilities
        if hasattr(hotel, 'Parking'):
            hotel.Parking = Parking
        if hasattr(hotel, 'Restaurant'):
            hotel.Restaurant = Restaurant
        hotel.save()  # Save the changes

        return redirect('view_hotels')  # Redirect to view_hotels view
    return render(request, 'add_hotel.html')  # Render add_hotel.html template if request method is not POST

def view_hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'view_hotels.html', {'hotels': hotels})

def delete_hotel(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    hotel.delete()
    return redirect(view_hotels)

def search_view(request):
    if request.method == 'GET':
        location = request.GET.get('location')
        results = Hotel.objects.filter(location__icontains=location)
        return render(request,'bookhotel.html',{'hotels': results})
    else:
        return render(request,{'error': 'Method not allowed'}, status=405)

def adminhomepage(request):
    return render(request,'adminhomepage.html')

def hoteloverview(request,hotel_id):
    hotel = Hotel.objects.filter(pk=hotel_id)
    return render(request,'hoteloverview.html',{'hotels': hotel})

