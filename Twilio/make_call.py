# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from twilio import twiml

# Get these credentials from http://twilio.com/user/account
account_sid = "ACc195897e66e840711f5b11eee31a3291"
auth_token = "90d6976931640d6d43038f94f02e0d50"

client = TwilioRestClient(account_sid, auth_token)

nums = ["+19085287844", "+16107616189", "+17326681916", "+17324850325"]

for i in range(0,2): 
	# Make the call
	call = client.calls.create(to=nums[i],
				from_="+14159686840",
				url="http://twimlets.com/conference?Name=foo")


for i in range(2,4): 
	# Make the call
	call = client.calls.create(to=nums[i],
				from_="+14159686840",
				url="http://twimlets.com/conference?Name=foo2")
# resources = client.calls.list()

