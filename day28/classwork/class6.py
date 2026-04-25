#demande à l'utilisateur de saisir son âge. Vérifie : si l'âge est inférieur à 18, affiche "You are a kid", sinon affiche "You are an Adult"

age=int(input("Enter your age "))

if age<18:
    print("you are a kid")

else:
    print("you are an adult")