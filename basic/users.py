import subprocess
import os.path


#REMOVING THIS BECAUSE IT NEEDS TO BE REDONE

#FIRST GET ALL USERS
#=====================
# this gets all human users
# before, just got all in "/home"
p = subprocess.Popen("cut -d: -f1,3 /etc/passwd | egrep ':[0-9]{4}$' | cut -d: -f1".split(), stdout=subprocess.PIPE)
output, err = p.communicate()
users_on_computer = output.split("\n")


# removed reading auth.txt/admin.txt (it's clunky)
# WHAT NEXT?
# have script parse the README provided by cyberpatriot to find its list of admins and users (TODO)


#THEN LOCK ROOT
#=============
subprocess.call("passwd -l root".split())
print "root has been locked!"

#/etc/security/access.conf -:root: ALL EXCEPT LOCAL
if os.path.exists("/etc/security/access.conf") == True:
    with open("/etc/security/access.conf", "a") as myfile:
        myfile.write("\n-:root: ALL EXCEPT LOCAL")
    print "access.conf edited!"
else:
    print "/etc/security/access.conf not found!"

#LOCK GUEST
#===========
if os.path.exists("/etc/lightdm/lightdm.conf") == True:
    with open("/etc/lightdm/lightdm.conf", "a") as myfile:
        myfile.write("\nallow-guest=false")

    print "guest locked!"
else:
    print "/etc/lightdm/lightdm.conf does not exist"
