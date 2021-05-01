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

        withCredentials([string(credentialsId: 'newdockercre', variable: 'newdockercre')])
        {

         sh "docker login -u rkuru -p ${newdockercre}"
        sh "docker push rkuru/school_app:latest"
        sh "docker push rkuru/nginx:latest"
        }



    }


}