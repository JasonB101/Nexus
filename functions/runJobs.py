import multiprocessing as mp
from classes.Job import Job
from functions.runJob import runJob
def runJobs(lasers):
    jobs = map(lambda laserConfig: Job(laserConfig), lasers)
        
    for job in jobs:
        proc = mp.Process(target=runJob, args=(job,))
        proc.start()