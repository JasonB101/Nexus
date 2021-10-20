import multiprocessing as mp
from classes.Job import Job
from functions.runJob import runJob

def startJobs(lasers, messageBox):
    jobsFinished = False
    jobs = map(lambda laserConfig: Job(laserConfig), lasers)
        
    for job in jobs:
        messageBox.insertMessage(f'Starting {job.profilename}')
        proc = mp.Process(target=runJob, args=(job, ))
        proc.start()
        
    while not jobsFinished:
        #keep checking the que for messages
        break