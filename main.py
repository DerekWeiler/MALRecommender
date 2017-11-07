import requests
user = raw_input("Enter you MyAnimeList username: ");
curl = "https://myanimelist.net/malappinfo.php?u={}&status=all".format(user)
from xml.dom import minidom
xmldoc = minidom.parseString(requests.get(curl).text)
malList = []
for node in xmldoc.getElementsByTagName('anime'):
    malList.append(node.toxml())
print malList[1]
