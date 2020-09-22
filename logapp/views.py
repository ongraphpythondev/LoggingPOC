import sys
import datetime

from django.core.mail import send_mail
from LoggingPOC import settings
from django.shortcuts import render

# Create your views here.
# import the logging library
import logging
from django.http import HttpResponse


# Get an instance of a logger
logger = logging.getLogger(__name__)

def Test(request):
    try:
        # import pdb;
        # pdb.set_trace()
        print('Hello')
        c='a'/10
    except Exception as e:

        exc_type, exc_value, exc_traceback = sys.exc_info()
        logger.error(exc_type)
        sendSimpleMail("Internal Error", 'exc_type',settings.EMAIL_HOST_USER,'durgesh.ccts@gmail.com')
        traceback_details = {
            'file_name': exc_traceback.tb_frame.f_code.co_filename,
            'line_no': exc_traceback.tb_lineno,
            'name': exc_traceback.tb_frame.f_code.co_name,
            'type': exc_type.__name__,
            'message': str(e),  # or see traceback._some_str()
            'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    return HttpResponse('In Test')



def sendSimpleMail(subject,msg,emailfrom,emailto):
    send_mail(subject,msg, emailfrom, [emailto],fail_silently = False)
