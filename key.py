from twilio.rest import Client

account_sid = 'Your Sid'
auth_token = 'Your Token'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+91xxxxxxxxxx'
)

print(message.sid)

