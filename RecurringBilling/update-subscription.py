import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')

def update_subscription(subscriptionId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    creditcard = apicontractsv1.creditCardType()
    creditcard.cardNumber = "4111111111111111"
    creditcard.expirationDate = "2035-12"

    payment = apicontractsv1.paymentType()
    payment.creditCard = creditcard

    #set profile information
    profile = apicontractsv1.customerProfileIdType()
    profile.customerProfileId = "121212"
    profile.customerPaymentProfileId = "131313"
    profile.customerAddressId = "141414"

    subscription = apicontractsv1.ARBSubscriptionType()
    subscription.payment = payment
    #to update customer profile information
    #subscription.profile = profile

    request = apicontractsv1.ARBUpdateSubscriptionRequest()
    request.merchantAuthentication = merchantAuth
    request.refId = "Sample"
    request.subscriptionId = subscriptionId
    request.subscription = subscription

    controller = ARBUpdateSubscriptionController(request)
    controller.execute()

    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print ("SUCCESS")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % response.messages.message[0]['text'].text)
    else:
        print ("ERROR")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % response.messages.message[0]['text'].text)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    update_subscription(constants.subscriptionId)
