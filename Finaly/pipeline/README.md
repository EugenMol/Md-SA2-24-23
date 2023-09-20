#Описание pipeline
Push main branch from git
Check Dockerfile hadolint
Start Docker container
Проверяем на работоспособность запущенные конейнер командой curl
Push Docker image on DockerHub
Deploy on k8s namespace Test
Start QA test
Manual approve
Deploy on k8s namespace PreProd 
