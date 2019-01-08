#!/bin/bash
#TOKEN="1187ed720890e83403e380a8d0c0c53f72"
#USER="nico"
USER="x103814"
#TOKEN_JENKINS_HOME="1169e03f37cf253e2dc27b4e7241dd1047"
#TOKEN_JENKINS_HOME="1169e03f37cf253e2dc27b4e7241dd1047"
TOKEN_JENKINS_HOME="11d33856b4c8ca3b4f923b2faabb78e8fa"
#URL="https://jenkins.home.dyndns.org/cjoc"
#URL="https://jenkins.home.dyndns.org/teams-nico-team/"
URL=https://jenkins.alm.europe.cloudcenter.corp/cjoc/

java -jar jenkins-cli.jar -noCertificateCheck -s $URL -auth $USER:$TOKEN_JENKINS_HOME $*

# token 1187ed720890e83403e380a8d0c0c53f72
