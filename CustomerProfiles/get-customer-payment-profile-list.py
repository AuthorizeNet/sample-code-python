"""http://developer.authorize.net/api/reference/#customer-profiles-get-customer-payment-profile-list"""
import os
import sys
import imp
import time

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import getCustomerPaymentProfileListController
constants = imp.load_source('modulename', 'constants.py')


def get_customer_payment_profile_list():
    """Retrieve a list of customer payment profiles matching the specific search parameters"""

    # Create a merchantAuthenticationType object with authentication details
    # retrieved from the constants file
    merchant_auth = apicontractsv1.merchantAuthenticationType()
    merchant_auth.name = constants.apiLoginId
    merchant_auth.transactionKey = constants.transactionKey

    # Set the transaction's refId
    ref_id = "ref{}".format(int(time.time())*1000)

    # Set the paging (this particular API call will only return up to 10 results at a time)
    paging = apicontractsv1.Paging()
    paging.limit = 10
    paging.offset = 1

    # Set the sorting
    sorting = apicontractsv1.CustomerPaymentProfileSorting()
    sorting.orderBy = apicontractsv1.CustomerPaymentProfileOrderFieldEnum.id
    sorting.orderDescending = "false"

    # Set search parameters
    search = apicontractsv1.CustomerPaymentProfileSearchTypeEnum.cardsExpiringInMonth
    month = "2020-12"

    # Creating the request with the required parameters
    request = apicontractsv1.getCustomerPaymentProfileListRequest()
    request.merchantAuthentication = merchant_auth
    request.refId = ref_id
    request.paging = paging
    request.sorting = sorting
    request.searchType = search
    request.month = month

    controller = getCustomerPaymentProfileListController(request)
    controller.execute()

    response = controller.getresponse()

    if response is not None:
        if response.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
            print ("SUCCESS")
            print ("Total Num in Result Set: %s" % response.totalNumInResultSet)
            for profile in response.paymentProfiles.paymentProfile:
                print("Profile ID: %s" % profile.customerProfileId)
                print("Payment Profile ID: %s" % profile.customerPaymentProfileId)
                try:
                    print("Card: %s" % profile.payment.creditCard.cardNumber)
                except AttributeError:
                    print("Bank account: %s" % profile.payment.bankAccount.accountNumber)
                print()

        else:
            print ("ERROR")
            if response.messages is not None:
                print ("Result code: %s" % response.messages.resultCode)
                print ("Message code: %s" % response.messages.message[0]['code'].text)
                print ("Message text: %s" % response.messages.message[0]['text'].text)
    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_customer_payment_profile_list()
