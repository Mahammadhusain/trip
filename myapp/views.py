from django.shortcuts import render,redirect
from .models import VehicleModel,BookingModel
from .form import (BookingForm,UserLoginForm,UserRegistrationForm,
UserProfileChangeForm,PassChangeForm)

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from datetime import datetime,date
from .filter import SearchFilter
from django.core.paginator import Paginator
import razorpay
# Create your views here.



def HomeView(request):
    if request.user.is_authenticated:
        pass
        return render(request,'home.html')
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

def DashboardView(request):
    if request.user.is_authenticated:
        today = datetime.today()
        today_booked = BookingModel.objects.filter(user= request.user,book_date__year=today.year,book_date__month=today.month,book_date__day=today.day).count()
        total_booked = BookingModel.objects.filter(user= request.user).count()
        show_data = BookingModel.objects.filter(user= request.user)
        car_booked = BookingModel.objects.filter(user= request.user,v_type='Car').count()
        car_booked = BookingModel.objects.filter(user= request.user,v_type='Car').count()
        buses_booked = BookingModel.objects.filter(user= request.user,v_type='Bus').count()
        trains_booked = BookingModel.objects.filter(user= request.user,v_type='Train').count()
        flights_booked = BookingModel.objects.filter(user= request.user,v_type='Flight').count()
        
        # Pagination 
        paginator = Paginator(show_data, 3, orphans=1)
        page_number = request.GET.get('page')
        show_data = paginator.get_page(page_number)

        context = {'car_booked':car_booked,'buses_booked':buses_booked,
        'trains_booked':trains_booked,'flights_booked':flights_booked,
        'today_booked':today_booked,'total_booked':total_booked,
        'show_data':show_data,'page_number':page_number}
        return render(request,'dashboard.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')
    
def ProfileView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form =UserProfileChangeForm(request.POST,instance=request.user)
            
            if form.is_valid():
                form.save()
                messages.info(request,'Profile Successfully Updated')
                return redirect('/profile/')
        else:
            form =UserProfileChangeForm(instance=request.user)
            user_data = request.user
            context = {'form':form,'user_data':user_data}
        return render(request,'profile.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')
    
def SlipView(request,id):
    data = BookingModel.objects.get(id=id)
    context = {'data':data}
    return render(request,'slip.html',context)

def CarView(request):
    if request.user.is_authenticated:
        carset = VehicleModel.objects.filter(v_type='Car')
        myFilter =SearchFilter(request.GET,queryset=carset)
        carset = myFilter.qs
        

        # Pagination 
        paginator = Paginator(carset, 3, orphans=1)
        page_number = request.GET.get('page')
        carset = paginator.get_page(page_number)

        context = {'carset':carset,'myFilter':myFilter,'page_number':page_number}
        return render(request,'car.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

def BusView(request):
    if request.user.is_authenticated:
        busset = VehicleModel.objects.filter(v_type='Bus')
        myFilter =SearchFilter(request.GET,queryset=busset)
        busset = myFilter.qs

        # Pagination 
        paginator = Paginator(busset, 3, orphans=1)
        page_number = request.GET.get('page')
        busset = paginator.get_page(page_number)

        context = {'busset':busset,'myFilter':myFilter,'page_number':page_number}
        return render(request,'bus.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

def TrainView(request):
    if request.user.is_authenticated:
        trainset = VehicleModel.objects.filter(v_type='Train')
        myFilter =SearchFilter(request.GET,queryset=trainset)
        trainset = myFilter.qs

        # Pagination 
        paginator = Paginator(trainset, 3, orphans=1)
        page_number = request.GET.get('page')
        trainset = paginator.get_page(page_number)

        context = {'trainset':trainset,'myFilter':myFilter,'page_number':page_number}
        return render(request,'train.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

def FlightView(request):
    if request.user.is_authenticated:
        flightset = VehicleModel.objects.filter(v_type='Flight')
        myFilter =SearchFilter(request.GET,queryset=flightset)
        flightset = myFilter.qs

        # Pagination 
        paginator = Paginator(flightset, 3, orphans=1)
        page_number = request.GET.get('page')
        flightset = paginator.get_page(page_number)

        context = {'flightset':flightset,'myFilter':myFilter,'page_number':page_number}
        return render(request,'flight.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')


def BookingView(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            info = VehicleModel.objects.get(id=id)
            form = BookingForm(request.POST) 
            amount =(info.price)*100
            client = razorpay.Client(
            auth=("rzp_test_3TgO7ZbqAF1dN1", "eONIoTp17Y0eAGU0UTuJ0C44"))
            payment = client.order.create({'amount': amount, 'currency': 'INR',
                                                    'payment_capture': '1'})
            if form.is_valid():
                fname = form.cleaned_data['fname']
                lname = form.cleaned_data['lname']
                mobile = form.cleaned_data['mobile']
                email = form.cleaned_data['email']
                gender = form.cleaned_data['gender']
                data = BookingModel(
                    user = request.user,
                    fname = fname,
                    lname= lname,
                    mobile=mobile,
                    email=email,
                    gender=gender,
                    provider=info.provider,
                    from_location=info.from_location,
                    to_location=info.to_location,
                    class_type=info.v_class,
                    v_type=info.v_type,
                    duration=info.duration,
                    total=info.price,
                )
                data.save()
                messages.success(request,'You Ticket Successfully Booked...!!')
                return redirect('/dashboard/')
        else:
            info = VehicleModel.objects.get(id=id)
            form = BookingForm()
            amount =(info.price)*100
            client = razorpay.Client(
            auth=("rzp_test_3TgO7ZbqAF1dN1", "eONIoTp17Y0eAGU0UTuJ0C44"))
            payment = client.order.create({'amount': amount, 'currency': 'INR',
                                                    'payment_capture': '1'}) 
        context = {'info':info,'form':form,'payment':payment}
        return render(request,'booking.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')



# Auth

def SigninView(request):
    form = UserLoginForm()
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username=uname,password=upass)
        if user is None:
            messages.error(request,'Please Enter Correct Credinatial')
            return redirect('/signin/')
        else:
            login(request,user)
            messages.info(request,'Login Successful')
            return redirect('/dashboard/')
    else:
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        else:
            return render(request,'signin.html',{'form':form})
    return render(request,'signin.html',{'form':form})



def RegisterView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Registred')
        return render(request, 'register.html', {'form': form})
    else:
        form = UserRegistrationForm()
    context = {'form': form, }
    return render(request, 'register.html', context)


def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, '🙋‍ You are Successfully Logged Out !')
        return redirect('/signin')
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')

def ChangePassView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PassChangeForm(user = request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Password Successfully Changed')
        else:
            form = PassChangeForm(user =request.user)
        context= {'form':form}
        return render(request,'changepass.html',context)
    else:
        messages.info(request, '☹︎ Please Login First')
    return redirect('/signin')



# TEST KEY : rzp_test_3TgO7ZbqAF1dN1
# TEST ID : eONIoTp17Y0eAGU0UTuJ0C44









