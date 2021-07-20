from browser import document, bind, ajax, html
import json

@bind('#chat-submit', 'click')
def send_message(event):
	csrf = document.cookie
	beg = csrf.find('=')
	csrf = csrf[beg+1:-1]
	message = document.select('.input_text')[0].value
	chat = document['chat-logs']
	chat <= html.DIV(message, style=dict(height='fit-content', float='right', background='#5a5eb9', color='#ffffff'), Class='cm-msg-text')
	req = ajax.ajax()
	req.open('POST', 'response-city/', True)
	req.set_header('content-type', 'application/x-www-form-urlencoded')
	req.send({'data': message, 'X-CSRFToken': csrf})
	req.bind('complete', complete)

def complete(request):
	chat=document['chat-logs']
	data = json.loads(request.responseText)
	answer = data['data']
	chat <= html.DIV(answer, style=dict(height='fit-content'), Class='cm-msg-text')
	document.select('.input_text')[0].value = ''