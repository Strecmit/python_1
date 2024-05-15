print("***ТЕЛЕФОННЫЙ СПРАВОЧНИК 1.0***")

def menu():
    print("1-ПОИСК")
    print("2-ВЕСЬ СПРАВОЧНИК")
    print("3-РЕДАКТОР")
    print("4-ВЫХОД")
    vybor = int(input("ВАШ ВЫБОР >"))

    return(vybor)

def search():
    with open("sprav.txt","r", encoding="utf-8") as file:
        povt_zapros = 1
        while int(povt_zapros) !=0:
            poisk = input("ВВЕДИТЕ ФАМИЛИЮ/ИМЯ/ОТЧЕСТВО/№ ТЕЛЕФОНА >")
            i=0
            for line in file:
                if poisk.upper() in line:
                    print(line)
                    i+=1
            if i==0:
                print("ЗАПИСЬ НЕ НАЙДЕНА")
            povt_zapros = input("ПОВТОРИТЬ ПОИСК? 1-ДА  0-НЕТ>")
            file.seek(0,0)
                
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
        input_num = input("ВВЕДИТЕ НОМЕР ТЕЛЕФОНА >")
        while input_num.isnumeric()!=1:
            print("НЕВЕРНЫЙ ВВОД НОМЕРА")
            input_num = input("ВВЕДИТЕ НОМЕР ТЕЛЕФОНА >")
        phb_num = int(input_num)


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

        

    
        
        


