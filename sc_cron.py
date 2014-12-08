import subprocess

def set_job(today):
    subprocess.call(["at", "-f", "run.sh", "-v", "now + 15 days"]) #2 veckor + en extra dag
