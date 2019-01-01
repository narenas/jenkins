#!/bin/bash
TOKEN="1187ed720890e83403e380a8d0c0c53f72"
USER="nico"
TOKEN_JENKINS_HOME="1169e03f37cf253e2dc27b4e7241dd1047"
#URL="https://jenkins.home.dyndns.org/cjoc"
URL="https://jenkins.home.dyndns.org/teams-nico-team/"

java -jar jenkins-cli.jar -noCertificateCheck -s $URL -auth $USER:$TOKEN_JENKINS_HOME $*

# token 1187ed720890e83403e380a8d0c0c53f72
