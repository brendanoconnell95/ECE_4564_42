def getAnswer(str):
    import wolframalpha
    from serverKeys import app_id
    client = wolframalpha.Client(app_id)
    print('Sending question to Wolframalpha: %s' % (str))
    result = client.query(str)
    stringAnswer = next(result.results).text
    print('Received answer from Wolframalpha: %s' % (stringAnswer))
    return stringAnswer

import socket
import sys

input = raw_input("Question: ")
ans = getAnswer(input)
print(ans)