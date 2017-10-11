"""http://developer.authorize.net/api/reference/index.html#customer-profiles-get-customer-profile-ids"""
import os
import sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import getCustomerProfileIdsController
constants = imp.load_source('modulename', 'constants.py')

def get_customer_profile_ids():
    """get customer profile IDs"""
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    CustomerProfileIdsRequest = apicontractsv1.getCustomerProfileIdsRequest()
    CustomerProfileIdsRequest.merchantAuthentication = merchantAuth
    CustomerProfileIdsRequest.refId = "Sample"

    controller = getCustomerProfileIdsController(CustomerProfileIdsRequest)
    controller.execute()

    # Work on the response
    response = controller.getresponse()

    # if (response.messages.resultCode == "Ok"):
    #     print("Successfully retrieved customer ids:")
    #     for identity in response.ids.numericString:
    #         print(identity)
    # else:
    #     print("response code: %s" % response.messages.resultCode)



    if response is not None:
        if response.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
            if hasattr(response, 'ids'):
                if hasattr(response.ids, 'numericString'):
                    print('Successfully retrieved customer IDs.')
                    if response.messages is not None:
                        print('Message Code: %s' % response.messages.message[0]['code'].text)
                        print('Message Text: %s' % response.messages.message[0]['text'].text)
                        print('Total Number of IDs Returned in Results: %s'
                            % len(response.ids.numericString))
                        print()
                    # There's no paging options in this API request; the full list is returned every call.
                    # If the result set is going to be large, for this sample we'll break it down into smaller
                    # chunks so that we don't put 72,000 lines into a log file
                    print('First 20 results:')
                    for profileId in range(0,19):
                        print(response.ids.numericString[profileId])
            else:
                if response.messages is not None:
                    print('Failed to get list.')
                    print('Code: %s' % (response.messages.message[0]['code'].text))
                    print('Text: %s' % (response.messages.message[0]['text'].text))
        else:
            if response.messages is not None:
                print('Failed to get list.')
                print('Code: %s' % (response.messages.message[0]['code'].text))
                print('Text: %s' % (response.messages.message[0]['text'].text))
    else:
        print('Error. No response received.')

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_customer_profile_ids()
