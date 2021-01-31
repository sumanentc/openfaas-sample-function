## Sample Serverless Function using [OpenFaas Templates](https://github.com/openfaas/templates)

- python3-sample is a sample function written in python3 using [python3 template](https://github.com/openfaas/templates/tree/master/template/python3)
  To deploy the function we need to execute the below commands

```
export OPENFAAS_PREFIX=sumand
faas-cli up -f python3-sample/python-hello-world.yml

```

To invoke the function we need to run the below commands

```

curl http://127.0.0.1:8080/function/py-hello-world --data-binary '{ "name": "Suman", "greeting": "Hello" }'

```

- dockerfile-sample is a sample function written using [dockerfile template](https://github.com/openfaas/templates/tree/master/template/dockerfile)

```
export OPENFAAS_PREFIX=sumand
faas-cli up -f dockerfile-sample/sample-flask-service.yml

```

```
curl http://127.0.0.1:8080/function/sample-flask-service/api/items

```
