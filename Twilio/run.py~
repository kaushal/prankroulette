from flask import Flask, render_template, request
from twilio.util import TwilioCapability
import twilio.twiml

app = Flask(__name__)

 # Add a Twilio phone number or number verified with Twilio as the caller ID
caller_id = "+14159686840"
default_client = "JohnCorndog"
 
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    from_number = request.values.get('PhoneNumber', None)
    resp = twilio.twiml.Response()
 
    # Nest <Client> TwiML inside of a <Dial> verb
    with resp.dial(callerId=caller_id) as r: 
	    if from_number and re.search('^[\d\(\)\- \+]+$', from_number):
		    r.number(from_number)
	    else:
		    r.client(default_client)

    return str(resp)

@app.route('/client', methods=['GET','POST'])
def client():
    """Respond to incoming requests."""
 
    account_sid = "AC566da319c49345fe4fbbbea81ada1de0"
    auth_token = "741080b04bcb6c2471cf9439d939abce"
 
    capability = TwilioCapability(account_sid, auth_token)

    # This is a special Quickstart application sid - or configure your own
    # at twilio.com/user/account/apps
    application_sid = "APabe7650f654fc34655fc81ae71caa3ff"
    capability.allow_client_outgoing(application_sid)
    capability.allow_client_incoming("JohnCorndog")
    token = capability.generate()
 
    return render_template('client.html', token=token)
 
if __name__ == "__main__":
    app.run(debug=True)
