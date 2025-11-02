Restaurant App Deployment with Docker, Kubernetes, CI/CD, Monitoring 

Description

Ce projet montre le déploiement d’une application simple restaurant-app utilisant Docker, Kubernetes, un pipeline CI/CD avec GitHub Actions, et la mise en place d’un monitoring avec Prometheus et Grafana.

(En bonus, une infrastructure AWS minimale a été créée via Terraform à partir de cloudSHELL : une VM EC2 et un bucket S3 pour le stockage)



 Architecture du projet

 <img width="361" height="612" alt="image" src="https://github.com/user-attachments/assets/9eddcaf0-4fc0-4605-9723-48f5ba168615" />



Containerisation

Création d’un Dockerfile multi-stage pour optimiser l’image.

Build local avec Minikube Docker :

eval $(minikube docker-env)
docker build -t restaurant-app:latest .

 Déploiement Kubernetes

Création des manifests :

namespace.yaml

deployment.yaml

service.yaml

Déploiement :

kubectl apply -f namespace.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods -n restaurant-app

 Monitoring avec Helm

Ajout des repositories Helm :

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update


Installation Prometheus & Grafana :

helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring --create-namespace
kubectl get svc -n monitoring


Accès Grafana :

kubectl port-forward svc/prometheus-grafana 3000:80 -n monitoring


 CI/CD avec GitHub Actions

Pipeline automatisé à chaque push :

Build Docker

Lint du code

Possibilité de push vers registry (Docker Hub) ou déploiement sur cluster
