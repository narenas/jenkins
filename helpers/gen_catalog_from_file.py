#!/usr/bin/env python
import urllib.request, json
import re

url_base = "https://plugins.jenkins.io/api/plugin/"
url_base_nexus = "https://nexus.alm.europe.cloudcenter.corp/repository/jenkins-plugins/"
#url_base_nexus = "https://repo.jenkins-ci.org/releases/"

def create_json (plug_collection):
    configurations=[]
    configuration={}
    configuration["description"]="Plugins"
    configuration["includePlugins"]=plug_collection
    configurations.append(configuration)
    json_catalog={}
    json_catalog["type"]="plugin-catalog"
    json_catalog["version"]="1"
    json_catalog["name"]="test-nexus-repository"
    json_catalog["displayName"]="Test Nexus Repo"
    json_catalog["configurations"]=configurations
    return json_catalog

def read_plugins(file):
    f = open(file , "r")
    plugins=[]
    for line in f:
        plugins.append(line.rstrip())
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
            gav = data.get("gav")
        gav_split = gav.split(":")
        gav_split[0] = gav_split[0].replace('.','/')
        dir = "/".join(gav_split)
        file = plugin + "-"+version + ".hpi"
        plugin_info = {}
        plugin_info[plugin] = {}
        release_url = url_base_nexus + dir + "/" + file
        plugin_info[plugin]["url"] =  release_url
        #plugin_info[plugin]["version"] = version

    except urllib.error.URLError as e:
        print(plugin + " " + e.reason)
        return 0
    return plugin_info




plugins = read_plugins("plugins_in_catalog.txt")
plug_collection = {}

for plugin in plugins:
    print (plugin)
    my_plugin = plugin.rstrip()
    plug = re.sub('[",]', '', my_plugin)
    plugins_info = generate_json(plug)
    if plugins_info == 0:
        continue
    plug_collection.update(plugins_info)

json_catalog = create_json(plug_collection)

f = open("plugins_catalog.json", "w")
print (json.dumps(json_catalog , indent=4 , sort_keys=True ) , file=f )
f.close
