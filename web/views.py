from django.shortcuts import render, redirect
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm, SubscribeForm
from .models import ContactMessage, Subscribe
from django.contrib import messages



def home(request):
    subscribe_form = SubscribeForm()
    context={
        'subscribe_form': subscribe_form
    }
    return render(request, 'web/index.html', context)


def about(request):
    return render(request, 'web/aboutus.html')

def success(request):
    return render(request, 'web/success.html')

def Subsuccess(request):
    return render(request, 'web/Sub_success.html')  

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Save message to database
            contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
            contact_message.save()
            
            # Send email to host email(company email)
            host_subject = 'New contact form submission'
            host_message = f"A new contact form has been submitted by {name} ({email}).\n\nSubject: {subject}\n\nMessage: {message}"
            send_mail(host_subject, host_message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])


            # Retrieve email addresses of all messages in the database
            messages = ContactMessage.objects.all()
            recipient_list = [message.email for message in messages]

            # Send email to recipient(individuals that contact the company)
            recipient_list = [email]
            subject= 'Re Enquiry'
            message = f"Dear {name},\n\nThank you for contacting us. We will get back to you as soon as possible.\n\nBest regards,\n\n\nMikdol&Partners"
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)


            return redirect('success')
    else:
        form = ContactForm()
        return render(request, 'web/contactus1.html', {'form': form})

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            print(f"Subscribe form data: {first_name}, {last_name}, {email}")
            
            if Subscribe.objects.filter(email=email).exists():
                print(f"Email address {email} is already subscribed.")
                messages.warning(request, 'You have already subscribed to our newsletter.')
            else:
                subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
                subscribe.save()
                print(f"Saved subscription: {subscribe}")
                subject = f"Dear {first_name}, Thanks for subscribing to our newsletter!"
                message = 'Welcome to our newsletter! You will now receive regular updates from us.'
                from_email = settings.EMAIL_HOST_USER
                to = [email]
                send_mail(
                    subject, 
                    message, 
                    from_email, 
                    to, 
                    fail_silently=False
                )
                messages.success(request, 'You have successfully subscribed to our newsletter!')
                print(f"Saving new subscription: {subscribe}")
                return redirect('Subsuccess')  # redirect to the success page after successful subscription
        else:
            messages.error(request, 'Please enter valid information.')
    else:
        form = SubscribeForm() 

    context = {
        'form': form
    }
    return render(request, 'web/index.html', context)

                
            
            
            
        


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             # Save message to database
#             contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
#             contact_message.save()

#             # Send email to recipient
#             recipient_list = ['adefolaluadegboyega@gmail.com', 'goingwelllogic@gmail.com']
#             email_message = EmailMessage(
#                 subject=subject,
#                 body=message,
#                 from_email=settings.EMAIL_HOST_USER,
#                 to=[recipient_list],
#                 reply_to=[email],
#             )
#             email_message.send()

#             return redirect('success')
#     else:
#         form = ContactForm()
#     return render(request, 'web/contact.html', {'form': form})



# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             # Save message to database
#             contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
#             contact_message.save()

#             # Send email to recipient
#             recipient_list = [email]
#             send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

#             return redirect('success')
#     else:
#         form = ContactForm()
#     return render(request, 'web/contact.html', {'form': form})

    
  
    
   


