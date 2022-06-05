# Infrastructure

There are many ways to deploy an application onto virtual machines, containers, and more. For this project the `games-api` can be deployed onto a local Kubernetes cluster with provisioning done by Ansible.

## Pre-Requisites

Minikube should be up and running, a simple

```
minikube start 
```
on your terminal will create a barebones Kubernetes cluster with all the bells and whistles to get you started.

Note: You may specify drivers by passing in the `--driver=${driver_name}` command. More info found at https://minikube.sigs.k8s.io/docs/drivers/ . By default minikube will use the Docker driver. 

Ansible should also be installed and a virtual environment to be able to run the ansible playbook.

## Ansible

In your terminal you can run the command:

```
ansible-playbook ansible/minikube_deploy.yml
```

which will perform tasks to build the games-api image via Dockerfile and create Kubernetes resources (namespace, service, and deployment) to spin up application pods in your cluster.

## Kubernetes

Once the playbook completes you can inspect the custer and run `kubectl` commands to interact with it.

To find all resources within the `games-api` namespace:

```
kubectl get all -n games-api
NAME                            READY   STATUS    RESTARTS   AGE
pod/games-api-5ff77cfb4-chmk9   1/1     Running   0          25m
pod/games-api-5ff77cfb4-nqmjb   1/1     Running   0          25m

NAME                TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                         AGE
service/games-api   LoadBalancer   10.111.202.150   <pending>     5000:30299/TCP,8000:31802/TCP   25m

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/games-api   2/2     2            2           25m

NAME                                  DESIRED   CURRENT   READY   AGE
replicaset.apps/games-api-5ff77cfb4   2         2         2       25m
```

## How to Access

Due to limitations with minikube, the default Docker driver will not allow you to run the `minikube service` command which allows a user to access their app through a browser by exposing a port and IP from the cluster. 

Depending on the OS, one could install a different driver such as `hyperkit` and it should work.

Note: By default the games-api service does not have an `external-ip` that can be used as there needs to be some sort of proxy and/or ingress. Cloud providers such as AWS EKS for example would provide one given there is a LoadBalancer type. 

Fear not as one can access it by opening a tunnel. Run `minikube tunnel`


```
minikube tunnel
✅  Tunnel successfully started

📌  NOTE: Please do not close this terminal as this process must stay alive for the tunnel to be accessible ...

🏃  Starting tunnel for service games-api.
```
 
 then open another terminal. Run:
 ```
 kubectl get services games-api -n games-api
NAME        TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                         AGE
games-api   LoadBalancer   10.111.202.150   127.0.0.1     5000:30299/TCP   31m
```

You will now see an `External-IP`. Note the IP and port.

Go to your browser and in the example above the application will be accessible at `127.0.0.1:5000`

Horray! You should be able to access the app through the Kubernetes cluster now. 

## Future Improvements
- Use Terraform and provision infrastructure in AWS, GCP, etc.
- Use Packer to build the image 
- Add infrastructure tests like Terragrunt, Goss, etc. 
- Create a DNS record with SSL to secure the cluster and access through a friendly record name. 
