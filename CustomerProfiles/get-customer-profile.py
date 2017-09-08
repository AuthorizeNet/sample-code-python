import os, sys
import imp
 
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
 
def get_customer_profile(customerProfileId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey
 
    getCustomerProfile = apicontractsv1.getCustomerProfileRequest()
    getCustomerProfile.merchantAuthentication = merchantAuth
    getCustomerProfile.customerProfileId = customerProfileId
    controller = getCustomerProfileController(getCustomerProfile)
    controller.execute()
 
    response = controller.getresponse()
 
    if (response.messages.resultCode=="Ok"):
        print "Successfully retrieved a customer with profile id %s and customer id %s" % (getCustomerProfile.customerProfileId, response.profile.merchantCustomerId)
        if hasattr(response, 'profile') == True:
            if hasattr(response.profile, 'paymentProfiles') == True:
                for paymentProfile in response.profile.paymentProfiles:
                     print ("paymentProfile in get_customerprofile is:" %paymentProfile)
                     print ("Payment Profile ID %s" % str(paymentProfile.customerPaymentProfileId))
             if hasattr(response.profile, 'shipToList') == True:
                 for ship in response.profile.shipToList:
                     print ("Shipping Details:")
                     print ("First Name %s" % ship.firstName)
                     print ("Last Name %s" % ship.lastName)
                     print ("Address %s" % ship.address
                     print ("Customer Address ID %s" % ship.customerAddressId)
        if hasattr(response, 'subscriptionIds') == True:
            if hasattr(response.subscriptionIds, 'subscriptionId') == True:
                print ("list of subscriptionid:")
                 for subscriptionid in (response.subscriptionIds.subscriptionId):
                    print (subscriptionid)
    else:
        print ("response code: %s" % response.messages.resultCode)
        print ("Failed to get customer profile information with id %s" % getCustomerProfile.customerProfileId)
 
    return response
 
if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_customer_profile(constants.customerProfileId)