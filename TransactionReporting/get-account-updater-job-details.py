import os
import sys
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import getAUJobDetailsController
from authorizenet.constants import constants

def get_account_updater_job_details():
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    paging = apicontractsv1.Paging()
    # Paging limit can be up to 1000 for this request
    paging.limit = 1000
    paging.offset = 2
    request = apicontractsv1.getAUJobDetailsRequest()
    request.merchantAuthentication = merchantAuth
    request.paging = paging
    request.month = "2018-08"
    request.modifiedTypeFilter = "all"
    request.refId = "123456"
    controller = getAUJobDetailsController(request)
    controller.execute()
    response = controller.getresponse()

    if response is not None:
        if response.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:

                if hasattr(response, 'auDetails'):
                    print('SUCCESS: Get Account Updater job details for Month :' + request.month)
                    if response.messages is not None:
                        print('Message Code: %s' % response.messages.message[0]['code'].text)
                        print('Message Text: %s' % response.messages.message[0]['text'].text)
                        print('Total Number In Results: %s' % response.totalNumInResultSet)
                        print('\n')

                        for details in response.auDetails.auDelete:
                            print('Deleted Profile:')
                            # auDelete Start
							print('Customer Profile ID: %s' % details.customerProfileID)
                            print('Customer Payment Profile ID: %s' % details.customerPaymentProfileID)                            
                            print('First Name: %s' % details.firstName)
                            print('Last Name: %s' % details.lastName)
                            print('AU Reason Code: %s' % details.auReasonCode)
                            print('Reason Description: %s' % details.reasonDescription)
                            print('Update Time UTC: %s' % details.updateTimeUTC)
                            print(' ')
                            # fetching card details:
                            print('Card Details:')
                            print('Card Number: %s' % details.creditCard.cardNumber)
                            print('Card Type: %s' % details.creditCard.cardType)
                            print('Expiration Date: %s' % details.creditCard.expirationDate)                            
                            # auDelete End
                        print('\n')

                        for details in response.auDetails.auUpdate:

                                # auUpdate Start
                                print('Updated Profile:')
								print('Customer Profile ID: %s' % details.customerProfileID)
                                print('Customer Payment Profile ID: %s' % details.customerPaymentProfileID)                                
                                print('First Name: %s' % details.firstName)
                                print('Last Name: %s' % details.lastName)
                                print('AU Reason Code: %s' % details.auReasonCode)
                                print('Reason Description: %s' % details.reasonDescription)
                                print('Update Time UTC: %s' % details.updateTimeUTC)
                                # fetching Old card details:
                                print('Old Card details:')
                                print('old Card Number: %s' % details.oldCreditCard.cardNumber)
                                print('old Card Type: %s' % details.oldCreditCard.cardType)
                                print('old Expiration Date: %s' % details.oldCreditCard.expirationDate)
                                # fetching New  card details:
                                print('Old Card details:')
                                print('new Card Number: %s' % details.newCreditCard.cardNumber)
                                print('new Card Type: %s' % details.newCreditCard.cardType)
                                print('new Expiration Date: %s' % details.newCreditCard.expirationDate)                                

                else:
                        print('Failed to get Get Account Updater job details for Month :' + request.month)
                        print('Message Code: %s' % response.messages.message[0]['code'].text)
                        print('Message Text: %s' % response.messages.message[0]['text'].text)

        else:
                print('Failed to get Get Account Updater job details for Month :' + request.month)
                print('Message Code: %s' % response.messages.message[0]['code'].text)
                print('Message Text: %s' % response.messages.message[0]['text'].text)
    else:
        print('No response received')


if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_account_updater_job_details()

