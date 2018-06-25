# zoa-ws V0

## Description 
This Flask app reads pdf input to show texte ouput on the web page.
The file conversion to txt is done by a standalone Apache Tika App sets in External Folder

## Input
The file input is a pdf document sets antwhere in your local machine.

## Output
The ouput is directly print on the web page

## Ways to acces the Web service
http://localhost:5000/pdf-parser (unix dist / windows with docker CE)
http://localhost:5000/pdf-parser (unix dist / windows with docker CE)

##Dependancies
The Web Service uses :
  -> Python 3
  -> Flask (V. > 0.10.1)
  -> Tika Standalone (V. > 1.18 )
  -> Java OpenJDK (V. 8)


Gottavianoni
