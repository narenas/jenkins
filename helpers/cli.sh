#!/bin/bash
TOKEN="1187ed720890e83403e380a8d0c0c53f72"
USER="nico"

java -jar jenkins-cli.jar -s http://jenkins.192.168.64.13.xip.io/cjoc/ -auth $USER:$TOKEN $*

# token 1187ed720890e83403e380a8d0c0c53f72
