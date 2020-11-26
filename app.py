from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)
done = [1, 2, 10, 12, 13, 3, 4, 5, 6, 14, 34, 35, 36, 29, 23]
current = []

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/sms', methods=['POST'])
def reply():
    global done, current
 

    current.clear()
    msg = request.form.get('Body')
    if (msg.lower() == "ame"):
        i = 0
        while i < 5:
            questions = random.randint(1,38)

            if len(done) + len(current) == 37:
                break 

            if (questions in done) or (questions in current):
                continue
            
        
            else:
                current.append(questions)
                i += 1


        if len(current) == 0:
            reply = 'Congratulation You Finished All Of Them'

        else:
            done.extend(current)
            converted_list = [str(element) for element in current]
            joined = ', '.join(converted_list)
            reply = joined

    else:
        reply = msg
    
    response = MessagingResponse()
    response.message(reply)

    return str(response)





if __name__ == '__main__':
    app.run(debug=True)