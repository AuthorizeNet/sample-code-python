import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def charge_tokenized_credit_card():
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    creditCard = apicontractsv1.creditCardType()
    creditCard.cardNumber = "4111111111111111"
    creditCard.expirationDate = "2035-12"
    # Set the token specific info
    creditCard.isPaymentToken = True
    creditCard.cryptogram = "EjRWeJASNFZ4kBI0VniQEjRWeJA="

    payment = apicontractsv1.paymentType()
    payment.creditCard = creditCard

    transactionrequest = apicontractsv1.transactionRequestType()
    transactionrequest.transactionType = "authCaptureTransaction"
    transactionrequest.amount = Decimal ('1.5')
    transactionrequest.payment = payment

    createtransactionrequest = apicontractsv1.createTransactionRequest()
    createtransactionrequest.merchantAuthentication = merchantAuth
    createtransactionrequest.refId = "MerchantID-0001"
    createtransactionrequest.transactionRequest = transactionrequest

    createtransactioncontroller = createTransactionController(createtransactionrequest)
    createtransactioncontroller.execute()

    response = createtransactioncontroller.getresponse()

    if response is not None:
        if response.messages.resultCode == "Ok":
            if hasattr(response.transactionResponse, 'messages') == True:
                print ('Successfully created transaction with Transaction ID: %s' % response.transactionResponse.transId)
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
    charge_tokenized_credit_card()
