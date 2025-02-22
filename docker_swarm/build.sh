docker build -t node_swarm:0.1.0  . 

docker swarm init 

docker service create --replicas 3 --name node_swarm  --publish 3000:3000 node_swarm:0.1.0

echo "Done"