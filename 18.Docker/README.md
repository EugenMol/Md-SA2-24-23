#Команда для запуска докер контейнера с actions runner
#На хосте должен быть установлен docker-compose как standalone (обязательно, как плагин не работает)
#При создание нового образа надо уточнить версию actions-runner с сайта github и TOKEN
#Записать значение этих переменных в соответствующие поля Dockerfile
docker build -t start_github_action .   - сборка образа 
docker run -ti -v /var/run/docker.sock:/var/run/docker.sock -v /usr/local/bin/docker-compose:/usr/local/bin/docker-compose -v ./:/app start_github_action bash - запуск контейнера
