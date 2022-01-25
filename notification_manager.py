from twilio.rest import Client

TWILIO_SID = 'ACea4f3179da9ddc4ccb022dc748442613'
TWILIO_AUTH_TOKEN = 'aa729c74a16037e6f777b072922dcc83'
TWILIO_VIRTUAL_NUMBER = "+16072845347"
TWILIO_VERIFIED_NUMBER = "+923022217482"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+16072845347",
            to="+923022217482",
        )
        # Prints if successfully sent.
        print(message.sid)
