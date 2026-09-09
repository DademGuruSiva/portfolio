from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # 📩 Email to YOU (Owner)
            send_mail(
                "New Contact Form Submission",
                f"""
First Name: {contact.first_name}
Last Name: {contact.last_name}
Phone: {contact.phone_number}
Email: {contact.email}
Message:
{contact.message}
""",
                settings.EMAIL_HOST_USER,
                ['gurusiva14896@gmail.com'],
                fail_silently=False,
            )

            # 📩 Auto-reply to USER (Recruiter tone)
            send_mail(
                "Thank You for Visiting My Portfolio",
                f"""
Hi {contact.first_name},

Thank you for taking the time to visit my portfolio.

I truly appreciate your interest and would be happy to connect regarding any suitable opportunities.

Please feel free to reach out for further discussion.

Looking forward to your response.

Best Regards,  
DADEM GURU SIVA
""",
                settings.EMAIL_HOST_USER,
                [contact.email],
                fail_silently=False,
            )

            return render(request, 'success.html')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
