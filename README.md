# zoa-ws V0

## Description 
This Flask app reads pdf input to show texte ouput on the web page.
The file conversion to txt is done by a standalone Apache Tika App sets in External Folder

## Manual
### Get docker image
To get the docker image first intall docker and then :

`docker pull gottavianoni/zoa-ws:V0`

### The image will be set in a local container
Then you can run the app :

`docker run gottavianoni/zoa-ws:V0`

### The image will be set in a local container
Then you can acces the app through your web browser :

`locahost:5000/pdf-parser`
or
`192.168.99.100:5000/pdf-parser`



## Ways to acces the Web service
http://localhost:5000/pdf-parser (unix dist / windows with docker CE)
http://192.168.99.100:5000/pdf-parser ( With Docker Toolbox / Windows )

## Dependancies
The Web Service uses :
  -> Python 3
  -> Flask (V. > 0.10.1)
  -> Tika Standalone (V. > 1.18 )
  -> Java OpenJDK (V. 8)


Gottavianoni
