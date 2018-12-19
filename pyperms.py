# usr/bin/env python
import glob
import os
from ruamel.yaml import YAML

VERBOSE = False
YAML = YAML()
dir = glob.glob1("users/", "*.group")
config = YAML.load(open("users/config.yml"))

for server in config['servers']:
    print "************************************"
    print "> Server: " + server
    print "************************************"

    for groupFile in dir:

        # get name of group by stripping ".group" from file name
        groupName = groupFile.replace(".group", "").lower()

        # try to find group override
        try:
            override = config['servers'][server]['override'][groupName].lower()
        except:
            override = groupName
        if VERBOSE:
            print "> " + groupName + " --> " + override

        # pull usernames from group file
        readGroupFile = open("users/" + groupFile).read().splitlines()

        # iterate and send mark2 command for each user
        for user in readGroupFile:
            try:
                cmd = "mark2 send -n " + server + " lp user " + user.lower() + " parent set " + override
                print ">> " + cmd
                #os.system(cmd)
            except:
                print "Error sending command"
            if VERBOSE:
                print ">> " + user.lower() + " --> " + override
