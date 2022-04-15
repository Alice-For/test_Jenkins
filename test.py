#import os

def fonction_test() :
    try :
        print("ceci est un test pour voir comment marche Docker")
        a = (True, "abc", 42)
        b = [True, "abc", 42]
        print("Liste initiale : ", b)
        print("1er élément du tuple : ", a[0])
        print("1er élément de la liste : ", b[0])

        b.append("hello there")

        print("Liste modifiée : ", b)

    except Exception as err :
        print("une erreur est survenue : ", err)
       
    finally : 
        print("fin du test")
        #os.system("pause")
    

fonction_test()