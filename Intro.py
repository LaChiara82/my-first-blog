partecipante1={'nome':'chiara','cognome':'bruschi','data_nascita':[15,12,1990]}
#print(partecipante1)
#print(len(partecipante1))
partecipante2={'nome':'chiara','cognome':'bruschi','data_nascita':[20,6,1990]}
anno1=partecipante1['data_nascita'][2]
#print(anno1)
anno2=partecipante2['data_nascita'][2]
mese1=partecipante1['data_nascita'][1]
mese2=partecipante2['data_nascita'][1]
giorno1=partecipante1['data_nascita'][0]
giorno2=partecipante2['data_nascita'][0]
#print(anno2)
#print(anno1>anno2)
#print(anno1<anno2)
if anno1==anno2 and mese1==mese2 and giorno1==giorno2:
    print('I partecipanti sono coetanei')
elif anno1==anno2 and mese1<mese2:
    print('Partecipante 1 è più vecchio di Partecipante 2')
elif anno1<anno2:
    print('Partecipante 1 è più vecchio di Partecipante 2')
else:
    print('Partecipante 1 è più giovane di Partecipante 2')
