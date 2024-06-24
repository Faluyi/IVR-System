# Interactive Voice Response (IVR) System

![Screenshot (129)](https://github.com/Faluyi/IVR-System/assets/83612442/22d40c8e-6524-4081-a603-2d4c1dd60466)


## Overview

This Interactive Voice Response (IVR) System is a powerful automation solution built using the Twilio API. It is designed to initiate calls, record conversations, transcribe the calls, extract digits from the transcriptions, and save the extracted data in a text file. This system offers a versatile and efficient way to handle voice communication and data extraction.

![IVR system design](https://github.com/Faluyi/IVR-System/assets/83612442/df0a5c88-5bc5-472c-9d30-849ee7e95fac)

## Features

- **Call Initiation:** The IVR system can initiate calls to active phone numbers.

- **Call Recording:** It records entire call conversations for reference and analysis.

- **Transcription:** The system transcribes the recorded calls, converting spoken words into text.

- **Digit Extraction:** The system can identify and extract digits from the transcribed conversations.

- **Data Storage:** Extracted digits are saved in a text file for further use.

## Prerequisites

Before using the IVR system, ensure you have the following prerequisites in place:

- Python: The script is written in Python, so make sure you have it installed.

- Twilio Account: You need a Twilio account with the necessary credentials and a Twilio phone number.

- Flask (for handling callback endpoints): Install Flask using `pip install Flask`.

- [ngrok](https://ngrok.com/): If you're testing locally, ngrok can help expose your local server to the public internet.

## Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/Faluyi/IVR-System.git
