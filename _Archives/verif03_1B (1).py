def verifB(invisible):
  print("03-1. B")
  try:
    b = invisible
  except: 
    print("Il n'y a plus de variable portant le nom de `invisible`. Vous devez la déclarer à nouveau...")
  else:
    if invisible == True:
      print("Bravo ! Vous avez affecté une nouvelle valeur à la variable `invisible`. Vous lui avez donné `"+ str(invisible)+"` comme valeur.")
    else:
      print("La valeur que vous avez affecté à la variable `invisible` n'est pas celle qui est attendue. Vous devez affecter une valeur bouléenne (Vrai ou Faux. En Anglais, T... ou False). Essayez à nouveau...")


def erreurB():
  print("03-1. B")
  print("Il n'y a plus de variable nommée `invisible`. Il faut la déclarer à nouveau...")

if __name__ == '__main__':
  pass
  # Le code ici ne s'exécutera que si le module est exécuté directement

