def getConfig():
    config = {}
    for c in open("config.ini").read().split("\n"):
        if "=" in c:
            key, val = c.split("=")
            config[key.strip()] = val.strip()
    return config