#!/usr/bin/python3
import glob


class SondeTemp(object):
    """Lecture de sonde(s),
renvoie les adresse (liste), le fichier brut (liste) et la valeur des sondes (liste)"""
    
    def adrs_sonde(self):
        """renvoi toutes les adrs de sondes sous liste (str)"""
        adrs =[]
        Lrep_sonde = glob.glob("/sys/bus/w1/devices/" + "28*")
        if len(Lrep_sonde) == 0:
            print("Led.defaut_sonde()")
        else:
            for F in Lrep_sonde:
                adrs.append(F+"/w1_slave")
        return adrs
    

    def lire_F_brut(self):
        """renvoi le contenu des fichier sonde sous forme de (str)"""
        Brut =[]
        for A in  self.adrs_sonde():
            with open(A, 'r') as F:
                Brut+=F.readlines()
        return Brut
    
    def TempC(self):
        """revoie les valeurs de sonde sous liste(float)"""
        index = 0
        Temp =[]
        Chain = ''.join(self.lire_F_brut())
        while index < len(Chain):
            index = Chain.find('t=', index)
            if index == -1:
                break
            Temp.append(Chain[index+2:index+7])
            index +=2
        return Temp
        


#Test renvois chaques argument
if __name__ =='__main__':


    toto = SondeTemp()
    print(toto.adrs_sonde())
    print(toto.lire_F_brut())

    print(toto.TempC())

