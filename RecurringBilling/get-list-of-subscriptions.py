"""http://developer.authorize.net/api/reference/#recurring-billing-get-a-list-of-subscriptions"""
import os
import sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import ARBGetSubscriptionListController
constants = imp.load_source('modulename', 'constants.py')

def get_list_of_subscriptions():
    """get list of subscriptions"""
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    # set sorting parameters
    sorting = apicontractsv1.ARBGetSubscriptionListSorting()
    sorting.orderBy = apicontractsv1.ARBGetSubscriptionListOrderFieldEnum.id
    sorting.orderDescending = True

    # set paging and offset parameters
    paging = apicontractsv1.Paging()
    # Paging limit can be up to 1000 for this request
    paging.limit = 20
    paging.offset = 1

    request = apicontractsv1.ARBGetSubscriptionListRequest()
    request.merchantAuthentication = merchantAuth
    request.refId = "Sample"
    request.searchType = apicontractsv1.ARBGetSubscriptionListSearchTypeEnum.subscriptionInactive
    request.sorting = sorting
    request.paging = paging

    controller = ARBGetSubscriptionListController(request)
    controller.execute()

    # Work on the response
    response = controller.getresponse()

    if response is not None:
        if response.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
            if hasattr(response, 'subscriptionDetails'):
                print('Successfully retrieved subscription list.')
                if response.messages is not None:
                    print('Message Code: %s' % response.messages.message[0]['code'].text)
                    print('Message Text: %s' % response.messages.message[0]['text'].text)
                    print('Total Number In Results: %s' % response.totalNumInResultSet)
                    print()
                for subscription in response.subscriptionDetails.subscriptionDetail:
                    print('Subscription Id: %s' % subscription.id)
                    print('Subscription Name: %s' % subscription.name)
                    print('Subscription Status: %s' % subscription.status)
                    print('Customer Profile Id: %s' % subscription.customerProfileId)
                    print()
            else:
                if response.messages is not None:
                    print('Failed to get subscription list.')
                    print('Code: %s' % (response.messages.message[0]['code'].text))
                    print('Text: %s' % (response.messages.message[0]['text'].text))
        else:
            if response.messages is not None:
                print('Failed to get transaction list.')
                print('Code: %s' % (response.messages.message[0]['code'].text))
                print('Text: %s' % (response.messages.message[0]['text'].text))
    else:
        print('Error. No response received.')

    return response

if os.path.basename(__file__) == os.path.basename(sys.argv[0]):
    get_list_of_subscriptions()
