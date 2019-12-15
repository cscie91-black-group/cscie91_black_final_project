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
        
        stage("build-image-on-dev"){
             when {
                branch 'dev'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@34.238.151.5 'cd cscie91_black_final_project && sudo docker build -t webserver:dev .'"
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
                    sh "ssh -o StrictHostKeyChecking=no e91user@34.238.151.5 'sudo docker stop web_server_dev; sudo docker run --rm --name web_server_dev -d -p 80:80 webserver:dev'"
                }
                sleep 2
            }
        }
        
        stage("merge-dev-to-stage"){
             when {
                branch 'dev'
            }
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'e91user', keyFileVariable: 'KEY_FILE')]) {
                    sh '''
                        eval `ssh-agent -s`
                        ssh-add ${KEY_FILE}
                        test ! $(ssh -o StrictHostKeyChecking=no -T git@github.com)
                        ssh-add -L
                        git remote set-url origin git@github.com:cscie91-black-group/cscie91_black_final_project.git
                        git pull --all
                        git checkout dev
                        git merge stage
                        git commit --allow-empty -m "dev -> stage"
                        git push origin dev:stage
                    '''
                }
                sleep 2
            }
        }
        
        stage("pull-updates-to-stage"){
            when {
                branch 'stage'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@18.234.104.208 'git clone https://github.com/cscie91-black-group/cscie91_black_final_project.git; cd cscie91_black_final_project && git checkout . && git checkout stage && git pull'"
                }
                sleep 2
            }
        }    
        
        stage("run-python-code-on-stage"){
             when {
                branch 'stage'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@18.234.104.208 'cd cscie91_black_final_project && python3.6 test.py'"
                }
                sleep 2
            }
        }
        
        stage("build-image-on-stage"){
             when {
                branch 'stage'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@18.234.104.208 'cd cscie91_black_final_project && sudo docker build -t webserver:stage .'"
                }
                sleep 2
            }
        }
        
        stage("deploy-on-stage"){
             when {
                branch 'stage'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@18.234.104.208 'sudo docker stop web_server_stage; sudo docker run --rm --name web_server_stage -d -p 80:80 webserver:stage'"
                }
                sleep 2
            }
        }
                
        stage("pull-updates-to-prod"){
            when {
                branch 'master'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@35.199.9.219 'git clone https://github.com/cscie91-black-group/cscie91_black_final_project.git; cd cscie91_black_final_project && git checkout . && git checkout master && git pull'"
                }
                sleep 2
            }
        }    
        
        stage("run-python-code-on-prod"){
             when {
                branch 'master'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@35.199.9.219 'cd cscie91_black_final_project && python3.6 test.py'"
                }
                sleep 2
            }
        }
        
        stage("build-image-on-prod"){
             when {
                branch 'master'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@35.199.9.219 'cd cscie91_black_final_project && sudo docker build -t webserver:prod .'"
                }
                sleep 2
            }
        }
        
        stage("deploy-on-prod"){
             when {
                branch 'master'
            }
            steps {
                sshagent (credentials: ['e91user']) {
                    sh "ssh -o StrictHostKeyChecking=no e91user@35.199.9.219 'sudo docker stop web_server_prod; sudo docker run --rm --name web_server_prod -d -p 80:80 webserver:prod'"
                }
                sleep 2
            }
        }
    }
}
