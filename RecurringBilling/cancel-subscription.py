import os, sys
from importlib.machinery import SourceFileLoader

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = SourceFileLoader('modulename', 'constants.py').load_module()

def cancel_subscription(subscriptionId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    request = apicontractsv1.ARBCancelSubscriptionRequest()
    request.merchantAuthentication = merchantAuth
    request.refId = "Sample"
    request.subscriptionId = subscriptionId

    controller = ARBCancelSubscriptionController(request)
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
    cancel_subscription(constants.subscriptionId)
