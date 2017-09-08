import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def get_accept_customer_profile_page(customerProfileId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    setting = apicontractsv1.settingType()
    setting.settingName = apicontractsv1.settingNameEnum.hostedProfileReturnUrl
    setting.settingValue = "https://returnurl.com/return/"

    settings = apicontractsv1.ArrayOfSetting()
    settings.setting.append(setting)

    profilePageRequest = apicontractsv1.getHostedProfilePageRequest()
    profilePageRequest.merchantAuthentication = merchantAuth
    profilePageRequest.customerProfileId = customerProfileId
    profilePageRequest.hostedProfileSettings = settings

    profilePageController = getHostedProfilePageController(profilePageRequest)

    profilePageController.execute()

    profilePageResponse = profilePageController.getresponse()

    if profilePageResponse is not None:
        if profilePageResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
            print('Successfully got hosted profile page!')

            print('Token : %s' % profilePageResponse.token)

            if profilePageResponse.messages:
                print('Message Code : %s' % profilePageResponse.messages.message[0]['code'].text)
                print('Message Text : %s' % profilePageResponse.messages.message[0]['text'].text)
        else:
            if profilePageResponse.messages:
                print('Failed to get batch statistics.\nCode:%s \nText:%s' % (profilePageResponse.messages.message[0]['code'].text,profilePageResponse.messages.message[0]['text'].text))

    return profilePageResponse

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_hosted_profile_page(constants.customerProfileId)
