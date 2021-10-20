import serial
import time
        
def getReport(port):
    conn = serial.Serial(port=port, baudrate=115200, timeout=5)
    if conn.is_open == True:
        print(f'Getting report from {port}')
        conn.write(("\r\n\r\n").encode())
        time.sleep(2)   # Wait for grbl to initialize
        conn.flushInput()
        conn.write(('?').encode())
                
    while True:
        response = conn.readline()
        if len(response) > 0:
            return f'PORT: {port} - {response.rstrip()}'
        else:
            break
        
    return f'PORT: {port} - No Response...'
        