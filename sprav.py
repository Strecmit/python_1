print("***ТЕЛЕФОННЫЙ СПРАВОЧНИК 1.0***")

def menu():
    print("1-ПОИСК")
    print("2-НОВЫЙ КОНТАКТ")
    print("3-РЕДАКТОР")
    print("4-ВЫХОД")
    vybor = input("ВАШ ВЫБОР >")

    return(vybor)

def search():
    poisk = input("ВВЕДИТЕ ФАМИЛИЮ/ИМЯ/ОТЧЕСТВО/№ ТЕЛЕФОНА >")
    with open("sprav.txt","a", encoding="utf-8") as file:
        lines = 0
        words1 = 0
        for line in file:
            if poisk in line:
                print(line)
    return()

def new_c():
    
        
        


