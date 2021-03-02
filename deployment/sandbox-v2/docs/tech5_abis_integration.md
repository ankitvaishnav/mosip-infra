# Tech5 ABIS integration

## Setup from Tech5 ABIS side

### ABIS gallery matcher
Tech5 gives us a VM that contains ABIS & other related modules

Tech5 ABIS directory: /opt/Tech5/t5plugin

#### Update config.properties
```text
url=http://localhost:9090/T5CloudService/1.0/processRequest

consumeURL=tcp://sandbox2.mosip.net:30616
publishURL=tcp://sandbox2.mosip.net:30616

consumeQueue=mosip-to-abis1
publishQueue=abis1-to-mosip

#####qa
authenticationUrl=https://sandbox2.mosip.net/v1/authmanager/authenticate/clientidsecretkey
biometricUrl=https://sandbox2.mosip.net/registrationprocessor/v1/bio-dedupe/biometricfile

appId=regproc
clientId=mosip-regproc-client
secretKey=
id=io.mosip.registration.processor
version=v1

irisThreshold=0.2
faceThreshold=8.0
fingerThreshold=0.2
maxResults=10

```

#### Start & stop gallery matcher

* Go to Tech5 ABIS directory
* Check if the gallery matcher is already running: `ps -ef | grep galler`
```text
centos   15451(pid) 14811 29 11:30 pts/0    00:00:01 java -jar galleryMatcher_sqlite.jar
centos   15475 14811  0 11:30 pts/0    00:00:00 grep --color=auto galler
```
* Kill gallery matcher: `kill -9 <pid>`
* Clear the nohup logs: `sudo rm nohup.out`
* Run the gallery matcher: `sudo nohup java -jar galleryMatcher_sqlite.jar &`


### ABIS service
Copy & paste the below script in a new bash file (ABIS-MOSIP-StartStopServices.sh)

