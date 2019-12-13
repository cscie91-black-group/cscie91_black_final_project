pipeline {
    agent any
    
    stages {
        stage("pull-updates-to-dev"){
            when {
                branch 'dev'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@34.238.151.5 'git clone https://github.com/cscie91-black-group/cscie91_black_final_project.git; cd cscie91_black_final_project && git checkout . && git checkout dev && git pull'"
                }
                sleep 2
            }
        }    
        
        stage("run-python-code-on-dev"){
             when {
                branch 'dev'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@34.238.151.5 'cd cscie91_black_final_project && python3.6 test.py'"
                }
                sleep 2
            }
        }
        
        stage("deploy-on-dev"){
             when {
                branch 'dev'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@34.238.151.5 'sudo docker stop $(sudo docker ps -aq); sudo docker run --rm --name web_server_dev -d -p 80:80 nginx'"
                }
                sleep 2
            }
        }
    }
}
