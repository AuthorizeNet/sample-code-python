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
    paypal.payerID = "LM6NCLZ5RAKBY"

    payment = apicontractsv1.paymentType()
    payment.payPal = paypal

    transactionrequest = apicontractsv1.transactionRequestType()
    transactionrequest.transactionType = apicontractsv1.transactionTypeEnum.authOnlyContinueTransaction
    transactionrequest.refTransId = "2245592542"
    transactionrequest.payment = payment

    request = apicontractsv1.createTransactionRequest()
    request.merchantAuthentication = merchantAuth
    request.refId = "Sample"
    request.transactionRequest = transactionrequest

    controller = createTransactionController(request)
    controller.execute()

    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print "SUCCESS"
        print "Message Code : %s" % response.messages.message[0].code
        print "Message text : %s" % response.messages.message[0].text
        if (response.transactionResponse.responseCode == "1" ):
            print "Description : %s " % response.transactionResponse.messages.message[0].description
            print "Payer Id : %s " % response.transactionResponse.secureAcceptance.PayerID
            print "Transaction ID : %s " % response.transactionResponse.transId
    else:
        print "ERROR"
        print "Message Code : %s" % response.messages.message[0].code
        print "Message text : %s" % response.messages.message[0].text

    return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
    authorization_only_continued()