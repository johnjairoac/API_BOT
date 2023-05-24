def GefTextUser(message):
    text  = ""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]

    elif typeMessage  == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]

        if typeInteractive == "button_reply":
            text =(interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply ":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")

    else:
        print ("sin mensaje")

    return text



def TextMessage(text, number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "text": {
                "body": text
            },
            "type": "text"
           }
    return data


def TextFormatMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": "*Información importante*\n_Necesitas enviar tu correo_\n"
            }
           }
    return data


def ImageMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "image",
            "image": {
                "link": "https://www.google.com/search?q=whatsapp&rlz=1C1VDKB_esCO1054CO1054&tbm=isch&sxsrf=APwXEddFSSgj8mj4bVmgch-JWU5FxMqKhA:1684774182187&source=lnms&sa=X&ved=2ahUKEwjHqp_1sIn_AhVtgoQIHaRiBhMQ_AUoAnoECAEQBA#imgrc=4oEgdwh7y6UAKM"
            }
           }
    return data

def AudioMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "audio",
            "audo": {
                "link": "https://www.google.com/search?q=whatsapp&rlz=1C1VDKB_esCO1054CO1054&tbm=isch&sxsrf=APwXEddFSSgj8mj4bVmgch-JWU5FxMqKhA:1684774182187&source=lnms&sa=X&ved=2ahUKEwjHqp_1sIn_AhVtgoQIHaRiBhMQ_AUoAnoECAEQBA#imgrc=4oEgdwh7y6UAKM"
            }
           }
    return data

def VideoMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "video",
            "video": {
                "link": "https://www.youtube.com/watch?v=UrsQZpf1jNQ"
            }
           }
    return data

def DocumentMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "document",
            "document": {
                "link": "https://www.youtube.com/watch?v=UrsQZpf1jNQ"
            }
           }
    return data


def LocationMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "location",
            "location":{
                "latitude": "-12.067158831865067",
                "longitude": "-77.0337",
                "name": "Estadio Nacional de peru",
                "address": "calle 100 #100-100"
            } 
           }
    return data

def ButtonsMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body":{
                    "text":"Do you already have an account?"
                },
                "action":{
                    "buttons":[
                        {
                            "type": "reply",
                            "reply":{
                                "id": "001",
                                "title": "log in"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "002",
                                "title": "log in"
                            }
                        }
                    ]
                }
            }
 
           }
    return data


def ListMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type":"list",
                "body":{
                    "text":" I have these options"
                },
                "footer":{
                    "text": "Select an option"
                },
                "action":{
                    "button": "see options",
                    "sections":[
                        {
                            "title": "Buy and sell products",
                            "rows":[
                                {
                                    "id": "main-buy",
                                    "title": "Buy",
                                    "description": "Buy the best product your home"
                                },
                                {
                                    "id": "main-sell",
                                    "title": "Sell",
                                    "description": "Sell your products"                                   
                                }
                            ]
                        },
                        {
                            "title": "center of attention",
                            "rows":[
                                {
                                    "id": "main-agency",
                                    "title": "Agency",
                                    "description": "Your can visit our agency"
                                },
                                {
                                    "id": "main-sell",
                                    "title": "Contact center",
                                    "description": "One  of our agents will assist you"                                   
                                }
                            ]
                        }
                    ]                
                }
            }
         }
 
           
    return data