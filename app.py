from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
import re
import os

app = Flask(__name__)

# Your Twilio Account SID and Auth Token
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_phone_number = "+16613753487"

target_phone_number = '+2347068162549'
numbers_file_path = 'numbers.txt'
output_file_path = "results.txt"


# Initialize Twilio client
client = Client(account_sid, auth_token)

# Create a TwiML response object
response = VoiceResponse()
response.play(digits='1')  # Send the DTMF tone "1"
response.record(
action='https://b7eb-196-220-147-48.ngrok.io/handle-recording',  # Set this to your recording handling endpoint
maxLength=120,
transcribe=True,
transcribeCallback='https://b7eb-196-220-147-48.ngrok.io/handle-transcription'  # Set this to your transcription handling endpoint
)



def store_result(number, extracted_number):
        with open(output_file_path, "a") as f:
            result = f"{number}={extracted_number}"
            f.writelines(result)
            print(f"Stored result: {result}")


# Function to initiate a call
# @app.route('/initiate-call', methods=['GET'])
def initiate_call():
    
    call = client.calls.create(
        to = target_phone_number,  # Replace with the target phone number
        from_ = twilio_phone_number,
        twiml=str(response)
    )
    
    return f"Initiated Call with SID: {call.sid}"

# Function to handle the recording callback
@app.route('/handle-recording', methods=['POST'])
def handle_recording():
    recording_url = request.form['RecordingUrl']
    
    # Process the recording URL as needed
    # For simplicity, we'll just print it
    app.logger.info(recording_url)
    return "Recording URL Received"

# Function to handle the transcription callback
@app.route('/handle-transcription', methods=['POST'])
def handle_transcription():
    transcription_text = request.form['TranscriptionText']
    pattern = r'\d+' 
    match = re.findall(pattern, transcription_text)
    
    if match:
        extracted_number = match
    else:
        extracted_number = None # or any other value you want to use for non-matching cases
    
    # Store the number and result in the output file
    store_result(target_phone_number, extracted_number)
   
    print("Transcription Text:", transcription_text)

    return "Transcription Text Received"

    
if __name__ == '__main__':
    initiate_call()
    app.run()
    # with open(numbers_file_path) as f:
    #     numbers = f.read().splitlines()
    # # Iterate over the numbers and make the phone calls
    # for number in numbers:
    #     target_phone_number = number
    #     initiate_call(number)

