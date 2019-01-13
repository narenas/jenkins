#!/usr/bin/env python

def read_plugins(file):
    f = open(file , "r")
    plugins=[]
    for line in f:
        plugins.append(line.rstrip())
        #print(line)
    f.close()
    return plugins

all_plugins = read_plugins("plugins_installed.txt")
not_install = read_plugins("not_in_catalog.txt")
catalog_plugins = []
f = open("plugins_in_catalog.txt", "w")
for plugin in all_plugins:
    if str(plugin) not in not_install:
        print (plugin + " not in")
        catalog_plugins.append(plugin)
        print (plugin , file=f)


print (not_install)
print (catalog_plugins)
