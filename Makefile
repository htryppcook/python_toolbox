
TAG = python_toolbox
BUILD_CMD = sudo docker build -t $(TAG) .
RUN_CMD = sudo docker run
LOGCAPTURE =

ifneq ($(DISABLE_NOSETEST_LOGCAPTURE),)
  LOGCAPTURE = --nologcapture
endif

# External Commands
docker_test:
	$(BUILD_CMD)
	$(RUN_CMD) -t $(TAG) make test
docker_test_verbose:
	$(BUILD_CMD)
	$(RUN_CMD) -e DISABLE_NOSETEST_LOGCAPTURE=true -t $(TAG) make test 
docker_test_debug:
	$(BUILD_CMD)
	$(RUN_CMD) -i -t $(TAG) /bin/bash

# Internal Commands
init:
	python setup.py install
test:
	python setup.py nosetests $(LOGCAPTURE)

