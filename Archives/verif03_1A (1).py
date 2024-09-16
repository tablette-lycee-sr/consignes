def verifA(score):
  print("03-1. A")
  try:
    a = 100
  except: 
    print("Il n'y a plus de variable portant le nom de `score`. Vous devez la déclarer à nouveau...")
  else:
    if score == None:
      print("Vous n'avez pas affecté de valeur à la variable `score`. Essayez à nouveau...")
    elif ((not isinstance(score, int)) or (score != 100)): 
      print("Vous avez affecté une valeur à la variable score. Mais vous lui avez donné `" + str(score) + "`. Essayez à nouveau...")
    else:
      print("Bravo ! Vous avez affecté la valeur attendue à la variable `score`.")

def erreurA():
  print("03-1. A")
  print("Il n'y a plus de variable nommée `score`. Il faut la déclarer à nouveau...")

if __name__ == '__main__':
  pass
  # Le code ici ne s'exécutera que si le module est exécuté directement

