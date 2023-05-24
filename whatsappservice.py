import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAADzGOOZCvCsBAEreq11RJkavxIBb7R5eaLwAQZAFiPS71Ax4ersjZB7gIbSOJesR0HK9zc5ZBNDhFpWUCZAJAL5iT5YIjGMFLIJM01ZBZAivTOwUZAeFyuNvK56ndQScJ6f3jZA3XA73WyutQECXzk0lESvjZAt1FmZC5EPotwQu1Jw5HI00ZC38qZBe"
        api_url = "https://graph.facebook.com/v16.0/122532270840741/messages"

        headers = {"Content-Type": "application/json", "Authorization": "Bearer" + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers )


        if response.status_code == 200:
            return True
        
        return False
    except Exception as exception:
        print(exception)
        return False