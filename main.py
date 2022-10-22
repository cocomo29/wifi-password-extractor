from subprocess import check_output, CalledProcessError

data = check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
names = []

for i in data:
    if "All User Profile" in i:
        names.append(i.split(":")[1][1:-1])
        
result = {}

try:
    for i in names:
        password = check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode("utf-8").split("\n")
        for j in password:
            if "Key Content" in j:
                result[i] = j.split(":")[1][1:-1]
                break
            else:
                result[i] = ""
except CalledProcessError:
    print("[!] Couldn't Retrieve Profiles. Are you sure this is a Windows System?")
    exit(0)

for i in result:
        print("{:<29}--------             {:<29}".format(i, result[i]))