```shell
#!/bin/bash/
# Built by Tech5 team. Contact us at support@tech5-sa.com 

# Script to perform operations on ABIS System.

## Function to stop services.

StopServices () {

for service in Master FaceM IrisM FingerM FaceTC IrisTC FingerTC
do
    sh /opt/Tech5/T5-ABIS/$service/bin/catalina.sh stop
    sleep 10
done

kill -9 `ps aux | grep java | grep ABIS | awk '{print $2}'`

}


## Function to start ABIS services:

StartServices () {

for service in Master FaceM IrisM FingerM FaceTC IrisTC FingerTC
do
    sh /opt/Tech5/T5-ABIS/$service/bin/catalina.sh start
    sleep 10
done

# Check logs to see if there are any errors

for abislogs in Master FaceM IrisM FingerM FaceTC IrisTC FingerTC
do
    printf "\n\033[41m******** $abislogs Catalina logs **********\e[0m\n\n"
    tail -30 /opt/Tech5/T5-ABIS/$abislogs/logs/catalina.out

    printf "\n\033[41m******** $abislogs ABIS logs **********\e[0m\n\n"
    tail -30 /opt/Tech5/T5-ABIS/$abislogs/logs/T5Service.log
done

# Check getStatus page

curl http://localhost:9090/T5CloudService/1.0/getStatus

}

## Script to Re-start services

RestartServices () {

for service in Master FaceM IrisM FingerM FaceTC IrisTC FingerTC
do
    sh /opt/Tech5/T5-ABIS/$service/bin/catalina.sh stop
    sleep 10
done

kill -9 `ps aux | grep java | grep ABIS | awk '{print $2}'`

# Starting services

for service in Master FaceM IrisM FingerM FaceTC IrisTC FingerTC
do
    sh /opt/Tech5/T5-ABIS/$service/bin/catalina.sh start
    sleep 10
done

# Check logs to see if there are errors

for abislogs in Master FaceM IrisM FingerM FaceTC IrisTC FingerTC
do
    printf "\n\033[41m******** $abislogs Catalina logs **********\e[0m\n\n"
    tail -30 /opt/Tech5/T5-ABIS/$abislogs/logs/catalina.out

    printf "\n\033[41m******** $abislogs ABIS logs **********\e[0m\n\n"
    tail -30 /opt/Tech5/T5-ABIS/$abislogs/logs/T5Service.log
done

# Check getStatus Page

curl http://localhost:9090/T5CloudService/1.0/getStatus

}


## Function to backup exisitng ABIS cache and Re-start services with zero cache

RestartServicesWithZeroCache () {


for service in Master FaceM IrisM FingerM FaceTC IrisTC FingerTC
do
    sh /opt/Tech5/T5-ABIS/$service/bin/catalina.sh stop
    sleep 10
done

kill -9 `ps aux | grep java | grep ABIS | awk '{print $2}'`

mv /opt/Tech5/T5-ABIS/cache /opt/Tech5/T5-ABIS/cache_backup
mkdir /opt/Tech5/T5-ABIS/cache


for service in Master FaceM IrisM FingerM FaceTC IrisTC FingerTC
do
    sh /opt/Tech5/T5-ABIS/$service/bin/catalina.sh start
    sleep 10
done


for abislogs in Master FaceM IrisM FingerM FaceTC IrisTC FingerTC
do
    printf "\n\033[41m******** $abislogs Catalina logs **********\e[0m\n\n"
    tail -30 /opt/Tech5/T5-ABIS/$abislogs/logs/catalina.out

    printf "\n\033[41m******** $abislogs ABIS logs **********\e[0m\n\n"
    tail -30 /opt/Tech5/T5-ABIS/$abislogs/logs/T5Service.log
done


curl http://localhost:9090/T5CloudService/1.0/getStatus

}



#################################################################


echo 'Select an option to perform Operation
  1) Select 1 to Start ABIS Services
  2) Select 2 to Stop ABIS Services 
  3) Select 3 to Restart ABIS Services
  4) Select 4 to Clear Cache & Restart ABIS Services
  5) Exit?'

read OPTION


if [ "$OPTION" == "1" ]
        then
                echo "Starting ABIS Services"
		StartServices

    elif [ "$OPTION" == "2" ]
        then
                echo "Stoping ABIS Services"
		StopServices

    elif [ "$OPTION" == "3" ]
        then
                echo "Restarting ABIS Services"
		RestartServices				

    elif [ "$OPTION" == "4" ]
        then
                 echo "Clearing Cache & ReStarting ABIS Services"
		 RestartServicesWithZeroCache
				 

    else
        echo "Please select one of these 1 or 2 or 3 or 4 options to run the script"

fi


###           End of the Script  ###################
```

Start ABIS: `sh ABIS-MOSIP-StartStopServices.sh 1`

Stop ABIS: `sh ABIS-MOSIP-StartStopServices.sh 2`

Restart ABIS: `sh ABIS-MOSIP-StartStopServices.sh 3`

Clear cache & retart ABIS: `sh ABIS-MOSIP-StartStopServices.sh 4`

## Configuration from MOSIP side

### Update config properties (registration-processor-abis.json)

```text
{
    "abis": [{
        "name": "ABIS1",
        "host": "",
        "port": "",
        "brokerUrl": "tcp://{{ clusters.mz.nodeport_node }}:{{ activemq.nodeport }}",
        "inboundQueueName": "mosip-to-abis1",
        "outboundQueueName": "abis1-to-mosip",
        "pingInboundQueueName": "",
        "pingOutboundQueueName": "",
        "userName": "admin",
        "password": "admin",
        "typeOfQueue": "ACTIVEMQ"
    }]
}
```

### Disable Proxy ABIS

* Remove regproc helm chart: `helm1 delete regproc`
* Remove proxy abis templates:
```text
deployment/sandbox-v2/helm/charts/regproc/templates/proxyabis-dep.yaml
deployment/sandbox-v2/helm/charts/regproc/templates/proxyabis-svc.yaml
```
* Re-run regproc playbook: `an playbooks/regproc.yml`
  