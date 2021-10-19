#status - 0: ready 1: running 2: paused
class Job:
    
    def __init__(self, config):
        self.status = 0
        self.atHomePos = False
        self.power = config.power()
        self.speed = config.speed()
        self.filepath = config.filepath
        self.port = config.port()

        
