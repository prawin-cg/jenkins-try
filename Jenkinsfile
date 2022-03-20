pipeline{
  agent any
  stages{
    stage('Build'){
      sh 'gcloud builds submit gcr.io/famous-strategy-344516/load-job-img:10'
    }
    stage('Deploy'){
      sh 'gcloud container clusters get-credentials cluster-1 --zone us-central1-c --project famous-strategy-344516'
      sh 'kubectl apply -f cronjob.yaml'
    }
  }
}
