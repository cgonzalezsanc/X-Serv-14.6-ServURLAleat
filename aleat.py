import webapp
import random


class otroServidor(webapp.webApp):

    def process(self, parsedRequest):

        rand = random.randint(1, 100000000)
        htmlAnswer = '<html><body><h1>Hola.<a href="' + str(rand)
        htmlAnswer = htmlAnswer + '">Dame otra</a></h1></body></html>'
        return("200 OK", htmlAnswer)


if __name__ == "__main__":
    serv = otroServidor("localhost", 1240)
