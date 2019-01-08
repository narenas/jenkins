#!/usr/bin/env python
import urllib.request, json
import re

url_base = "https://plugins.jenkins.io/api/plugin/"

def read_plugins(file):
    f = open(file , "r")
    plugins=[]
    for line in f:
        plugins.append(f.readline().rstrip())
        #print(line)
    f.close()
    return plugins

def generate_json(plugin):
    url_plugin = url_base + plugin
    #print ("Get info for " +  url_plugin + "\n")
    try:
        with urllib.request.urlopen(url_plugin) as url:
            data = json.loads(url.read().decode())
            version = data.get("version")
            download_url = data.get("url")
        plugin_info = {}
        plugin_info[plugin] = {}
        #plugin_info[plugin]["version"] = version
        plugin_info[plugin]["url"] =  download_url
    except urllib.error.URLError as e:
        print(plugin + " " + e.reason)
        return 0
    return plugin_info

plugins = read_plugins("plug1.txt")
plug_collection = {}

for plugin in plugins:
    my_plugin = plugin.rstrip()
    plug = re.sub('[",]', '', my_plugin)
#    print (plug)
    plugins_info = generate_json(plug)
    if plugins_info == 0:
        continue
    # print (plugins_info[plugin]["version"])
    # print (plugins_info[plugin]["download_url"])
    plug_collection.update(plugins_info)

f = open("plugins_json.txt", "w")
print (json.dumps(plug_collection , indent=4 , sort_keys=True ) , file=f  )
f.close
