Build and Run Image Locally Via Compose: <br>
PORT=<PORT_NUMBER> docker-compose up --build

Build, Push, and Run image: 
docker build -t <IMAGE_NAME> .
docker push <IMAGE_NAME>  
docker run -e PORT=<PORT_NUMBER> -p <PORT>:<PORT> <IMAGE_NAME>

You can also pull image via: 
docker pull cato16/py-to-do found on https://hub.docker.com/r/cato16/py-to-do

Deploy and Apply Image
kubectl apply -f service.yaml
kubectl apply -f deploy.yaml 
kubectl get service app-service 

