IMAGE_NAME=my-image

.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo
	@echo "Targets:"
	@echo "  test\t\tLookup for docker and docker-compose binaries"
	@echo "  help\t\tPrint this help"
	@echo "  setup\t\tCreate required directories and build docker images"
	@echo "  run\t\tRun job"
	@echo "  run-other\t\tRun other job"
	@echo "  runi\t\tRun interactive shell"

.PHONY: test
test:
	which docker
	which docker-compose

setup: Dockerfile
	docker image build -t $(IMAGE_NAME) .

.PHONY: run
run:
	docker run --rm -v $(PWD):/usr/src/app $(IMAGE_NAME) python py_script

.PHONY: run-other
run-other:
	docker run --rm -v $(PWD):/usr/src/app $(IMAGE_NAME) run echo 'Hello World!'

.PHONY: runi
runi:
	docker run -it --rm -v $(PWD):/usr/src/app $(IMAGE_NAME) bash
