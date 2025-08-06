**Build and Run Image Locally Via Compose:** <br>
```
PORT=<PORT_NUMBER> docker-compose up --build
```

**Build, Push, and Run Image:**
```
docker build -t <IMAGE_NAME> .
docker push <IMAGE_NAME>  
docker run -e PORT=<PORT_NUMBER> -p <PORT>:<PORT> <IMAGE_NAME>
```

**You can also pull image via:**
```
docker pull cato16/py-to-do
```
found on https://hub.docker.com/r/cato16/py-to-do

Note: docker compose does not utilize secrets and config map files.
      Main purpose is to test whether containers and connections are working properly.

**Creating Secrets and Config Maps:**
```
kubectl create secret generic to-do-secret1 --from-literal='password=password1'
kubectl create configmap to-do-config1 --from-literal='user=user1' --from-literal='db=db1'

# Confirm successful compilation.
kubectl get secrets 
kubectl get configmaps
```
**Deploy and Apply Image**
```
minikube apply -f service.yaml
minikube apply -f deploy.yaml 
minikube get service app-service 
```
