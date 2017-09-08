import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

constants = imp.load_source('modulename', 'constants.py')

def get_subscription_status(subscriptionId):
    # Setting the mercahnt details
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey
    # Seeting the request
    request = apicontractsv1.ARBGetSubscriptionStatusRequest()
    request.merchantAuthentication = merchantAuth
    request.refId = "Sample"
    request.subscriptionId = subscriptionId
    # Executing the controller
    controller = ARBGetSubscriptionStatusController(request)
    controller.execute()
    # Getting the response
    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print ("SUCCESS:")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % response.messages.message[0]['text'].text)
        print ("Subscription Status : %s" % response.status)
    else:
        print ("ERROR:")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % response.messages.message[0]['text'].text)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_subscription_status(constants.subscriptionId)
