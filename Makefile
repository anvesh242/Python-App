#Make File to build and run Docker container 
validate: 
    FILE =/tmp/python/Dockerfile
    if test -f "$FILE";then
        echo "$file exists."
    else
	echo "$FILE does not exists,Please locate the Dockerfile"
	fi
build:
  docker build -t python-app .

run:
  docker run -it python-app 
