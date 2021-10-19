import serial.tools.list_ports

def getComPorts():
    ports = serial.tools.list_ports.comports()
    portsList = []
    for i in ports:
        portsList.append(i.device)
    return portsList