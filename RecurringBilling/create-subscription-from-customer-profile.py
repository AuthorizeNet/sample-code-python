import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *
from datetime import *

def create_subscription_from_customer_profile(amount, days, profileId, paymentProfileId, customerAddressId):

    # Setting the merchant details
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey
    # Setting payment schedule
    paymentschedule = apicontractsv1.paymentScheduleType()
    paymentschedule.interval = apicontractsv1.paymentScheduleTypeInterval() #apicontractsv1.CTD_ANON() #modified by krgupta
    paymentschedule.interval.length = days
    paymentschedule.interval.unit = apicontractsv1.ARBSubscriptionUnitEnum.days
    paymentschedule.startDate = datetime(2021, 12, 30)
    paymentschedule.totalOccurrences = 12
    paymentschedule.trialOccurrences = 1

    #setting the customer profile details
    profile = apicontractsv1.customerProfileIdType()
    profile.customerProfileId = profileId
    profile.customerPaymentProfileId = paymentProfileId
    profile.customerAddressId = customerAddressId

    # Setting subscription details
    subscription = apicontractsv1.ARBSubscriptionType()
    subscription.name = "Sample Subscription"
    subscription.paymentSchedule = paymentschedule
    subscription.amount = amount
    subscription.trialAmount = Decimal('0.00')
    subscription.profile = profile

    # Creating the request
    request = apicontractsv1.ARBCreateSubscriptionRequest()
    request.merchantAuthentication = merchantAuth
    request.subscription = subscription

    # Creating and executing the controller
    controller = ARBCreateSubscriptionController(request)
    controller.execute()
    # Getting the response
    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print ("SUCCESS:")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % response.messages.message[0]['text'].text)
        print ("Subscription ID : %s" % response.subscriptionId)
    else:
        print ("ERROR:")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % response.messages.message[0]['text'].text)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    create_subscription_from_customer_profile(constants.amount, constants.days, "247150", "215472", "189691")
