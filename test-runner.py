import unittest
import sys
import imp
import random
from authorizenet import apicontractsv1

class TestRunner(unittest.TestCase):
	 
	def getEmail(self):
		return str(random.randint(0, 10000)) + "@test.com"

	def getAmount(self):
		return random.randint(0, 10000)
		
	def getDay(self):
		return random.randint(7, 365)

	def create_an_apple_pay_transaction(self):
		print("create_an_apple_pay_transaction")
		modl = imp.load_source('modulename', 'ApplePayTransactions/create-an-apple-pay-transaction.py')
		return modl.create_an_apple_pay_transaction()

	def create_customer_payment_profile(self):
		print("create_customer_payment_profile")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()

		#create customer payment profile for that above profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-payment-profile.py')
		response = modl.create_customer_payment_profile(response.customerProfileId)

		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(response.customerProfileId)

		return response

	def create_customer_profile_from_transaction(self):
		print("create_customer_profile_from_transaction")

		#Create transaction
		modl = imp.load_source('modulename', 'PaymentTransactions/authorize-credit-card.py')
		response = modl.authorize_credit_card()

		#create customer payment profile for above transaction
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile-from-transaction.py')
		response = modl.create_customer_profile_from_transaction(response.transactionResponse.transId)

		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(response.customerProfileId)

		return response

	def create_customer_profile(self):
		print("create_customer_profile")
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()

		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(response.customerProfileId)

		return response

	def create_customer_shipping_address(self):
		print("create_customer_shipping_address")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()

		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-shipping-address.py')
		response = modl.create_customer_shipping_address(response.customerProfileId)

		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(response.customerProfileId)

		return response

	def delete_customer_payment_profile(self):
		print("delete_customer_payment_profile")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()
		customerProfileId = response.customerProfileId
		
		#create customer payment profile for that above profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-payment-profile.py')
		response = modl.create_customer_payment_profile(response.customerProfileId)

		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-payment-profile.py')
		response = modl.delete_customer_payment_profile(customerProfileId, response.customerPaymentProfileId)

		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(customerProfileId)

		return response


	def delete_customer_profile(self):
		print("delete_customer_profile")

		#Create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()

		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		return modl.delete_customer_profile(response.customerProfileId)

	def delete_customer_shipping_address(self):
		print("delete_customer_shipping_address")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()
		customerProfileId = response.customerProfileId

		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-shipping-address.py')
		response = modl.create_customer_shipping_address(customerProfileId)

		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-shipping-address.py')
		response = modl.delete_customer_shipping_address(customerProfileId, response.customerAddressId)

		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(customerProfileId)

		return response

	def get_customer_payment_profile(self):
		print("get_customer_payment_profile")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()
		customerProfileId = response.customerProfileId
		
		#create customer payment profile for that above profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-payment-profile.py')
		response = modl.create_customer_payment_profile(customerProfileId)

		modl = imp.load_source('modulename', 'CustomerProfiles/get-customer-payment-profile.py')
		response = modl.get_customer_payment_profile(customerProfileId, response.customerPaymentProfileId)
		
		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(customerProfileId)

		return response


	def get_customer_profile_ids(self):
		print("get_customer_profile_ids")
		modl = imp.load_source('modulename', 'CustomerProfiles/get-customer-profile-ids.py')
		return modl.get_customer_profile_ids()

	def get_customer_profile(self):
		print("get_customer_profile")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()
		customerProfileId = response.customerProfileId

		modl = imp.load_source('modulename', 'CustomerProfiles/get-customer-profile.py')
		response = modl.get_customer_profile(customerProfileId)

		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(customerProfileId)

		return response

	def get_customer_shipping_address(self):
		print("get_customer_shipping_address")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()
		customerProfileId = response.customerProfileId

		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-shipping-address.py')
		response = modl.create_customer_shipping_address(customerProfileId)

		modl = imp.load_source('modulename', 'CustomerProfiles/get-customer-shipping-address.py')
		response = modl.get_customer_shipping_address(customerProfileId, response.customerAddressId)

		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(customerProfileId)

		return response

	def get_hosted_profile_page(self):
		print("get_hosted_profile_page")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()
		customerProfileId = response.customerProfileId

		modl = imp.load_source('modulename', 'CustomerProfiles/get-hosted-profile-page.py')
		response = modl.get_hosted_profile_page(customerProfileId)

		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(customerProfileId)

		return response

	def update_customer_payment_profile(self):
		print("update_customer_payment_profile")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()
		customerProfileId = response.customerProfileId
		
		#create customer payment profile for that above profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-payment-profile.py')
		response = modl.create_customer_payment_profile(customerProfileId)

		modl = imp.load_source('modulename', 'CustomerProfiles/update-customer-payment-profile.py')
		response = modl.update_customer_payment_profile(customerProfileId, response.customerPaymentProfileId)
		
		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(customerProfileId)

		return response

	def update_customer_profile(self):
		print("update_customer_profile")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()
		customerProfileId = response.customerProfileId
		
		modl = imp.load_source('modulename', 'CustomerProfiles/update-customer-profile.py')
		response = modl.update_customer_profile(customerProfileId)

		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(customerProfileId)

		return response
		
	def update_customer_shipping_address(self):
		print("update_customer_shipping_address")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()
		customerProfileId = response.customerProfileId

		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-shipping-address.py')
		response = modl.create_customer_shipping_address(customerProfileId)

		modl = imp.load_source('modulename', 'CustomerProfiles/update-customer-shipping-address.py')
		response = modl.update_customer_shipping_address(customerProfileId, response.customerAddressId)

		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(customerProfileId)

		return response


	def validate_customer_payment_profile(self):
		print("validate_customer_payment_profile")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()
		customerProfileId = response.customerProfileId
		
		#create customer payment profile for that above profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-payment-profile.py')
		response = modl.create_customer_payment_profile(customerProfileId)

		modl = imp.load_source('modulename', 'CustomerProfiles/validate-customer-payment-profile.py')
		response = modl.validate_customer_payment_profile(customerProfileId, response.customerPaymentProfileId)
		
		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(customerProfileId)

		return response	

	def authorize_credit_card(self):
		print("authorize_credit_card")
		modl = imp.load_source('modulename', 'PaymentTransactions/authorize-credit-card.py')
		return modl.authorize_credit_card()

	def capture_funds_authorized_through_another_channel(self):
		print("capture_funds_authorized_through_another_channel")
		modl = imp.load_source('modulename', 'PaymentTransactions/capture-funds-authorized-through-another-channel.py')
		return modl.capture_funds_authorized_through_another_channel()

	def capture_previously_authorized_amount(self):
		print("capture_previously_authorized_amount")
		modl = imp.load_source('modulename', 'PaymentTransactions/capture-previously-authorized-amount.py')
		return modl.capture_previously_authorized_amount()

	def charge_credit_card(self):
		print("charge_credit_card")
		modl = imp.load_source('modulename', 'PaymentTransactions/charge-credit-card.py')
		return modl.charge_credit_card(self.getAmount())

	def charge_customer_profile(self):
		print("charge_customer_profile")

		#create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-profile.py')
		response = modl.create_customer_profile()
		customerProfileId = response.customerProfileId
		
		#create customer payment profile for that above profile
		modl = imp.load_source('modulename', 'CustomerProfiles/create-customer-payment-profile.py')
		response = modl.create_customer_payment_profile(customerProfileId)

		modl = imp.load_source('modulename', 'PaymentTransactions/charge-customer-profile.py')
		response = modl.charge_customer_profile(customerProfileId, response.customerPaymentProfileId, self.getAmount())
		
		#delete newly create customer profile
		modl = imp.load_source('modulename', 'CustomerProfiles/delete-customer-profile.py')
		modl.delete_customer_profile(customerProfileId)

		return response

	def charge_tokenized_credit_card(self):
		print("charge_tokenized_credit_card")
		modl = imp.load_source('modulename', 'PaymentTransactions/charge-tokenized-credit-card.py')
		return modl.charge_tokenized_credit_card()

	def credit_bank_account(self):
		print("credit_bank_account")
		modl = imp.load_source('modulename', 'PaymentTransactions/credit-bank-account.py')
		return modl.credit_bank_account()

	def debit_bank_account(self):
		print("debit_bank_account")
		modl = imp.load_source('modulename', 'PaymentTransactions/debit-bank-account.py')
		return modl.debit_bank_account()

	def refund_transaction(self):
		print("refund_transaction")

		modl = imp.load_source('modulename', 'PaymentTransactions/authorize-credit-card.py')
		response = modl.authorize_credit_card()

		modl = imp.load_source('modulename', 'PaymentTransactions/refund-transaction.py')
		return modl.refund_transaction(response.transactionResponse.transId)

	def update_split_tender_group(self):
		print("update_split_tender_group")
		modl = imp.load_source('modulename', 'PaymentTransactions/update-split-tender-group.py')
		return modl.update_split_tender_group()

	def void_transaction(self):
		print("void_transaction")

		modl = imp.load_source('modulename', 'PaymentTransactions/authorize-credit-card.py')
		response = modl.authorize_credit_card()

		modl = imp.load_source('modulename', 'PaymentTransactions/void-transaction.py')
		return modl.void_transaction(response.transactionResponse.transId)

	def authorization_and_capture_continue(self):
		print("authorization_and_capture_continue")

		modl = imp.load_source('modulename', 'PaypalExpressCheckout/authorization-and-capture.py')
		response = modl.authorization_and_capture(self.getAmount())

		modl = imp.load_source('modulename', 'PaypalExpressCheckout/authorization-and-capture-continue.py')
		return modl.authorization_and_capture_continue(response.transactionResponse.transId, "6ZSCSYG33VP8Q")

	def authorization_and_capture(self):
		print("authorization_and_capture")
		modl = imp.load_source('modulename', 'PaypalExpressCheckout/authorization-and-capture.py')
		return modl.authorization_and_capture(self.getAmount())

	def authorization_only_continued(self):
		print("authorization_only_continued")
		modl = imp.load_source('modulename', 'PaypalExpressCheckout/authorization-only-continued.py')
		return modl.authorization_only_continued()

	def authorization_only(self):
		print("authorization_only")
		modl = imp.load_source('modulename', 'PaypalExpressCheckout/authorization-only.py')
		return modl.authorization_only()

	def credit(self):
		print("credit")
		modl = imp.load_source('modulename', 'PaypalExpressCheckout/credit.py')
		return modl.credit()

	def get_details(self):
		print("get_details")

		modl = imp.load_source('modulename', 'PaypalExpressCheckout/authorization-and-capture.py')
		response = modl.authorization_and_capture(self.getAmount())

		modl = imp.load_source('modulename', 'PaypalExpressCheckout/get-details.py')
		return modl.get_details(response.transactionResponse.transId)

	def prior_authorization_capture(self):
		print("prior_authorization_capture")

		modl = imp.load_source('modulename', 'PaypalExpressCheckout/authorization-and-capture.py')
		response = modl.authorization_and_capture(self.getAmount())

		modl = imp.load_source('modulename', 'PaypalExpressCheckout/prior-authorization-capture.py')
		return modl.prior_authorization_capture(response.transactionResponse.transId)

	def void(self):
		print("void")

		modl = imp.load_source('modulename', 'PaypalExpressCheckout/authorization-and-capture.py')
		response = modl.authorization_and_capture(self.getAmount())

		modl = imp.load_source('modulename', 'PaypalExpressCheckout/void.py')
		return modl.void(response.transactionResponse.transId)

	def cancel_subscription(self):
		print("cancel_subscription")

		modl = imp.load_source('modulename', 'RecurringBilling/create-subscription.py')
		response = modl.create_subscription(self.getAmount(), self.getDay())

		modl = imp.load_source('modulename', 'RecurringBilling/cancel-subscription.py')
		return modl.cancel_subscription(response.subscriptionId)

	def create_subscription(self):
		print("create_subscription")

		modl = imp.load_source('modulename', 'RecurringBilling/create-subscription.py')
		return modl.create_subscription(self.getAmount(), self.getDay())

	def get_list_of_subscription(self):
		print("get_list_of_subscription")

		modl = imp.load_source('modulename', 'RecurringBilling/get-list-of-subscription.py')
		return modl.get_list_of_subscription()

	def get_subscription_status(self):
		print("get_subscription_status")

		modl = imp.load_source('modulename', 'RecurringBilling/create-subscription.py')
		response = modl.create_subscription(self.getAmount(), self.getDay())
		subscriptionId = response.subscriptionId

		modl = imp.load_source('modulename', 'RecurringBilling/get-subscription-status.py')
		response = modl.get_subscription_status(subscriptionId)

		modl = imp.load_source('modulename', 'RecurringBilling/cancel-subscription.py')
		modl.cancel_subscription(subscriptionId)

		return response

	def get_subscription(self):
		print("get_subscription")

		modl = imp.load_source('modulename', 'RecurringBilling/create-subscription.py')
		response = modl.create_subscription(self.getAmount(), self.getDay())
		subscriptionId = response.subscriptionId

		modl = imp.load_source('modulename', 'RecurringBilling/get-subscription.py')
		response = modl.get_subscription(subscriptionId)

		modl = imp.load_source('modulename', 'RecurringBilling/cancel-subscription.py')
		modl.cancel_subscription(subscriptionId)

		return response	

	def update_subscription(self):
		print("update_subscription")

		modl = imp.load_source('modulename', 'RecurringBilling/create-subscription.py')
		response = modl.create_subscription(self.getAmount(), self.getDay())
		subscriptionId = response.subscriptionId

		modl = imp.load_source('modulename', 'RecurringBilling/update-subscription.py')
		response = modl.update_subscription(subscriptionId)

		modl = imp.load_source('modulename', 'RecurringBilling/cancel-subscription.py')
		modl.cancel_subscription(subscriptionId)

		return response

	def get_batch_statistics(self):
		print("get_batch_statistics")
		modl = imp.load_source('modulename', 'TransactionReporting/get-batch-statistics.py')
		return modl.get_batch_statistics()

	def get_settled_batch_list(self):
		print("get_settled_batch_list")
		modl = imp.load_source('modulename', 'TransactionReporting/get-settled-batch-list.py')
		return modl.get_settled_batch_list()

	def get_transaction_details(self):
		print("get_transaction_details")

		modl = imp.load_source('modulename', 'PaymentTransactions/authorize-credit-card.py')
		response = modl.authorize_credit_card()

		modl = imp.load_source('modulename', 'TransactionReporting/get-transaction-details.py')
		return modl.get_transaction_details(response.transactionResponse.transId)

	def get_transaction_list(self):
		print("get_transaction_list")
		modl = imp.load_source('modulename', 'TransactionReporting/get-transaction-list.py')
		return modl.get_transaction_list()

	def get_unsettled_transaction_list(self):
		print("get_unsettled_transaction_list")
		modl = imp.load_source('modulename', 'TransactionReporting/get-unsettled-transaction-list.py')
		return modl.get_unsettled_transaction_list()

	def create_visa_checkout_transaction(self):
		print("create_visa_checkout_transaction")
		modl = imp.load_source('modulename', 'VisaCheckout/create-visa-checkout-transaction.py')
		return modl.create_visa_checkout_transaction()

	def decrypt_visa_checkout_data(self):
		print("decrypt_visa_checkout_data")
		modl = imp.load_source('modulename', 'VisaCheckout/decrypt-visa-checkout-data.py')
		return modl.decrypt_visa_checkout_data()

	def validate_response(self, response):
		if(response is None):
			return False
			
		if (response.messages.resultCode != apicontractsv1.messageTypeEnum.Ok):
			return False

		return True
		
	def test_all_sample_codes(self):
		failed = []
		succeeded = [] 
		f = open('list_of_sample_codes.txt', 'r')
		for line in f:
			#print(line)
			items = line.split('\t')
			apiName = items[0]
			isDependent = items[1]
			shouldApiRun = items[2].rstrip()[0]		

			if(shouldApiRun == '0'):
				print("Not runnning the test : " + apiName)
			elif(shouldApiRun == '1'):
				#print("Running : " + apiName)
				response = getattr(self, apiName)()
				#if(self.validate_response(response)):
				#	succeeded.append(apiName)
				#else:
				#	failed.append(apiName)
				
				self.assertTrue(self.validate_response(response))

		#print("-------- Success ----------")
		#for line in succeeded:
		#	print(line)

		#print("-------- Failed ----------")
		#for line in failed:
		#	print(line)


	#def test_sample(self):
	#	self.assertTrue(self.get_customer_shipping_address())
		
unittest.main()