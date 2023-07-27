import base64
import mcstatus

mcJ = mcstatus.JavaServer

def main(__x):
    serveur = mcJ.lookup(__x)
    serveurstatus = serveur.status()
    return(serveurstatus)



def players(__x):
    return(__x.players)


def status(__x):
    return(__x.status)

def version(__x):
    return(__x.version)

def favicon(__x):
    __img = __x.icon
    __img = __img.replace('data:image/png;base64,', '')
    __img = base64.b64decode(__img)
    __imgdoc = open('image.png', 'wb')
    __imgdoc.write(__img)
    __imgdoc.close()
    return(__x.icon)

