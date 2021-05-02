node {

    stage("Clone from SCM - Github")
        {
            git branch: 'master', credentialsId: 'Github-2', url: 'https://github.com/Rohitkuru/schoolmanagement.git'
        }

    stage("Test and build - docker images")
        {
            sh "docker build -t rkuru/school_app:latest ."
            sh "docker build -t rkuru/school_app-nginx:latest nginx/."
        }

    stage("Push Docker Images to DockerHub"){

        withCredentials([string(credentialsId: 'newdockercre', variable: 'newdockercre')])
        {

            sh "docker login -u rkuru -p ${newdockercre}"
            sh "docker push rkuru/school_app:latest"
            sh "docker push rkuru/school_app-nginx:latest"
        }

    stage("Pull images to webserver")
        {
            sshagent(['swam-agent-test'])
            {
                   sh "scp -o StrictHostKeyChecking=NO docker-compose.yml automation@194.195.119.41:/app"
                   sh "ssh -o StrictHostKeyChecking=NO automation@194.195.119.41 /usr/bin/sudo docker pull rkuru/school_app:latest"
                   sh "ssh -o StrictHostKeyChecking=NO automation@194.195.119.41 /usr/bin/sudo docker pull rkuru/school_app-nginx:latest"
                   sh "ssh -o StrictHostKeyChecking=NO automation@194.195.119.41 /usr/bin/sudo docker stack deploy --compose-file /app/docker-compose.yml schoo_app"
            }

        }


    }


}