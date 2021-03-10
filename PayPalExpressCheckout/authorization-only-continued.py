import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def authorization_only_continued():
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    paypal = apicontractsv1.payPalType()
    paypal.successUrl = "http://www.merchanteCommerceSite.com/Success/TC25262"
    paypal.cancelUrl = "http://www.merchanteCommerceSite.com/Success/TC25262"
    paypal.payerID = "586E72QHPGHXS"

    payment = apicontractsv1.paymentType()
    payment.payPal = paypal

    transactionrequest = apicontractsv1.transactionRequestType()
    transactionrequest.transactionType = apicontractsv1.transactionTypeEnum.authOnlyContinueTransaction
    transactionrequest.refTransId = "60158280211"
    transactionrequest.payment = payment

    request = apicontractsv1.createTransactionRequest()
    request.merchantAuthentication = merchantAuth
    request.refId = "Sample"
    request.transactionRequest = transactionrequest

    controller = createTransactionController(request)
    controller.execute()

    response = controller.getresponse()

    if response is not None:
        if response.messages.resultCode == "Ok":
            if hasattr(response.transactionResponse, 'messages') == True:
                print ('Successfully created transaction with Transaction ID: %s' % response.transactionResponse.transId)
                print ("Payer Id : %s " % response.transactionResponse.secureAcceptance.PayerID)
                print ('Transaction Response Code: %s' % response.transactionResponse.responseCode)
                print ('Message Code: %s' % response.transactionResponse.messages.message[0].code)
                print ('Description: %s' % response.transactionResponse.messages.message[0].description)
            else:
                print ('Failed Transaction.')
                if hasattr(response.transactionResponse, 'errors') == True:
                    print ('Error Code:  %s' % str(response.transactionResponse.errors.error[0].errorCode))
                    print ('Error message: %s' % response.transactionResponse.errors.error[0].errorText)
        else:
            print ('Failed Transaction.')
            if hasattr(response, 'transactionResponse') == True and hasattr(response.transactionResponse, 'errors') == True:
                print ('Error Code: %s' % str(response.transactionResponse.errors.error[0].errorCode))
                print ('Error message: %s' % response.transactionResponse.errors.error[0].errorText)
            else:
                print ('Error Code: %s' % response.messages.message[0]['code'].text)
                print ('Error message: %s' % response.messages.message[0]['text'].text)
    else:
        print ('Null Response.')

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    authorization_only_continued()
