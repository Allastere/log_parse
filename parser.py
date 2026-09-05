def log_parse(filename):
    logs = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.split()
            if "Failed password" in line:
                log = {
                    "date" : parts[0] + " " + parts[1],
                    "time" : parts[2],
                    "event" : parts[5] + " " + parts[6],
                    "user" : parts[8],
                    "ip" : parts[10],
                    "port" : parts[12]
                }
                logs.append(log)
        for line in file:
            parts = line.split()
            if "Accepted password" in line:
                log = {
                    "date" : parts[0] + " " + parts[1],
                    "time" : parts[2],
                    "event" : parts[5] + " " + parts[6],
                    "user" : parts[8],
                    "ip" : parts[10],
                    "port" : parts[12]
                }
                logs.append(log)
    return logs


def detect_suspicious_ips(logs, threshold = 3):
    failed_attempts = {}
    for log in logs:
        if log["event"] == "Failed password":
            ip = log["ip"]
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
    suspicious_ips = {}

    for ip, attempts in failed_attempts.items():
        if attempts >= threshold:
            suspicious_ips[ip] = attempts

    return suspicious_ips

def print_suspicious_ips(suspicious_ips):
    for ip, attempts in suspicious_ips.items():
        print(f"IP: {ip} | Failed attempts: {attempts}")

logs = log_parse("ssh.log")
failed  = detect_suspicious_ips(logs, 1)
print_suspicious_ips(failed)