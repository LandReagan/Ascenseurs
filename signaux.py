""" Ce module contient le dictionnaire des signaux lancés par les différents
    objets de l'application.
    Codage :
    - pm_ : panneau de maintenance

        - cmc_ :    contrôle manuel de la cabine
        - dbh_ :    double bouton haut
        - bh_ :     bouton haut
        - bb_ :     bouton bas
        - dbb_ :    double bouton bas

        - behX_ :    bouton d'étage haut, étage X
        - bebX_ :    bouton d'étage bas, étage X

    - pc_ : panneau cabine

        - eX_ : bounton étage, étage X

    - pp_ : puit

        - cX_ : capteur d'étage, étage X
    """

from logger import logD

signaux = {}

signaux_precedents = {}


# Ajoute liste_signaux à signaux
def ajouter(liste_signaux):
    logD('Ajout signal ' + str(liste_signaux))
    signaux.update(liste_signaux)
    signaux_precedents.update(liste_signaux)


# met à jour une valeur du dictionnaire
def miseAJour(signal, valeur):
    signaux[signal] = valeur
    for k in signaux.keys():
        if signaux[k] is not signaux_precedents[k]:
            logD(str(signal) + ': ' + str(valeur))
            signaux_precedents[k] = signaux[k]


def etat():
    for k in signaux.keys():
        print(k, ': ', signaux[k])


def listeSignauxEtagesBas():
    """ Méthode qui retourne la liste des étages dont le bouton de demande vers
        le bas est activé. Les signaux associés commencent par pm_beb.
    """
    liste = []
    for s in signaux:
        if s[0:6] == 'pm_beb' and signaux[s]:
            liste.append(int(s[6]))
    return liste


def listeSignauxEtagesHaut():
    """ Méthode qui retourne la liste des étages dont le bouton de demande vers
        le haut est activé. Les signaux associés commencent par pm_beh.
    """
    liste = []
    for s in signaux:
        if s[0:6] == 'pm_beh' and signaux[s]:
            liste.append(int(s[6]))
    return liste


def unCapteurEtageEstActif():
    for s in signaux:
        if s[0:4] == 'pp_c':
            if signaux[s]:
                return True
    return False


if __name__ == '__main__':
    ajouter({'signal1': False, 'signal2': True, 'signal3': False})
    etat()
    miseAJour('signal1', True)
    etat()
