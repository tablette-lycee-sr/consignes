def verifA(score):
  print("03-1. A")
  try:
    a = score
  except: 
    print("Il n'y a plus de variable portant le nom de `score`. Vous devez la déclarer à nouveau...")
  else:
    if score == None:
      print("Vous n'avez pas affecté de valeur à la variable `score`. Essayez à nouveau...")
    elif isinstance(score, int): 
      print("Bravo ! Vous avez affecté un nombre entier à la variable score. Vous lui avez donné `"+ str(score)+"` comme valeur.")
    else:
      print("La valeur que vous avez affectée ne correspond pas au type de la variable `score`. Vous devez lui affecter un nombre entier. Essayez à nouveau...")

def erreurA():
  print("03-1. A")
  print("Il n'y a plus de variable nommée `score`. Il faut la déclarer à nouveau...")

if __name__ == '__main__':
  pass
  # Le code ici ne s'exécutera que si le module est exécuté directement

