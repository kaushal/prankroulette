# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from twilio import twiml
import string
import random


# Get these credentials from http://twilio.com/user/account
account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)
room_number = 0;

def setUpCall(numbers):
	if len(numbers) < 2:
		print "error: not enough numbers for conference"
		return 
	global room_number
	global client
	room = "pr"
	room = room + str(room_number)
	room_number += 1
	for num in numbers: 
		call = client.calls.create(to=num,
					from_="+14159686840",
					url="http://twimlets.com/conference?Name=" + room + "&Message=%20")
	return call

#nums = ["+19085287844", "+16107616189", "+17326681916", "+17324850325"]
# resources = client.calls.list()

