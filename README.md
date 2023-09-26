# run-on-cloud-nine

Create and deploy a service on AWS App Runner using this repo as source code repository.


Or create a repository on Amazon's Elastic Container Registry (ECR) push your docker image to it, then create and deploy an App Runner service based on container registry.

```
aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin <AWS ACCOUNT ID>.dkr.ecr.eu-west-1.amazonaws.com
docker build -t run-on-cloud-nine .
docker tag run-on-cloud-nine:latest <AWS ACCOUNT ID>.dkr.ecr.eu-west-1.amazonaws.com/run-on-cloud-nine:latest
docker push <AWS ACCOUNT ID>.dkr.ecr.eu-west-1.amazonaws.com/run-on-cloud-nine:latest
```
