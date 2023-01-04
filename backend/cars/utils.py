from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
from django.template import Template, Context

# You probably want all the following code in a function or method.
# You also need to set subject, sender and to_mail yourself.
# html_content = render_to_string("foo.html", context)
# text_content = render_to_string("foo.txt", context)
# msg = EmailMultiAlternatives(subject, text_content, sender, [to_mail])

# msg.attach_alternative(html_content, "text/html")

# msg.mixed_subtype = "related"

# for f in ["img1.png", "img2.png"]:
#     fp = open(os.path.join(os.path.dirname(__file__), f), "rb")
#     msg_img = MIMEImage(fp.read())
#     fp.close()
#     msg_img.add_header("Content-ID", "<{}>".format(f))
#     msg.attach(msg_img)

# msg.send()


def send_cancellation(users, order):
    send_mail(
        from_email=None,
        subject="Verify you email address",
        message="?",
        fail_silently=False,
        recipient_list=users,
    )


def send_invoice(user, order):
    t = Template(open("../invoice.html").read())
    c = Context(
        {
            "name": "Adrian",
            "credit_card_brand": "brand",
            "credit_card_last_four": "gg",
            "expiration_date": "date",
            "receipt_id": 1,
            "each_receipt_details": "hh",
            "each": "jj",
            "date": "j",
            "description": "description",
            "amount": "amount",
            "total": "total",
        }
    )
    rendered = t.render(c)
    open("../rendered.html", "w").write(rendered)

    send_mail(
        from_email=None,
        subject="Verify you email address",
        message="?",
        fail_silently=False,
        recipient_list=[user],
    )
