import json
from urllib.parse import parse_qs

from intents import intents
from similarity import get_intent

def handler(request):
    """Vercel Python serverless handler for /get

    Accepts a query parameter `msg` and returns JSON: {"response": "..."}
    """
    # Try common request interfaces
    user_input = ''
    try:
        if hasattr(request, 'args'):
            user_input = request.args.get('msg', '')
        elif hasattr(request, 'GET'):
            user_input = request.GET.get('msg', '')
        else:
            qs = request.environ.get('QUERY_STRING', '')
            user_input = parse_qs(qs).get('msg', [''])[0]
    except Exception:
        user_input = ''

    if not user_input:
        body = json.dumps({'error': 'msg parameter is required'})
        return {
            'statusCode': 400,
            'body': body,
            'headers': {'Content-Type': 'application/json'}
        }

    intent = get_intent(user_input)
    if intent == 'default':
        response_text = "Sorry, I didn't understand that. Can you please rephrase?"
    else:
        resp = intents.get(intent, {}).get('response', '')
        if isinstance(resp, list):
            response_text = resp[0] if resp else ''
        else:
            response_text = resp

    return {
        'statusCode': 200,
        'body': json.dumps({'response': response_text}),
        'headers': {'Content-Type': 'application/json'}
    }
