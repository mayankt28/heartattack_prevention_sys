from channels import Group
# from .models import session
from channels.sessions import channel_session
from channels.auth import channel_session_user_from_http,http_session_user,channel_session_user
from .utils import generate_graph


global tmp 
tmp=[]



@channel_session_user_from_http
def ws_connect(message):
    # print(dir(message))

    # Add to reader group
    # Group(message.user.username).add(message.reply_channel)
    Group("chat").add(message.reply_channel)
    # # Accept the connection request
    print('\n\n connection request received ')
    message.reply_channel.send({"accept": True})

    print('websocket --->CONNECTED')

def ws_disconnect(message):
    # Remove from reader group on clean disconnect
    # Group("chat_room").discard(message.reply_channel)
    print('websocket --->DISCONNECTED')

def ws_receive(message): 
   
    # tmp = 'kunal'
    avg = 70
   
    text = message.content.get("text")[1:]
    # print(text)
    graph = 'fdf'
    if len(tmp)<10:
        tmp.append(int(text))
    else:
        add=0
        for i in tmp:
            add+=i
        tmp.clear()
        avg = add/10
    msg = ""

    if avg < 60:
        msg = "Low pulse rate"
        
    elif avg > 105:
       msg = "High pulse rate"
    else :
        pass
    Group('chat').send({"text":text , "bytes":'msg'})
     
  