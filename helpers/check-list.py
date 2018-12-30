#!/usr/bin/env python

import re

file_black = "blacklisted-plugins"
file_plug = "plugins3.txt"

def read_plugins(file):
    f = open(file , "r")
    plugins=[]
    for line in f:
        if ((not line.startswith("#")) and (line.strip())):
            plugin = line.strip().split(" ")
            #print (plugin[0])
            plugins.append(plugin[0])
    f.close()
    return plugins

plugins_installed = read_plugins(file_plug)
plugins_blacklisted = read_plugins(file_black)

black_dict = {}
for plugin_black in plugins_blacklisted:
    match = re.match('(^.*)-(\d.*)' ,plugin_black )
    if match:
        black_dict[match.group(1)] = match.group(2)

    else:
        black_dict[plugin_black] = ""

for plugin in plugins_installed:
    if plugin in black_dict.keys():
        print("%s is blacklisted version to check if version installed is  %s" % (plugin , black_dict[plugin]))
