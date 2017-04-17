import time

logs = []

def log(msg):
    global logs
    logs.append(time.strftime("%I:%M:%S") + ": " + msg)
    print(time.strftime("%I:%M:%S") + ": " + msg)

def get_log():
    global logs
    log = logs[-1]
    logs.remove(log)
    return log