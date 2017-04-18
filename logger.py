import time

logs = []

def log(msg):
    global logs
    logs.append(time.strftime("%I:%M:%S") + ": " + msg)
    print(time.strftime("%I:%M:%S") + ": " + msg)

def get_logs():
    global logs
    templogs = list(logs)
    for log in templogs:
        logs.remove(log)
    return templogs