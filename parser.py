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
            elif "Accepted password" in line:
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


logs = log_parse("ssh.log")
print(logs)