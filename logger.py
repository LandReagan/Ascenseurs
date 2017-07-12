"""
    Ce fichier configure le module standard logging de python.
    Il définit diverses fonctions pour simplifier l'écriture
    et l'utilisation de cette fonctionalité
"""

import logging

FILE_NAME = 'log.txt'
LEVEL = logging.DEBUG


def initialiser(niveau=LEVEL):
    """ Cette fonction initialise le comportement du logger pour le mettre à
    notre goût : les messages prendront la forme :
    [niveau] HH:MM:SS - message
    """
    logging.basicConfig(
        filename=FILE_NAME,
        filemode='w',
        level=LEVEL,
        format='[%(levelname)s] %(asctime)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    logging.info('Démarrage du logger')


def logD(message):
    logging.debug(message)


def logI(message):
    logging.info(message)


def logW(message):
    logging.warning(message)


def logE(message):
    logging.error(message)


def logC(message):
    logging.critical(message)


if __name__ == '__main__':
    initialiser()
    logD('Test de logger niveau DEBUG')
    logI('Test du logger niveau INFO')
    logW('Test du logger niveau WARNING')
    logE('Test du logger niveau ERROR')
    logC('Test du logger niveau CRITICAL')
