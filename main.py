import json
import datetime
with open("bank.json", encoding='utf-8') as ff:
 p = json.load(ff)

#функция операций снять/положить
def operation(n, count, what_do):
 def write_in_bank():
  now_time=datetime.datetime.now()
  string_time=f"{now_time.day}.{now_time.month}.{now_time.year} {now_time.hour}:{now_time.minute}"
  p[n] = [string_time,count,what_do]
  with open("bank.json", 'w', encoding='utf-8') as f:
   json.dump(p, f, ensure_ascii=False, indent=4)
 #условия, если снять - то снять, положить - то положить
 if what_do == "снять":
  p["balance"] -= int(count)
  write_in_bank()
 if what_do == "положить":
  p["balance"] += int(count)
  write_in_bank()

#функция - чтобы узнать баланс, либо посмотреть историю транзакций
def read():
 print(f"Ваш баланс: $",p["balance"])
 answer = input("Вы хотите посмотреть историю операций? Y/N\n")
 if answer == "Y":
  for i in p:
   if i != "balance":
    print(str(i)+". Время:", p[i][0],"| Сумма операции: $"+str(p[i][1])+"| Тип операции:", p[i][2])
what = "1"
while int(what) != 0:
 print(what)
 if int(what) == 1:
  what = input("\033[33m {}" .format("Здравствуйте! Выберете тип операции\n===\nпосмотреть баланс - 1 \nснять/положить - 2 \nвыход - 0\n"))


 if not what.isdigit():
  print("\033[31m {}" .format("Ошибка! используйте только цифры"))

 if int(what) == 1:
  read()
  what_read = input("Выйти из просмотра - 1 \nВыйти из банка - 0\n")
  what = what_read
 if int(what) == 2:
  n_ = len(p)
  what_do_ = input("Какую операцию вы хотите выполнить?\nСнять - 1\nПоложить - 2\nВыйти - 0\n")

  if not what_do_.isdigit():
   print("\033[31m {}".format("Ошибка ввода"))
  else:
   if int(what_do_) == 1:

    count_ = input("Какую сумму снять со счёта? \n")
    if int(count_) <= 0:
     print("Ошибка. Минимальная транзакция - от $1")
    else:
     if int(count_) <= p["balance"]:
      operation(n_,count_,"снять")
      print("\033[31m{}".format("Cо счёта снято $"+str(count_)), "\033[33m {}" .format("\nТекущий баланс: $"+str(p["balance"])))
     else:
      print("Недостаточно средств. У вас доступно $"+str(p["balance"]))
   if int(what_do_) == 2:
    count_ = input("Какую сумму положить на счёт? \n")
    operation(n_,count_,"положить")
    print("\033[32m{}".format("На счёт добавлено $"+str(count_)), "\033[33m {}" .format("\nТекущий баланс: $"+str(p["balance"])))
   what_read = input("вернуться на главную - 1 \nпродолжить операции - 2 \nВыйти из банка - 0\n")
   if what_read in ["0","1","2"]:
    what = what_read
   if int(what_do_) == 0:
    what = 0
print("Спасибо что пользуетесь этим консольным банком.")