set -x
docker rm my-spark-app
docker rmi python-spark-app
docker build --rm -t python-spark-app .
docker run --name my-spark-app -e ENABLE_INIT_DAEMON=false --link spark-master:spark-master --net examples_default python-spark-app

