# Dash App

## How to run
On your terminal, create a new python environment
```
conda create -n rental_gpt_app
```

On your terminal, install all package
```
pip install -r requirements.txt
```

On your terminal, run the dash application via Bash
```
sh run.sh
```

## How to dockerize
Make sure you have DockerHub account

Make sure you have Docker Desktop installed locally. Open Docker Desktop and sign in with your DockerHub to enable Docker daemon to run on the background.

On your terminal, create a Docker image
```
docker build -t your-dockerhub-username/project-name .
```

On your terminal, test run your built Docker image
```
docker run -p 5000:8050 your-dockerhub-username/project-name
```

To deploy on GCP or Kubernetes Rancher, please check this [README](https://github.com/mnguyen0226/rental_gpt_dash/blob/main/README.md).