def verifC(nomDuJoueur):
  print("03-1. C")
  try:
    c = nomDuJoueur
  except:
    print(
      "Vous n'avez pas créé la variable avec le nom attendu. Essayez à nouveau..."
    )
  else:
    msg = "Vous avez créé une variable avec le nom attendu. "
    if str(nomDuJoueur) == "":
      msg = msg + "Mais vous ne lui avez pas affecté de valeur. Essayez à nouveau..."
    elif isinstance(nomDuJoueur, str): 
      msg = msg + "Bravo ! Vous lui avez donné `" + str(
        nomDuJoueur) + "` comme valeur."
    else:
      msg = msg + "Mais vous ne lui avez pas affecté une valeur de type chaîne de caractères. Essayez à nouveau..."
    print(msg)


def erreurC():
  print("03-1. C")
  print(
    "Vous n'avez pas créé la variable avec le nom attendu. Essayez à nouveau..."
  )


if __name__ == '__main__':
  pass
  # Le code ici ne s'exécutera que si le module est exécuté directement
