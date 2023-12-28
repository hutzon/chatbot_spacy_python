import spacy 

nlp = spacy.load("en_core_web_sm")

# Intenciones y respuestas
RESPONSES = {
    "greeting": "Hola, ¿cómo puedo ayudarte hoy?",
    "help_order": "Parece que necesitas ayuda con un pedido. ¿Qué problema tienes?",
    "farewell": "¡Adiós! Espero haber sido de ayuda.",
    "thank_you": "¡De nada! ¿Hay algo más en lo que pueda ayudarte?",
    "product_inquiry": "Puedo ayudarte con eso. ¿Qué producto te interesa?",
    "complaint": "Lamento escuchar que tienes un problema. Por favor, cuéntame más para que pueda asistirte.",
    "delivery_status": "Para revisar el estado de tu entrega, necesitaré tu número de pedido.",
    "payment_issue": "Parece que tienes un problema con el pago. ¿Puedes proporcionar más detalles?"
}

# Palabras clave para cada intención
INTENT_KEYWORDS = {
    "greeting": ["hola", "buenos días", "buenas tardes", "hey", "hello"],
    "help_order": ["ayuda", "pedido", "orden", "problema", "asistencia"],
    "farewell": ["adiós", "hasta luego", "chao", "bye"],
    "thank_you": ["gracias", "te agradezco", "agradecido"],
    "product_inquiry": ["producto", "artículo", "información", "detalles"],
    "complaint": ["queja", "reclamo", "insatisfecho"],
    "delivery_status": ["entrega", "envío", "estado", "paquete"],
    "payment_issue": ["pago", "factura", "problema de pago", "error de pago"]
}


def get_intent(text):
    doc = nlp(text.lower())
    for token in doc:
        for intent, keywords in INTENT_KEYWORDS.items():
            if token.text in keywords:
                return intent
            
    return "unknown"        


def process_text(text):
    intent = get_intent(text)
    return RESPONSES.get(intent, 'lo siento, no estoy seguro de como responder a eso.')


while True:
    user_input = input("Tu: ")
    if user_input.lower() in ["salir", "exit"]:
        print('Bot: Hasta luego!')
        break
    if not user_input.strip():
        print('Bot: Parece que no has ingresado nada. Puedes intentar de nuevo?')
        continue
    response = process_text(user_input)
    print('Bot: ', response)