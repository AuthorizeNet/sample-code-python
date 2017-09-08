import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')

def update_customer_profile(customerProfileId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    updateCustomerProfile = apicontractsv1.updateCustomerProfileRequest()
    updateCustomerProfile.merchantAuthentication = merchantAuth
    updateCustomerProfile.profile = apicontractsv1.customerProfileExType()

    updateCustomerProfile.profile.customerProfileId = customerProfileId
    updateCustomerProfile.profile.merchantCustomerId = "mycustomer"
    updateCustomerProfile.profile.description = "john doe"
    updateCustomerProfile.profile.email = "email@email.com"

    controller = updateCustomerProfileController(updateCustomerProfile)
    controller.execute()

    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print ("Successfully updated customer with customer profile id %s" % updateCustomerProfile.profile.customerProfileId)
    else:
        print (response.messages.message[0]['text'].text)
        print ("Failed to update customer profile with customer profile id %s" % updateCustomerProfile.profile.customerProfileId)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    update_customer_profile(constants.customerProfileId)
