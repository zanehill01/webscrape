from twilio.rest import Client
import keys

client = Client(keys.accountsid, keys.auth_token)

TwilioNumber = "+18775254432"

mycellphone = "+15127881279"

textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber, body="hey There!")


print(textmessage.status)

call = client.calls.create(url= "https://demo/twilio.com/docs/voice.xml", to=mycellphone,from_=TwilioNumber)