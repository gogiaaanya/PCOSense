from fastapi import FastAPI, Request
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Gather

app = FastAPI(title="PCOSense API")


@app.get("/")
def home():
    return {
        "message": "PCOSense backend is running!"
    }


# STEP 1: Initial language selection
@app.post("/ivr")
async def ivr(request: Request):

    response = VoiceResponse()

    gather = Gather(
        num_digits=1,
        action="https://equipment-stew-profound.ngrok-free.dev/ivr/language",
        method="POST"
    )

    gather.say(
        "नमस्ते, PCOSense में आपका स्वागत है। "
        "हिंदी के लिए एक दबाएं। "
        "For English, press two.",
        language="hi-IN"
    )

    response.append(gather)

    return Response(
        content=str(response),
        media_type="application/xml"
    )


# STEP 2: Language selection
@app.post("/ivr/language")
async def language(request: Request):

    form = await request.form()
    digit = form.get("Digits")

    print("Language selected:", digit)

    response = VoiceResponse()

    if digit == "1":

        gather = Gather(
            num_digits=1,
            action="https://equipment-stew-profound.ngrok-free.dev/ivr/period?lang=hi",
            method="POST"
        )

        gather.say(
            "आपने हिंदी चुनी है। "
            "क्या इस महीने आपके पीरियड आए थे? "
            "हाँ के लिए एक दबाएं। "
            "नहीं के लिए दो दबाएं।",
            language="hi-IN"
        )

        response.append(gather)

    elif digit == "2":

        gather = Gather(
            num_digits=1,
            action="https://equipment-stew-profound.ngrok-free.dev/ivr/period?lang=en",
            method="POST"
        )

        gather.say(
            "You have selected English. "
            "Did your period come this month? "
            "Press one for yes. "
            "Press two for no.",
            language="en-IN"
        )

        response.append(gather)

    else:

        response.say(
            "कृपया सही विकल्प चुनें। "
            "हिंदी के लिए एक दबाएं। "
            "For English, press two.",
            language="hi-IN"
        )

        response.redirect(
            "https://equipment-stew-profound.ngrok-free.dev/ivr"
        )

    return Response(
        content=str(response),
        media_type="application/xml"
    )


# STEP 3: Period question
@app.post("/ivr/period")
async def period(request: Request):

    form = await request.form()

    answer = form.get("Digits")
    lang = request.query_params.get("lang")

    print("Period answer:", answer)
    print("Selected language:", lang)

    response = VoiceResponse()

    gather = Gather(
        num_digits=1,
        action=f"https://equipment-stew-profound.ngrok-free.dev/ivr/duration?lang={lang}",
        method="POST"
    )

    if lang == "hi":

        gather.say(
            "आपके पीरियड आमतौर पर कितने दिनों तक चलते हैं? "
            "तीन दिनों से कम के लिए एक दबाएं। "
            "तीन से सात दिनों के लिए दो दबाएं। "
            "सात दिनों से अधिक के लिए तीन दबाएं।",
            language="hi-IN"
        )

    else:

        gather.say(
            "How many days does your period usually last? "
            "Press one for less than 3 days. "
            "Press two for 3 to 7 days. "
            "Press three for more than 7 days.",
            language="en-IN"
        )

    response.append(gather)

    return Response(
        content=str(response),
        media_type="application/xml"
    )


# STEP 4: Period duration
@app.post("/ivr/duration")
async def duration(request: Request):

    form = await request.form()

    answer = form.get("Digits")
    lang = request.query_params.get("lang")

    print("Period duration:", answer)
    print("Selected language:", lang)

    response = VoiceResponse()

    if answer not in ["1", "2", "3"]:

        if lang == "hi":

            response.say(
                "हमें आपका सही जवाब नहीं मिला। "
                "कृपया दोबारा कॉल करके प्रयास करें।",
                language="hi-IN"
            )

        else:

            response.say(
                "We could not receive a valid response. "
                "Please call again and try once more.",
                language="en-IN"
            )

        return Response(
            content=str(response),
            media_type="application/xml"
        )

    print("Period duration recorded:", answer)

    if lang == "hi":

        response.say(
            "धन्यवाद। आपकी सभी प्रतिक्रियाएं सफलतापूर्वक दर्ज कर ली गई हैं। "
            "PCOSense का उपयोग करने के लिए आपका धन्यवाद। "
            "अपना ध्यान रखें और स्वस्थ रहें। "
            "आपका दिन शुभ हो।",
            language="hi-IN"
        )

    else:

        response.say(
            "Thank you. Your responses have been recorded successfully. "
            "Thank you for using PCOSense. "
            "Please take care of yourself and stay healthy. "
            "Have a wonderful day.",
            language="en-IN"
        )

    return Response(
        content=str(response),
        media_type="application/xml"
    )