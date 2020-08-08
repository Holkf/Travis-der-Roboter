known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry","Holger","Holk"]

print(len(known_users))

while True:
    print ("Hi! My Name is Travis")
    name = input ("Wie ist dein name? ").strip().capitalize()
    print (name)

    if name in known_users:
        print ("Hello {} wie gehts?".format(name))
        remove = input ("Möchtest du von der Liste gelöscht werden j/n ").lower()

        if remove == "j":
            print (known_users)
            known_users.remove (name)
            print (known_users)
    else:
        print ("Du bist nicht bekannt")
# Na dat läuft doch schon recht gut!