from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm

@login_required
def doctor_dashboard(request):
    context={'user': request.user}
    return render(request, 'doctor_dashboard.html', context)

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 'doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'doctor':
            return reverse_lazy('doctor_dashboard')
        elif user.user_type == 'patient':
            return reverse_lazy('patient_dashboard')
        return reverse_lazy('login')  # fallback
