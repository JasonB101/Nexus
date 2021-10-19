import serial
        
def getResponse(port):
    conn = serial.Serial(port=port, baudrate=115200, timeout=5)
    if conn.is_open == True:
         print("Sending: ?")
         conn.write(str('?').encode())
                
    while True:
        response = conn.readline()
        if len(response) > 0:
            print (response.rstrip())
        else:
            break