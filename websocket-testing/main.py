import websocket
import json
import helper

# WebSocket URL for the states_list API
websocket_url = "wss://ws.binaryws.com/websockets/v3?app_id=36544"
TEST_CASES= []

def append_data(description,excpected_result,actual_result, status):
    print(description)
    TEST_CASES.append({
        'step'                  : len(TEST_CASES) + 1,
        'test step'             : description,
        'excpected result'      : excpected_result,
        'actual result'         : actual_result,
        'status'                : status
        })

def verify_data(response_data):
    if (response_data.get('error')):
        append_data("verifying data","data is verified","data is not verified","fail")
        return False
    else:
        append_data("verifying data","data is verified","data is verified","pass")
        return True

def on_message(ws, message):
    response_data = json.loads(message)
    append_data("Recieving response from the server","response recieved successfully","response recieved successfully","pass")
    # Perform verification of the received response data

    verify_data(response_data)
    ws.close()

def on_error(ws, error):
    print("WebSocket Error:", error)

def on_close(ws, close_status_code, close_msg):
    append_data("Closing connection","connection closed successfully","connection closed successfully","pass")
    print("WebSocket Connection Closed")

def on_open(ws):
    append_data("Creating connection","connection created","connection created","pass")
    print("connection created")
    # Send your request to the server
    request = {
    "states_list": "us"
    }

    append_data("Sending a request for states","request sent successfully","request sent successfully","pass")
    ws.send(json.dumps(request))


if __name__ == "__main__":
    ws = websocket.WebSocketApp(websocket_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    
    ws.on_open = on_open
    ws.run_forever()

    helper.save_data(TEST_CASES)