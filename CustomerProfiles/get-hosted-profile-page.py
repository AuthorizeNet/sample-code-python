from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

setting = apicontractsv1.settingType()
setting.settingName = apicontractsv1.settingNameEnum.hostedProfileReturnUrl
setting.settingValue = "https://returnurl.com/return/"

settings = apicontractsv1.ArrayOfSetting()
settings.setting.append(setting)

profilePageRequest = apicontractsv1.getHostedProfilePageRequest()
profilePageRequest.merchantAuthentication = merchantAuth
profilePageRequest.customerProfileId = "36152116"
profilePageRequest.hostedProfileSettings = settings

profilePageController = getHostedProfilePageController(profilePageRequest)

profilePageController.execute()

profilePageResponse = profilePageController.getresponse()

if profilePageResponse is not None:
	if profilePageResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
		print('Successfully got hosted profile page!')

		print('Token : %s' % profilePageResponse.token)

		if profilePageResponse.messages:
			print('Message Code : %s' % profilePageResponse.messages.message[0].code)
			print('Message Text : %s' % profilePageResponse.messages.message[0].text)
	else:
		if profilePageResponse.messages:
			print('Failed to get batch statistics.\nCode:%s \nText:%s' % (profilePageResponse.messages.message[0].code,profilePageResponse.messages.message[0].text))
