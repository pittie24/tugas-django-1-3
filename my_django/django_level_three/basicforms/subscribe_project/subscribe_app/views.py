from django.shortcuts import render
from subscribe_app.models import customer 
from subscribe_app.forms import NewSubscriber

# Create your views here.
def index(request):
    return render(request, 'subscribe_app/index.html')

def customers(request):
    customer_list = customer.objects.order_by('first_name')
    customer_dict = {'customers' :customer_list}
    return render(request, 'subscribe_app/customer.html', context=customer_dict)

def subscribe(request):
    form = NewSubscriber()

    if request.method == 'POST':
        form = NewSubscriber(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return customers(request)
        else:
            print("Error: Form invalid")

    return render  (request, 'subscribe_app/subscribe.html', {'form': form})