print("***ТЕЛЕФОННЫЙ СПРАВОЧНИК 1.0***")

def menu():
    print("1-ПОИСК")
    print("2-ВЕСЬ СПРАВОЧНИК")
    print("3-РЕДАКТОР")
    print("4-ВЫХОД")
    vybor = int(input("ВАШ ВЫБОР >"))

    return(vybor)

def search():
    poisk = input("ВВЕДИТЕ ФАМИЛИЮ/ИМЯ/ОТЧЕСТВО/№ ТЕЛЕФОНА >")
    with open("sprav.txt","a", encoding="utf-8") as file:
        lines = 0
        words1 = 0
        for line in file:
            if poisk in line:
                print(line)
    input("ДЛЯ ВЫХОДА В МЕНЮ НАЖМИТЕ ЛЮБУЮ КЛАВИШУ >")
    return()

def all_phb():
    empty_line = 0
    with open("sprav.txt", "r", encoding="utf-8") as file1:
        for line in file1:
            print(line.strip())
    input("ДЛЯ ВЫХОДА В МЕНЮ НАЖМИТЕ ЛЮБУЮ КЛАВИШУ >")
    return()

def redactor():
    print("1-НОВЫЙ КОНТАКТ")
    print("2-ИЗМЕНИТЬ КОНТАКТ")
    print("3-УДАЛИТЬ КОНТАКТ")
    vybor_red = int(input("ВАШ ВЫБОР >"))
    if vybor_red == 1:
        name_s = input("ВВЕДИТЕ ФАМИЛИЮ >")
        name = input("ВВЕДИТЕ ИМЯ >")
        name_f = input("ВВЕДИТЕ ОТЧЕСТВО >")
        phb_num = input("ВВЕДИТЕ НОМЕР ТЕЛЕФОНА >")
        with open("sprav.txt", "a", encoding="utf-8") as file1:
            file1.write(f"{name_s.upper()}\t{name.upper()}\t{name_f.upper()}\t{phb_num}\n")
        print("КОНТАКТ ДОБАВЛЕН")
        input("ДЛЯ ВЫХОДА В МЕНЮ НАЖМИТЕ ЛЮБУЮ КЛАВИШУ >")
        
while True:
    menu_vub = menu()

    if menu_vub == 1:
        search()
    elif menu_vub == 2:
        all_phb()
    elif menu_vub==3:
        redactor()
    elif menu_vub==4:
        exit()
    else:
        print("НЕВЕРНЫЙ ВВОД!")
        menu()

        

    
        
        


