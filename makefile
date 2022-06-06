install-concourse:
	curl -O https://concourse-ci.org/docker-compose.yml

up:
	docker-compose up -d 

ci-login:
	fly -t tutorial login -c http://localhost:8080

pipeline:
	fly -t tutorial set-pipeline -p games-api -c ci/pipeline.yml

unpause:
	fly -t tutorial unpause-pipeline -p games-api

down:
	docker-compose down 
	