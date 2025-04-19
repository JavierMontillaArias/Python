from twilio.rest import Client  

account_sid = '##################################'  

auth_token = '[AuthToken]'  

client = Client(account_sid, auth_token)  

message = client.messages.create( 
                                from_='+18312311142',  
                                body='HELLOOOOOOOOOO',
                                to='+01678046902' 
)  

print(message.sid) 
