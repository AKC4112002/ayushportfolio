from django.shortcuts import render
from django.contrib import messages

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

# def contact(request):
#     return render(request, 'portfolio/contact.html')

def resume(request):
    return render(request, 'portfolio/resume.html')




from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Email content
        subject = f"New Contact Form Submission from {name}"
        message_body = f"""
        You have received a new message from your website contact form:

        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """
        from_email = email
        recipient_list = ['your_email@gmail.com']  # Your email to receive messages
        
        try:
            send_mail(subject, message_body, from_email, recipient_list)
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, 'There was an error sending your message. Please try again later.')
    
    return render(request, 'portfolio/contact.html')
