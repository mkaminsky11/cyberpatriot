import subprocess

print "Cyberpatriot script starting..."

#DO BASIC UPGRADES
#=====================
subprocess.call("apt-get update -y".split())
subprocess.call("apt-get upgrade -y".split())

print "basic updates done! downloading tools!"

tools_array = ["libpam-cracklib", "nmap", "gufw", "rkhunter", "chkrootkit"]
tools = "apt-get install " + ' '.join([str(x) for x in tools_array]) + " -y"
subprocess.call(tools.split())

#UPDATE FIREFOX
#======================
print "tools downloaded! updating firefox!"

subprocess.call("killall firefox".split())
subprocess.call("apt-get remove firefox -y".split())
subprocess.call("apt-get install firefox -y".split())