from django.core.mail import EmailMultiAlternatives
from django.template import Template, Context
from django.conf import settings

# from django.templatetags.static import static
from datetime import datetime

from django.urls import reverse


# def send_cancellation(users, order):
#     send_mail(
#         from_email=None,
#         subject="Verify you email address",
#         message="?",
#         fail_silently=False,
#         recipient_list=users,
#     )


def send_invoice(request, order):
    t = Template(open(settings.INVOICE_PATH).read())
    items = [
        {"description": f"Rent car: {order.car_design.car.brand}", "amount": 1},
    ]
    items += [
        {
            "description": f"Addon: {option_info.option.title}",
            "amount": option_info.count,
        }
        for option_info in order.added_options_info.all()
    ]
    c = Context(
        {
            "name": order.user.first_name,
            "receipt_id": order.id,
            "date": datetime.now().strftime("%m/%d/%Y <br> %H:%M:%S"),
            "items": items,
            "total": order.cost,
            "contact_url": request.build_absolute_uri(reverse("contactus")),
            "homepage": request.build_absolute_uri(reverse("home")),
            # "logo_url": request.build_absolute_uri(static("imghomePage/logoo.png")),
        }
    )
    body_html = t.render(c)
    message = EmailMultiAlternatives(
        subject=f"Your Receipt For Payment (Order #{order.id})",
        body=body_html,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[order.user],
    )
    message.mixed_subtype = "related"
    message.attach_alternative(body_html, "text/html")
    message.send(fail_silently=False)
