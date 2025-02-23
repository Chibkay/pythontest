from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse 

def register(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate and log in the user.  
            authenticated_user = authenticate(request, username=user.username, password=request.POST['password2']) # password2 is the confirmed password field
            if authenticated_user: # Check if authentication was successful.
                login(request, authenticated_user)
                return redirect('learning_logs:index') 
            else:
                # Handle authentication failure (e.g., set a message on the form)
                form.add_error(None, "Authentication failed. Please try again.") 
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)