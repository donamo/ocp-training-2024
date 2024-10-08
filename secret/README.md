cmd:

```
kubectl create secret docker-registry dockerhub --from-file=.dockerconfigjson=secret/dockerconfig.json
```

kubectl edit sa/default
