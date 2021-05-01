node {

    stage("Clone from SCM - Github")
        {
            git branch: 'master', credentialsId: 'Github-2', url: 'https://github.com/Rohitkuru/schoolmanagement.git'
        }

    stage("Test and build - docker images")
        {
            sh "docker build -t rkuru/school_app:latest ."
            sh "docker build -t rkuru/nginx:latest nginx/."
        }

    stage("Push Docker Images to DockerHub"){

        withCredentials([string(credentialsId: 'DockerPassword-2', variable: 'DockerPassword-2')])
        {

        sh "docker login -u rkuru -p ${DockerPassword-2}"
        sh "docker push rkuru/school_app:latest"
        sh "docker push rkuru/nginx:latest"
        }



    }


}