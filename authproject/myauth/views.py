from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)  # Auto-login after signup
            return redirect('login')  # Redirect to home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'myauth/signup.html', {'form': form})


from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib import messages
from django.urls import reverse

def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()
        
        if user:
            # Generate reset link
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_url = request.build_absolute_uri(reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token}))

            # Send email
            subject = "Password Reset Request"
            message = render_to_string('registration/password_reset_email.html', {'reset_url': reset_url})
            send_mail(subject, message, 'admin@example.com', [email])

            messages.success(request, "Password reset link sent to your email.")
            return redirect("password_reset_done")
        else:
            messages.error(request, "No account found with this email.")

    return render(request, "registration/password_reset_form.html")

from django.contrib.auth import update_session_auth_hash

def password_reset_confirm(request, uidb64, token):
    from django.utils.http import urlsafe_base64_decode

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == "POST":
            password = request.POST.get("password")
            password_confirm = request.POST.get("password_confirm")

            if password == password_confirm:
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user)  # Keep the user logged in
                messages.success(request, "Password successfully changed.")
                return redirect("login")
            else:
                messages.error(request, "Passwords do not match.")
        
        return render(request, "registration/password_reset_confirm.html")
    else:
        messages.error(request, "Invalid or expired reset link.")
        return redirect("password_reset")
