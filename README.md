# PCOSense

**IVR-based menstrual health screening and referral platform**

PCOSense is a voice-based healthcare solution designed to make menstrual health screening more accessible, especially for women who may not have access to smartphones or internet-based healthcare applications.

## Current Progress

The current prototype focuses on building the basic IVR pipeline:

```text
Phone
  ↓
Twilio
  ↓
ngrok
  ↓
FastAPI Backend
  ↓
IVR Questions
  ↓
Keypad Responses
```

The system currently allows a user to:

1. Call the PCOSense Twilio number.
2. Select a preferred language:

   * Hindi
   * English
3. Answer whether their period came that month.
4. Provide their usual period duration.
5. Submit responses using keypad inputs.
6. Send the responses to the FastAPI backend.

## Technology Stack

* **Python** — Backend programming
* **FastAPI** — REST API and IVR endpoints
* **Uvicorn** — ASGI server
* **Twilio** — Voice calls and IVR
* **ngrok** — Local development tunnel
* **PostgreSQL** — Planned database for storing responses

## Current IVR Flow

```text
Incoming Call
     ↓
Welcome to PCOSense
     ↓
Language Selection
  1 → Hindi
  2 → English
     ↓
Did your period come this month?
  1 → Yes
  2 → No
     ↓
Period Duration
  1 → Less than 3 days
  2 → 3–7 days
  3 → More than 7 days
     ↓
Response Recorded
```

## Project Structure

```text
PCOSense/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   └── venv/
│
├── frontend/
│
├── docs/
│
└── README.md
```

> `.env` and `venv/` are excluded from GitHub using `.gitignore`.

## Development Status

### Completed

* [x] GitHub repository
* [x] FastAPI backend
* [x] Twilio integration
* [x] ngrok local tunneling
* [x] Hindi/English language selection
* [x] IVR keypad input
* [x] Period-related questions
* [x] Backend receives IVR responses

### Planned

* [ ] PostgreSQL database integration
* [ ] Store patient responses
* [ ] Additional menstrual health questions
* [ ] Screening and referral logic
* [ ] Patient/healthcare-worker portal
* [ ] OTP-based access
* [ ] Production deployment

## Note

PCOSense is currently a prototype for development and testing. It is **not a medical diagnostic system**. Any screening results should be followed by evaluation from a qualified healthcare professional.
