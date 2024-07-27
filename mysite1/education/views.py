import random
from datetime import datetime, timedelta
from django.contrib.auth.hashers import check_password, make_password
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from .helpers import MessageHandler
from django.contrib.auth import get_user_model, authenticate
# from paypalrestsdk import Payment, configure
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import *
from .models import *
from .token import account_activation_token
from mysite1 import settings
from django.views.decorators.cache import never_cache
from django.views.generic.edit import FormView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required


# import logging
# from paypal.standard.forms import PayPalPaymentsForm
# from paypal.standard.models import ST_PP_COMPLETED
# from paypal.standard.ipn.signals import valid_ipn_received


def Faculty_Page(request):
    return render(request, 'home.html')

@never_cache
def homefn(request):
    # records = user.objects.all()
    # product1 = home_add.objects.all()
    return redirect(register1)


@never_cache
def inactive1(request):
    return render(request, 'logout.html')


@never_cache
def my_view(request):
    last_activity = request.session.get('last_activity')
    if not last_activity:
        last_activity = timezone.now()
    context = {'last_activity': last_activity.isoformat()
               }
    return render(request, 'home.html', context)


@never_cache
def register1(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        un = request.POST['Un']
        Em = request.POST['Em']
        pw1 = request.POST['pw1']
        pw2 = request.POST['pw2']
        Role1 = request.POST['Role1']
        phone_number = request.POST['phone_number45']

        email_exists = user.objects.filter(email=Em).exists()
        if email_exists:
            Err = 'This Email Address Is Already Registered'
            return render(request, 'App1/register.html', {'ERROR2': Err})

        username_exists = user.objects.filter(uname=un).exists()
        if username_exists:
            Err = 'The Username Is Already Exists.'
            return render(request, 'App1/register.html', {'ERROR': Err})

        Phone_Number = user.objects.filter(phone_number=phone_number).exists()
        if Phone_Number:
            Err = 'The Number You Have Entered Is Already Exists !! '
            return render(request, 'App1/register.html', context={'Error3': Err})

        if pw1 == pw2:
            Hashed_password = make_password(pw1)
            u1 = user(fname=fn, lname=ln, uname=un, password=Hashed_password, email=Em, Field=Role1, phone_number=phone_number)
            u1.save()
            # send_mail(f'Welcome to Our Website !!',
            #           f'Hello {fn},\nThank you for registering on our website.',
            #           settings.EMAIL_HOST_USER, [Em, ])
            return redirect(Faculty_Page)
        else:
            Err = 'The Passwords Does not match.'
            return render(request, 'App1/register.html', {'ERROR1': Err})
    else:
        return render(request, 'App1/register.html')


@never_cache
def activate1(request, uid64, token):
    User = get_user_model()

    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user1 = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user1 = None
    if user1 is not None and account_activation_token.check_token(user1, token):
        user1.is_active = True
        user1.save()
        return redirect(login)
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('The Activation Link Is Expired')


@never_cache
def otpVerify(request, id):
    if request.method == "POST":
        vb = user.objects.get(id=id)
        if request.COOKIES.get('abc') is not None:
            if vb.otp == request.POST['otp']:
                return redirect(login)
            else:
                Err = 'Invalid otp !!'
                return render(request, 'otp.html', context={'err': Err})
        else:
            Err = 'You Have Reached The Time Limit !!'
            return render(request, 'register.html', context={'err': Err})
    else:
        return render(request, 'otp.html', {'id': id})


@never_cache
def login12(request):
    if request.method == 'POST':
        Username = request.POST['uname']
        password = request.POST['pwd']

        try:
            record = user.objects.get(uname=Username)

            if check_password(password, record.password):
                return redirect(Faculty_Page)
            else:
                Err = 'Password Does Not Match'
                return render(request, 'login.html', context={'Error': Err})

        except user.DoesNotExist:
            Err = 'Username Does Not Exist'
            return render(request, 'login.html', context={'Error': Err})

    else:
        return render(request, 'login.html')


@never_cache
def logout1(request):
    logout(request)
    return render(request, 'logout.html', )


@never_cache
def about(request):
    return render(request, 'about.html')


@never_cache
def student(request):
    User = Student.objects.all().count()
    records = Student.objects.all()
    SW = Student.objects.filter(course='Application Developer').count()
    SDD = Student.objects.filter(course='Software Developer').count()
    STD = Student.objects.filter(course='Website Design').count()
    # print(no)
    # print(record)
    return render(request, 'student.html', context={'std': records, 'Users': User, 'sv': SW, 'XYZ': SDD, 'ABC': STD})


@never_cache
def contactus(request):
    if request.method == 'POST':
        name = request.POST['Nm']
        Email = request.POST['Em']
        PH = request.POST['Ph']
        Message = request.POST['Ms']
        u3 = Cont(Name=name, Email=Email, PH=PH, Message=Message)
        u3.save()
        return redirect(homefn)
    else:
        return render(request, 'contactus.html')


@never_cache
def student2(request):
    if request.method == 'POST':
        role = request.POST.get('Role')

        if role == 'Student':
            fn = request.POST['fn']
            ln = request.POST['ln']
            un = request.POST['un']
            DOBi = request.POST['dob']
            Gen = request.POST['gen']
            Em = request.POST['Em']
            Phone = request.POST['Ph']
            course = request.POST['Dv']
            Role1 = request.POST['Role']
            u2 = Student(fname=fn, lname=ln, userno=un, dob=DOBi, Gender=Gen, Email=Em, Number=Phone,
                         course=course, Category=Role1)
            u2.save()
            return redirect(Faculty_Page)

        elif role == 'Faculty':
            fn = request.POST['fn']
            ln = request.POST['ln']
            un = request.POST['un']
            DOBi = request.POST['dob']
            Gen = request.POST['gen']
            Em = request.POST['Em']
            Phone = request.POST['Ph']
            course = request.POST['Dv']
            department = request.POST['Role']
            faculty = Faculty(fname=fn, lname=ln, userno=un, dob=DOBi, Gender=Gen, Email=Em, Number=Phone,
                              Category=department, course=course)
            faculty.save()

            return redirect(Faculty_Page)

    return render(request, 'student2.html')


@never_cache
def dashboard(request):
    return render(request, 'Dashboard.html')


@never_cache
def courses(request):
    return render(request, 'course.html')


@never_cache
def editUser(request, id):
    std1 = Student.objects.get(sid=id)
    if request.method == 'POST':
        fno = request.POST['fn']
        lno = request.POST['ln']
        DOBio = request.POST['dob']
        uno = request.POST['un']
        Geno = request.POST['Gen']
        Emo = request.POST['Em']
        Phoneo = request.POST['Ph']
        courseo = request.POST['Dv']
        std1.fname = fno
        std1.lname = lno
        std1.userno = uno
        std1.dob = DOBio
        std1.Gender = Geno
        std1.Email = Emo
        std1.Number = Phoneo
        std1.course = courseo
        std1.save()
        return redirect(axx)

    else:
        # print(std1.username)
        return render(request, 'editstd.html', context={'Std': std1})


@never_cache
def delete_std(request, id):
    std1 = Student.objects.get(sid=id)
    std1.delete()
    return render(request, 'App3/ad_edit.html')


@never_cache
def viewstd(request, id):
    std5 = Student.objects.get(sid=id)
    return render(request, 'view_std.html', context={'std6': std5})


@never_cache
def allinuser(request):
    vb = user.objects.all().count()
    records = user.objects.all()
    return render(request, 'alluser.html', context={'stud': records, 'Userss': vb})


@never_cache
def train(request):
    return render(request, 'traning.html')


@never_cache
def alp(request):
    return render(request, 'tr_alp.html')


@never_cache
def pro1(request):
    product = Add_product.objects.all()
    return render(request, 'product.html', context={'product': product})


@never_cache
def cate(request):
    return render(request, 'tr_cate.html')


@never_cache
def add_new(request, id):
    p = Add_product.objects.get(id=id)
    return render(request, 'Add_new.html', context={'p': p})


@never_cache
def axx(request):
    User3 = Student.objects.all().count()
    records = Student.objects.all()
    SW = Student.objects.filter(course='Application Developer').count()
    SDD = Student.objects.filter(course='Software Developer').count()
    STD = Student.objects.filter(course='Website Design').count()
    vb = user.objects.all().count()
    recordsn = user.objects.all()
    Faculty1 = Faculty.objects.all()
    Faculty12 = Faculty.objects.all().count()
    # print(no)
    # print(record)
    return render(request, 'admin.html',
                  context={'std': records, 'Users1': User3, 'sv': SW, 'XYZ': SDD, 'ABC': STD, 'all': vb,
                           'ann': recordsn, 'Faculty': Faculty1, 'FacultyAs': Faculty12})


@never_cache
# def back(request):
#     cp = Captcha(request.POST)
#     if request.method == 'POST':
#         username = request.POST['Em']
#         password = request.POST['Pw']
#
#         try:
#             records = user.objects.get(email=username)
#             print(records.password)
#             if records.password == password:
#                 if cp.is_valid():
#                     if username == 'dilipkarmakar1978@gmail.com':
#                         return redirect(axx)
#                     else:
#                         return render(request, 'home.html')
#                 else:
#                     Err = 'Invalid Captcha Code !! '
#                     return render(request, 'admin2.html', context={'Error': Err})
#             else:
#                 Err = 'Invalid Password !!'
#                 return render(request, 'admin2.html', context={'Error': Err})
#         except:
#             Err = 'You Are Not A Administer !! '
#             return render(request, 'admin2.html', context={'Error': Err})
#     else:
#         return render(request, 'admin2.html')


@never_cache
def ad_edit(request):
    User = Student.objects.all().count()
    records = Student.objects.all()
    SW = Student.objects.filter(course='Application Developer').count()
    SDD = Student.objects.filter(course='Software Developer').count()
    STD = Student.objects.filter(course='Website Design').count()

    return render(request, 'ad_edit.html', context={'std': records, 'Users': User, 'sv': SW, 'XYZ': SDD, 'ABC': STD})


@never_cache
def ad_alluser(request):
    if request.method == 'POST':
        if 'subvu' in request.POST:
            Name = request.POST['Name']
            New_price = request.POST['new']
            Old_price = request.POST['old']
            Pr_photo = request.FILES['photo']
            Des = request.POST['des']
            p1 = Add_product(Name=Name, New_price=New_price, Old_price=Old_price, Photo=Pr_photo, Dec=Des)
            p1.save()

            return redirect(pro1)
        elif 'subject2' in request.POST:
            Name = request.POST['Name']
            home_price = request.POST['new']
            home_image = request.FILES['photo']
            h6_head = request.POST['old']
            down_heading = request.POST['des']
            p12 = home_add(main_name=Name, home_price=home_price, home_image=home_image, h6_head=h6_head,
                           down_heading=down_heading)
            p12.save()
            return redirect(homefn)
    else:
        return render(request, 'ad_alluser.html')


@never_cache
def message(request):
    return redirect(message)


@never_cache
def rev(request):
    User3 = Student.objects.all().count()
    records = Student.objects.all()
    SW = Student.objects.filter(course='Application Developer').count()
    SDD = Student.objects.filter(course='Software Developer').count()
    STD = Student.objects.filter(course='Website Design').count()
    recordsn = user.objects.all()

    return render(request, 'rev.html',
                  context={'user': User3, 'rec': records, 'sw': SW, 'SDD': SDD, 'STD': STD, 'reco': recordsn})


@never_cache
def payment(request):
    if request.method == 'POST':
        Card_Number = request.POST['Num']
        Expiry = request.POST['date']
        Cvv = request.POST['Cvv']
        Card_Name = request.POST['Name']
        payment1 = Payment(Card_Number=Card_Number, Expiry=Expiry, Cvv=Cvv, Card_Name=Card_Name)
        payment1.save()
        return redirect(homefn)
    else:
        return render(request, 'payment.html')


@never_cache
def products(request):
    productsv = Add_product.objects.all().count()
    all_product = Add_product.objects.all()
    return render(request, 'product_admin.html', context={'prod': productsv, 'all_prod': all_product})


@never_cache
def my_view1(request):
    cp = Captcha(request.POST)
    if request.method == 'POST':
        username = request.POST['Em']
        password = request.POST['Pw']

        try:

            records = user.objects.get(uname=username)
            print(records.password)
            if records.password == password:
                if cp.is_valid():
                    return render(request, 'home.html')
                else:
                    Err = 'Invalid Captcha Code !! '
                    return render(request, 'error.html', context={'Error': Err, 'cap': cp})
            else:
                Err = 'Invalid Password !!'
                return render(request, 'error.html', context={'Error': Err, 'cap': cp})
        except:
            Err = 'user Does Not Existed !! '
            return render(request, 'error.html', context={'Error': Err, 'cap': cp})
    else:
        return render(request, 'error.html', context={'cap': cp})


@never_cache
def Forget_pass(request, id):
    if request.method == 'POST' and 'Email_frg' in request.POST:
        email = request.POST.get('Email_frg', '')

        user_record = user.objects.filter(email=email).count()
        if user_record == 1:
            user_record = user.objects.get(email=email)
            id = user_record.id
            email_otp = random.randint(100000, 999999)
            request.session['otp'] = email_otp
            send_mail(
                'Forget Password',
                f'Your one time password is {email_otp}',
                settings.EMAIL_HOST_USER,
                [email, ]
            )

            # Set a cookie to track OTP existence
            red = redirect(f'/App1/Otp_red/{id}/')
            red.set_cookie('Otp1', True, max_age=600)
            return red

        else:
            return render(request, 'Forget_pass.html', context={'id': id, 'Err': 'Email Not Registered!'})
    else:
        return render(request, 'Forget_pass.html', context={'id': id})


@never_cache
def Otp_red(request, id):
    if request.method == 'POST':
        if 'Otp1' in request.POST and request.POST['Otp1'] != '':
            if request.COOKIES.get('Otp1'):
                print('cookie get')
                if 'pw1' in request.POST and 'pw2' in request.POST:
                    pw1 = request.POST['pw1']
                    pw2 = request.POST['pw2']
                    Otp_Sms = int(request.session.get('otp'))

                    if Otp_Sms == int(request.POST['Otp1']):
                        if pw1 and pw2:
                            if pw1 == pw2:
                                try:
                                    user_record = user.objects.get(id=id)
                                    current_password = user_record.password

                                    if not check_password(pw1, current_password):
                                        user_record.password = make_password(pw1)
                                        user_record.save()
                                        return redirect(Faculty_Page)
                                    else:
                                        err = "You cannot use the old password!"
                                        return render(request, 'Otp_red.html', {'err': err, 'id': id})

                                except user.DoesNotExist:
                                    return HttpResponse('User ID does not exist')

                            else:
                                err = "Both passwords must be the same!"
                                return render(request, 'Otp_red.html', {'err': err, 'id': id})
                        else:
                            Err4 = 'Password Fields Cannot Be Empty'
                            return render(request, 'Otp_red.html', context={'Error4': Err4})
                    else:
                        Err = 'Yor Have Entered The Otp Is Wrong !!'
                        return render(request, 'Otp_red.html', context={'Error': Err})
                else:
                    Err1 = 'SomeThing Went Wrong !!'
                    return render(request, 'Otp_red.html', context={'Error1': Err1})
            else:
                Err2 = 'Your Cookie HAs Been Expire !! Retry Again Please !!'
                return render(request, 'Otp_red.html', context={'Error2': Err2})
        else:
            Err3 = 'Your Request Cant Be Proceed !!'
            return render(request, 'Otp_red.html', context={'Error3': Err3})
    else:
        return render(request, 'Otp_red.html', {'id': id})


#
#
# def payment_process(request):
#     try:
#         configure({
#             "mode": 'live',  # Change to 'live' for production
#             "client_id": 'Ae1CDbr6uS1Br1klRUpV0uGT-2k4Su_tPh2cIBoKcHQFf7vhkjGnPa_r86nOMJ2Bl-7GksJhWkq6wX9u',
#             "client_secret": 'EJj4_2OMEvdk9mbKo4MOTSxCMpXGzjYJWfOMtny_AN5arrKgUpPYUTeT4-P006UjPMiey2DMfVTYjvl5'
#         })
#
#         payment_data = {
#             "intent": "sale",
#             "payer": {
#                 "payment_method": "paypal"
#             },
#             "redirect_urls": {
#                 "return_url": "http://127.0.0.1:8000/return/",  # Replace with your actual return URL
#                 "cancel_url": "http://127.0.0.1:8000/cancel/"  # Replace with your actual cancel URL
#             },
#             "transactions": [{
#                 "amount": {
#                     "total": "1000.00",
#                     "currency": "INR"
#                 },
#                 "description": "Pay With PayPal"
#             }]
#         }
#
#         paypal_payment = Payment(payment_data)
#
#         if paypal_payment.create():
#             print('er')
#             for link in paypal_payment.links:
#                 if link.method == 'REDIRECT':
#                     redirect_url = str(link.href)
#                     return redirect(redirect_url)
#             return HttpResponse('No redirect URL found.')
#         else:
#             logger.error(paypal_payment.error)
#             return HttpResponse('Failed to create PayPal payment.')
#
#     except Exception as e:
#         logger.error(f"Error processing PayPal payment: {str(e)}")
#         return HttpResponse('Error processing PayPal payment.')
#
#
# logger = logging.getLogger(__name__)
#
#
# class paypalFormView(FormView):
#     template_name = 'product.html'
#     form_class = PayPalPaymentsForm
#
#     def get_initial(self):
#         return {
#             'business': settings.PAYPAL_RECEIVER_EMAIL,
#             'amount': 20,
#             'currency_code': 'EUR',
#             'item_name': 'Example item',
#             'invoice': 1234,
#             'notify_url': self.request.build_absolute_uri(reverse('paypal-ipn')),
#             'return_url': self.request.build_absolute_uri(reverse('paypal-return')),
#             'cancel_return': self.request.build_absolute_uri(reverse('paypal-cancel')),
#             'lc': 'EN',
#             'no_shipping': '1',
#         }
#
#
# @receiver(valid_ipn_received)
# def paypal_payment_received(sender, **kwargs):
#     ipn_obj = sender
#
#     if ipn_obj.payment_status == 'Completed':
#         if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
#             # Not a valid payment
#             return
#
#         try:
#             my_pk = ipn_obj.invoice
#             mytransaction = MyTransaction.objects.get(pk=my_pk)
#             assert ipn_obj.mc_gross == mytransaction.amount and ipn_obj.mc_currency == 'EUR'
#
#         except ObjectDoesNotExist:
#             logger.error('MyTransaction with pk={} does not exist'.format(my_pk))
#         except AssertionError:
#             logger.error('IPN data does not match transaction data')
#         except Exception as e:
#             logger.exception('Error processing PayPal IPN: {}'.format(e))
#         else:
#             mytransaction.paid = True
#             mytransaction.save()
#             logger.info('Transaction marked as paid: {}'.format(mytransaction))
#     else:
#         logger.debug('Paypal payment status not completed: %s' % ipn_obj.payment_status)



