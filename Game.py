import time
import sys
import os
import webbrowser as web
import smtplib
import random

print('=> Welcome')
while True:
    reg_user = input('Kullanıcı Adı:') #REGİSTER....
    reg_pass = input('Şifre:')
    reg_name = input('Name:')
    time.sleep(5)
    print('Nickname = ' , reg_user)
    print('Password =  ' , reg_pass)
    print('Name = ' , reg_name)
    time.sleep(3)

    while True:
        log_user = input('Nickname:')
        log_pass = input('Password:')

        if log_user ==  reg_user and log_pass == reg_pass:
            print('System Opened for' , reg_name)
            while True:
                print('OS =>' , os.name)
                print('Admin => ', reg_name)
                print('Company Name => Dominus')


                money = 1000
                motivation = 100
                dominus_money = 1000000
                computer_price = 500
                comp_have = 0
                progremmer_price = 750
                programmer = 0


                print('Money:' , money , '$')
                print('Motivation:' , motivation)
                print('Company Money:', dominus_money , '$')

                time.sleep(3)
                print('Buy Computers For your Dominus Piratiaes YES/NO')
                buy = input(' =>')

                if buy =='YES'
                    many = input('How Many:')

                    if many ==many:
                        dominus_money - many * computer_price
                        comp_have + many 

                        print('Computers:' , comp_have)
                        print('Company Money Remain:', dominus_money)
                        while True:

                        prog = input('How many buy programmer:')

                        if prog < many:
                            programmer + prog
                            dominus_money - programmer_price * prog

                            print('Company Money Remain:' , dominus_money)
                            print('Programmers:' , programmer)

                            class aylik_kazanc:
                                my_maas = 3000
                                programmers_maas = 950

                            print('Maaş Günü....')

                            money + aylik_kazanc.my_maas
                            dominus_money - aylik_kazanc.programmers_maas * prog

                            print('Company Money Remain:' , dominus_money)

                            dominus_money + 87282

                            print('Company Money Updated:' , dominus_money)

                            time.sleep(3)
                            while True:

                            gmail_address = 'canuhelpme1827@gmail.com'
                            gmail_password = 'canuhelpme'

                            sent_mail_address = input('=>')
                            konu = input('Konu:')
                            mesaj = 'random.randint(100000,999999))'

                            email_text = """
                            From: {}
                            To: {}
                            Subject: {}
                            {}
                            """ .format(gmail_address , sent_mail_address , konu , mesaj)
                            try:
                                server = smtplib.SMTP('smtp.gmail.com:587')
                                server.starttls()
                                server.login(gmail_address , gmail_password)
                                server.sendmail(gmail_address , sent_mail_address , email_text)
                                server.close()
                                print('Email Gönderildi , Lütfen Epostanınızı KOntrol Ediniz')

                                time.sleep(5)

                                correct_account = input('Doğrulama Kodunu Giriniz:')
                                if correct_account == mesaj:
                                    print('Succesful')

                                    time.sleep(4)
                                    print('Maaş Günü...')

                                    aylik_kazanc.my_maas + 1467
                                    money + aylik_kazanc.my_maas
                                    dominus_money - aylik_kazanc.programmers_maas * programmer

                                    print('Your Money:' , money)
                                    print('Company Money Remain:', dominus_money)

                                    dominus_money + 'random.randint(100000 ,222222 ))'
                                    print('Company Money Updated:' , dominus_money)

                                    time.sleep(2)

                                    print('CRACKİNG GAME w/Reverse Engineering')

                                    def quicksort(arr):
                                        if len(arr) <= 1:
                                            return arr
                                        pivot = arr[len(arr) // 2]
                                        left = [x for x in arr if x < pivot]
                                        middle = [x for x in arr if x == pivot]
                                        right = [x for x in arr if x > pivot]
                                        return quicksort(left) + middle + quicksort(right)

                                    print(quicksort([3,6,8,10,1,2,1]))

                                    time.sleep(2)

                                    print('STOP STOP !!!!!!')

                                    zaman = time.time()
                                    vakit = time.localtime(zaman)
                                    d = vakit[5]
                                    kontrol='devam'

                                    while kontrol !='dur':
                                        while ((time.localtime(time.time()))[5]) == (int(d)-1):
                                            print('DDOS Fatal Error 404')
                                            kontrol='dur'

                                            time.sleep(5)

                                            break

                                    print('')

                                            

                                    



                                else:
                                    print('Doğrulama Kodu Hatalı...')
                            except:
                                print('Bir Hata Oluştu Lütfen Tekrar Deneyiniz')
                        else:
                            print(many , 'den falza alamazsın')
        else:
            print('Try Again' , reg_name)
