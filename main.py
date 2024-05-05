from random import randint
from time import sleep
from time import time
import webbrowser
import re
import math
print('Powered by Algoritmika and Nikita Pokhodnya\n\nUPDATE - Stopwatch can now remember time!')
print('~'* 60)
print('ОБНОВЛЕНИЕ - Новые крестики-нолики!\n')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_menu_ru():
    print('Вот что я умею:')
    print('▷ 1 - Мини-игра "Угадай число"')
    print('▷ 2 - Порекомендовать фильм')
    print('▷ 3 - Посчитать скорость набора текста')
    print('▷ 4 - Открыть веб-сайт')
    print('▷ 5 - Открыть калькулятор')
    print('▷ 6 - Анализ текста')
    print('▷ 7 - Рандомайзер ')
    print('▷ 8 - Игра "Крестики-Нолики"')
    print('▷ 9 - Прогноз погоды')
    print('▷ 10 - Новости мира "Алгоритмики"')
    print('▷ 11 - Секундомер')
    print('▷ 12 - Мини-игра "Гений математики" BETA ')
    print('▷ 13 - Рекомендации игр BETA ')
    print('▷ 14 - Открыть случайную статью в Википедии ')
    print('(new!) ▷ 15 - Посчитать средний балл по школьному предмету ')
    '''print('▷ 16 - Генератор паролей')'''
    print('▷ @ - Найти информацию в интернете')
    print('▷ ? - Напомнить управление')
    print('▷ 0 - Остановиться')
    print('~'*64)
    print('Можешь ввести название функции или её номер, я всё равно пойму тебя)')
    print('~'*64)
def print_menu_eu():
    print ("Here's what I can do:")
    print ('▷ 1 - "Guess the number" mini-game')
    print ('▷ 2 - Recommend a movie')
    print ('▷ 3 - Calculate the typing speed')
    print ('▷ 4 - Open website')
    print ('▷ 5 - Open calculator')
    print ('▷ 6 - Analyze text')
    print ('▷ 7 - Randomizer')
    print ('▷ 8 - "The Tic Tac Toe" Game')
    print('▷ 9 - Weather forecast')
    print ('▷ 10 - News of the world "Algorithmics" ')
    print('(new) ▷ 11 - Stopwatch')
    print ('▷ @ - Find information on the internet')
    print ('▷ ? - Remind control')
    print ('▷ 0 - Stop')
    print ('Communicate with numbers only!')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
language = input('Hi! Please enter your language first!\nПривет! Для начала введи свой язык!\n\n▷ RUS - Russian (Русский)\n▷ ENG - English (Английский)\n\n').lower()
while True:
    if language == 'rus' or language == 'рус' or language == 'русский' or language == 'russian' or language == 'рашн':
        language = 'rus'
        break
    elif language == 'eng' or language == 'инг' or language == 'английский' or language == 'english' or language == 'инглиш':
        language = 'eng'
        break
    else:
        language = input('Please enter your language!\nПожалуйста, введите свой язык!\n\n▷ RUS - Russian (Русский)\n▷ ENG - English (Английский)\n\n').lower()
print('~'*62,'\n')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
yandex = 'https://yandex.ru/search/?text='         
google = 'https://google.ru/search?q='     
DuckDuckGo = 'https://duckduckgo.com/?q='
bing = 'https://bing.com/?q='
ecosia = 'https://www.ecosia.org/search?q='
yahoo = 'https://search.yahoo.com/search?p='
mailru = 'https://go.mail.ru/search?q='
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if language == 'rus':
    print('🤪 Привет! Я твой виртуальный помощник.')
    print('Меня создал Никита Походня!')
    print('Меня зовут Атлас! 🤓')
    name = input('🧐 А как зовут вас? 🧐')
    '''while name.count(' ') >= 2:
        print('Имя введенo некоректно! Введите только имя или псевдоним!')
        name = input('🧐 А как зовут вас? 🧐')'''
    print('Приятно познакомиться,',name,'! 😁')  
    rec_browser = input('Какой браузер ты предпочитаешь? 😊').lower()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    yandex_eng = rec_browser.find('yandex')
    yandex_ru = rec_browser.find('яндекс')
    google_ru = rec_browser.find('гугл')
    google_eng = rec_browser.find('google')
    DuckDuckGo_eng_classic = rec_browser.find('duckduckgo')
    DuckDuckGo_ru_classic = rec_browser.find('дакдакго')
    DuckDuckGo_ru_classic_correct = rec_browser.find('дакдакгоу')
    DuckDuckGo_ru = rec_browser.find('дак дак го')
    DuckDuckGo_ru_correct = rec_browser.find('дак дак гоу')
    DuckDuckGo_eng = rec_browser.find('duck duck go')
    bing_ru = rec_browser.find('бинг')
    bing_eng = rec_browser.find('bing')
    ecosia_ru = rec_browser.find('экозия')
    ecosia_eng = rec_browser.find('ecosia')
    yahoo_ru = rec_browser.find('яху')
    yahoo_eng = rec_browser.find('yahoo')
    mailru_rus = rec_browser.find('майл')
    mailru_rus_2 = rec_browser.find('мэйл')
    mailru_eng_ru = rec_browser.find('mail')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if yandex_eng != -1 or yandex_ru != -1:
        print('О, русский браузер?) Уважаю!')
        browser = yandex
    elif DuckDuckGo_eng_classic != -1 or DuckDuckGo_ru != -1 or DuckDuckGo_ru_classic != -1 or DuckDuckGo_ru_classic_correct != -1 or DuckDuckGo_ru_correct != -1 or DuckDuckGo_eng != -1: 
        print('Мммм... Любишь конфиденциальность ?)')
        browser = DuckDuckGo
    elif bing_ru != -1 or bing_eng != -1:
        print('Майкрософт, так Майкрософт)')
        browser = bing
    elif ecosia_ru != -1 or ecosia_eng != -1:
        print('Я тоже за экологию! Респект 😎')
        browser = ecosia
    elif yahoo_eng != -1 or yahoo_ru != -1:
        print('Настоящий олд!')
        browser = yahoo
    elif mailru_eng_ru != -1 or mailru_rus != -1 or mailru_rus_2 != -1:
        print('Воооу, давно я таких людей не встречал!')
        browser = mailru
    else:
        print('Спасибо за честный ответ!')
        browser = google
    print_menu_ru()
    q = input('Как я могу тебе помочь?').lower()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    while q != '0':
        if q == '1' or "угадай" in q:
            mode = input('Кто будет угадывать? (1 - Вы / 2 - Компьютер)')
            if mode == '1':
                print('Ты хочешь ввести максимальное число сам или выбрать уровень сложности?')
                print('1 - Ввести самому!')
                print('2 - Выбрать из уровней сложности!')
                q_rand_num = int(input('Выбирайте:'))
                if q_rand_num == 1:
                    num_play = int(input('Прошу, вводите:'))
                elif q_rand_num == 2:
                    print('1 - Легко (5 макс. число)')
                    print('2 - Нормально (10 макс. число)')
                    print('3 - Сложно (30 макс. число)')
                    num_play_q = int(input('Прошу, выбирайте:'))
                    if num_play_q == 1:
                        num_play = 5
                    elif num_play_q == 2:
                        num_play = 10
                    elif num_play_q == 3:
                        num_play = 30
                num_play_a = randint(1, num_play)
                print('Угадай загаданое мною число от 1 до',num_play,'!')
                print('Я буду подсказывать вам, говоря, что моё число больше(>) или меньше(<) вашего числа!')
                player_num = int(input('Вводите число:'))
                steps = 1
                while player_num != num_play_a:
                    if player_num < num_play_a:
                        print('Загаданое мною число >',player_num)
                        steps += 1
                        player_num = int(input('Вводите число:'))
                    elif player_num > num_play_a:
                        steps += 1
                        print('Загаданое мною число <',player_num)
                        player_num = int(input('Вводите число:'))
                print('Вы угадали число и выиграли!')
                print('Число угадано с',steps,'попытки!')
                print('~'*62,'\n')
            elif mode == '2':
                steps = 0
                arr = range(1, 102)
                print("Загадай любое число от 1 до 100")
                input('Нажми "Enter" когда будешь готов!')
                low = 0
                high = len(arr)-1
                while low < high:
                    steps += 1
                    middle = (low+high) // 2
                    ans_form = randint(1,5)
                    if ans_form == 1:
                        print('Это число - '+str(arr[middle])+'?')
                    elif ans_form == 2:
                        print('Быть может это - '+str(arr[middle])+'?')
                    elif ans_form == 3:
                        print('Я думаю это - '+str(arr[middle])+'?')
                    elif ans_form == 4:
                        print('Я уверен, что это - '+str(arr[middle])+'?')
                    elif ans_form == 5:
                        print('Может, тогда - '+str(arr[middle])+'?')
                    num_search = input('(< - меньше / > - больше / = - равно)')
                    if num_search == "=":
                        print(f"Число отгадано с {steps} попыток!")
                        break
                    elif num_search == "<":
                        high = middle
                    elif num_search == ">":
                        low = middle
                    if num_search == ">" and high == 100 and low == 99:
                        low = high
                        if low == high:
                            print("Загаданное тобою число < 1 / > 100 / ты неправильно поставил знаки!")
                            break
            print('~'*62)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '2' or 'фильм' in q:
            print('1 - комедии')
            print('2 - триллеры')
            print('3 - детектив')
            print('4 - ужасы')
            print('5 - романтические')
            catag = input('Какой жанр вы предпочитаете?')
            if catag == '1':
                films_comedy = ['Операция «Ы» и другие приключения Шурика','Тупой и ещё тупее','Иван Васильевич меняет профессию','Бриллиантовая рука','Один дома','Назад в будущее','Третий лишний']
                film_comedy_rand = randint(0,len(films_comedy)-1)
                print(f'Я советую посмотреть: {films_comedy[film_comedy_rand]}')
            elif catag == '2':
                films_triller = ['Побег из Претории','Амнезия','Гнев человеческий','Никто','Взаперти','Кто не спрятался']
                film_triller_rand = randint(0,len(films_triller)-1)
                print(f'Я советую посмотреть: {films_triller[film_triller_rand]}')
            elif catag == '3':
                films_d = ['Комната желаний','Поиск','Энола Холмс']
                film_d_rand = randint(0,len(films_d)-1)
                print(f'Посмотрите: {films_d[film_d_rand]}')
            elif catag == '4':
                films_scream = ['Поворот не туда','Заклятие 3','Греттель и Гензель']
                film_scream_rand = randint(0,len(films_scream)-1)
                print(f'Есть хороший фильм - {films_scream[film_scream_rand]}')
            elif catag == '5':
                films_l = ['Эмма','Жизнь за год','365 дней']
                film_l_rand = randint(0,len(films_l)-1)
                print(f'Советую: {films_l[film_l_rand]}')
            print('~'*62,'\n')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '3' or 'скорост' in q:
            input('Нажмите "Enter", когда будете готовы писать!!')
            start_time = time()
            play_phrase = input('Напишите отзыв обо мне!')
            end_time = time()
            total_time = end_time - start_time
            symbols = len(play_phrase)
            print_speed = round( symbols/ total_time, 2)
            print('\n','~'*62)
            print('* Скорость печати этого текста:', round(total_time, 2),'секунд!')       
            print('* Всего в этом тексте:',symbols,'символов!')
            print('* Ваша скорость:', print_speed,'символа в секунду или',print_speed*60,'символов в минуту!')
            if print_speed * 60 < 150:
                lvl_print_speed = 'Новичок'
            elif print_speed * 60 >= 150 and print_speed*60 < 250:
                lvl_print_speed = 'Нормальный пользователь'
            elif print_speed * 60 >= 250 and print_speed*60 < 400:
                lvl_print_speed = 'Профи'
            elif print_speed*60 >= 400 and print_speed*60 < 1080:
                lvl_print_speed = 'Уникум'
            elif print_speed*60 >= 1080:
                lvl_print_speed = 'Чтооооо?!! Это мировой рекорд! Делай скриншот!!!'
            print('* Ваш уровень:',lvl_print_speed,'!')
            print('~'*62,'\n')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '?' or 'управление' in q:
            print('🤪 Привет! Я чат-бот.')
            print('Меня зовут Атлас! 🤓')
            print('А вас ,видимо,',name,'😅')    
            print_menu_ru()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '4' or 'сайт' in q:
            print('Внимание! Сайты открываются в браузере по умолчанию!')
            print('Какой сайт вы хотите открыть?')
            print('~'*64)
            print('* ВК\n* YouTube\n* Steam\n* Apple\n* Start\n* ТНТ\n* СТС')
            print('~'*64)
            site = input('Введи название из предложеных:').lower()
            if site == 'youtube' or site == 'ютуб' or site == 'ютюб':
                print('Секунду...')
                sleep(1)
                webbrowser.open('https://www.youtube.com')
            elif site == 'вк' or site == 'вконтакте' or site == 'в контакте':
                print('Секунду...')
                sleep(1)
                webbrowser.open('https://vk.com')
            elif site == 'стим' or site == 'steam':
                print('Секунду...')
                sleep(1)
                webbrowser.open('https://store.steampowered.com/?l=russian')
            elif site == 'apple' or site == 'эпл' or site == 'эппл':
                print('Секунду...')
                sleep(1)
                webbrowser.open('https://www.apple.com/ru/')
            elif site == 'start' or site == 'старт':
                print('Секунду...')
                sleep(1)
                webbrowser.open('https://start.ru')
            elif site == 'тнт':
                print('Секунду...')
                sleep(1)
                webbrowser.open('https://tnt-online.ru')
            elif site == 'стс':
                print('Секунду...')
                sleep(1)
                webbrowser.open('https://ctc.ru')
            else:
                print('Прости! 🥺 Я не знаю такого сайта!')
                q_search = input('Искать? (да/нет)').lower()
                if q_search == 'да':
                    webbrowser.open_new_tab(browser + site)
                else:
                    print('Не хотите, как хотите)')
            print('~'*62,'\n')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '5' or 'калькулятор' in q:
            action = input('\nВыберите действие: \n - вычитание ;\n + cложение ;\n/ деление ;\n * умножение;\n // деление без остатка;\n % нахoждение остатка от деления;\n ** возведение в степень;\n$  нахождение квадратного корня от числа;\n! - нахождение факториала числа;\nlog - нахождение лагорифма числа;\nsum - найти сумму всех элементов в списке\narifm - нахождение µ всех чисел в списке\nP - найти периметр фигуры\nS - найти площадь фигуры\ncos - найти косинус по аргументу x\nsin - найти синус по аргументу x\ntan - найти тангенс по аргументу x').lower()
            if action == '-':
                num1 = float(input('\nВведите уменььшаемое (десятичную дробь через точку!):'))
                num2 = float(input('\nВведите вычитаемое (десятичную дробь через точку!):'))
                print('Ответ:',num1, '-', num2, '=', num1-num2 )
                print('~'*62)
            elif action == '*':
                num1 = float(input('\nВведите первый множитель (десятичную дробь через точку!):'))
                num2 = float(input('\nВведите второй множитель (десятичную дробь через точку!):'))
                print('\n','Ответ:',num1, '*', num2, '=', num1*num2)
                print('~'*62)
            elif action == '/':
                num1 = float(input('\nВведите делимое (десятичную дробь через точку!):'))
                num2 = float(input('\nВведите делитель (десятичную дробь через точку!):'))
                print('\n','Ответ:',num1, '÷', num2, '=', num1/num2)
                print('~'*62)
            elif action == '+':
                num1 = float(input('\nВведите первое слогаемое (десятичную дробь через точку!):'))
                num2 = float(input('\nВведите второе слогаемое (десятичную дробь через точку!):'))
                print('\n','Ответ:',num1, '+', num2, '=', num1+num2)
                print('~'*62)
            elif action == '//':
                num1 = float(input('\nВведите делимое (десятичную дробь через точку!):'))
                num2 = float(input('\nВведите делитель (десятичную дробь через точку!):'))
                print('\n','Ответ без остатка: ',num1, '÷', num2, '=', num1//num2)
                print('~'*62)
            elif action == '**':
                num1 = float(input('\nВведите число для возведения в степень (десятичную дробь через точку!):'))
                num2 = float(input('\nВведите в какую степень возвести (десятичную дробь через точку!):'))
                print('\n','Ответ:',num1,'^',num2, '=', num1**num2)
                print('~'*62)
            elif action == '%':
                num1 = float(input('\nВведите делимое (десятичную дробь через точку!):'))
                num2 = float(input('\nВведите делитель (десятичную дробь через точку!):'))
                print('\n','Ответ: Остаток от',num1, '÷', num2, '=', num1%num2)
                print('~'*62)
            elif action == '$':
                num1 = float(input('\nВведите число для нахождения квадратного корня (десятичную дробь через точку!):'))
                sqrt = math.sqrt(num1)
                print('\n','Ответ: ⎷'+str(num1)+ ' = ±'+ str(sqrt))
                print('~'*62)
            elif action =='!':
                num1 = float(input('\nВведите число для нахождения факториала (десятичную дробь через точку!):'))
                print('Ответ: !'+str(num1)+' =',math.factorial(num1))
                print('~'*62)
            elif action =='log':
                num1 = float(input('\nВведите число для нахождения логарифма (десятичную дробь через точку!):'))
                base = float(input('Введите основание:'))
                print('Ответ: log '+str(num1)+' c основанием',base,'=',math.log(num1,base))
                print('~'*62)
            elif action =='sum':
                numbers = []
                num_list = input('Вводите числа и заполняйте список (stop - остановиться)')
                while num_list != 'stop':
                    numbers.append(float(num_list))
                    num_list = input('Вводите числа и заполняйте список (stop - остановиться)')
                print('\nОтвет: Сумма всех элементов в списке',numbers,'=',math.fsum(numbers))
                print('~'*62)
            elif action =='arifm':
                numbers = []
                num_list = input('Вводите числа и заполняйте список (stop - остановиться)')
                while num_list != 'stop':
                    numbers.append(float(num_list))
                    num_list = input('Вводите числа и заполняйте список (stop - остановиться)')
                print('\nОтвет: µ всех элементов в списке',numbers,'=',math.fsum(numbers)/len(numbers))
                print('~'*62)
            elif action == 'p':
                figure = input('Введите название фигуры (пример: треугольник)').lower()
                if figure == 'треугольник':
                    len_1 = float(input('Введите длину 1 стороны:'))
                    len_2 = float(input('Введите длину 2 стороны:'))
                    len_3 = float(input('Введите длину 3 стороны:'))
                    perimetr = (len_1 + len_2 + len_3)
                    print('Ответ: Периметр этого треугольника =',perimetr)
                    print('~'*62)
                elif figure == 'квадрат':
                    len_1 = float(input('Введите длину любой стороны:'))
                    perimetr = (len_1 * 4)
                    print('Ответ: Периметр этого квадрата =',perimetr)
                    print('~'*62)
                elif figure == 'прямоугольник':
                    len_1 = float(input('Введите длину прямоугольника:'))
                    len_2 = float(input('Введите ширину прямоугольника:'))
                    perimetr = len_1 * 2 + len_2 * 2
                    print('Ответ: Периметр этого прямоугольника =',perimetr)
                    print('~'*62)
                elif figure == 'ромб':
                    len_1 = float(input('Введите длинну любой стороны:'))
                    perimetr = (len_1 * 4)
                    print('Ответ: Периметр этого ромба =',perimetr)
                    print('~'*62)
                elif figure == 'параллелограмм':
                    len_1 = float(input('Введите длину параллелограмма:'))
                    len_2 = float(input('Введите ширину параллелограмма:'))
                    perimetr = len_1 * 2 + len_2 * 2
                    print('Ответ: Периметр этого параллелограмма =',perimetr)
                    print('~'*62)
                else:
                    print('\n','☒Ошибка!☒ Я не понял что это за фигура! Проверьте написание названия фигуры!','\n')
                    print('~'*62)
            elif action == 's' :
                figure = input('Введите название фигуры (пример: треугольник)').lower()
                if figure == 'треугольник':
                    len_1 = float(input('Введите длину 1 стороны:'))
                    len_2 = float(input('Введите длину 2 стороны:'))
                    len_3 = float(input('Введите длину 3 стороны:'))
                    perimetr = (len_1 + len_2 + len_3) / 2
                    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
                    print('Ответ: Площадь этого треугольника =',s)
                    print('~'*62)
                elif figure == 'квадрат':
                    len_1 = float(input('Введите длину любой стороны:'))
                    s = (len_1 ** 2)
                    print('Ответ: Площадь этого квадрата =',s)
                    print('~'*62)
                elif figure == 'прямоугольник':
                    len_1 = float(input('Введите длину прямоугольника:'))
                    len_2 = float(input('Введите ширину прямоугольника:'))
                    s = len_1 * len_2
                    print('Ответ: Площадь этого прямоугольника =',s)
                    print('~'*62)
                else:
                    print('\n','☒Ошибка!☒ Я не понял что это за фигура! Проверьте написание названия фигуры!','\n')
                    print('~'*62)
            elif action == 'cos':
                num = float(input('Введите аргумент в радианах:'))
                print('Ответ: cos'+str(num)+' =',math.cos(num))
                print('~'*62)
            elif action == 'sin':
                num = float(input('Введите аргумент в радианах:'))
                print('Ответ: sin'+str(num)+' =',math.sin(num))
                print('~'*62)
            elif action == 'tan':
                num = float(input('Введите аргумент в радианах:'))
                print('Ответ: tan'+str(num)+' =',math.tan(num))
                print('~'*62)
            else:
                print('\n','☒Ошибка!☒ Я не понял действие!','\n')
                print('~'*62)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '@' or 'поиск' in q:
            print('Я могу найти всё, что угодно! 🥸')
            call = input('Введите ссылку или запрос: ')
            if re.search(r'\.', call):
                webbrowser.open_new_tab('https://' + call)
            elif re.search(r'\ ', call):
                webbrowser.open_new_tab(browser + call)
            else:
                webbrowser.open_new_tab(browser + call)
            print('~'*62,'\n')
            print_menu_ru()
        elif q == '6' or 'анализ' in q:
            txt = input('Вводите текст (можете его скопировать и вставить сюда):').capitalize()
            print('~'*62)
            print('Текст:\n',txt,'\n')
            print('Всего в этом тексте:\n'+str('~'*62),'\n*',len(txt),'cимволов/символа/cимвол\n*',txt.count(' ')+1,'слова/слово/слов\n*',txt.count('.'),'предложений/предложения/предложение\n'+str('~'*62),'\n')
            find_q = input('Вы хотите найти какое-то слово или символ в этом тексте? (да/нет)').lower().find('да')
            if find_q != -1:
                find_word = input('Введите символ или слово которое хотите найти:')
                word_num = txt.find(find_word)
                if word_num == -1:
                    print('Прости, но такого символа/слова в данном тексте нет!')
                else:
                    print('О, я знаю! он(о) начинается с символа номер',word_num + 1,'!')
            else:
                print('Не хотите, как хотите)')
            print('~'*62,'\n')
            print_menu_ru()
        elif q == '7' or 'рандомайзер' in q:
            affairs = list()
            affair = input('Вводите слова или числа и заполняйте список : (stop - остановиться)').lower()
            while affair != 'stop':
                affairs.append(affair)
                affair = input('Продолжайте вводить слова или числа и заполнять список : (stop - остановиться)').lower()
            len_affair = len(affairs)
            rand = randint(0, len_affair - 1)
            print('\n'+'Всего введёных элементов:',len_affair)
            print('Рандомная генерация... \nВыбрано:',affairs[rand],'\nШанс выбора этого элемента - 1 к',len_affair,'или', round(100 / len_affair, 2),'% !\n')
        elif q == '12' or 'математик' in q:
            print('Это игра бесконечна!')
            print('Если вы правильно ответили к вашему счёту прибавляется 1 балл!\nА если неправильно - 0 баллов!\nУдачи!')
            input('Нажмите "Enter" когда будете готовы!')
            score = 0
            steps = 0
            num1 = randint(0,100)
            num2 = randint(0,100)
            print(f'{num1} + {num2}')
            ans = input('Ответ: (stop - остановиться)')
            while ans != 'stop':
                steps+=1
                try:
                    ans = int(ans)
                except:
                    print('Вы ввели не число')
                    break
                if ans == num1+num2:
                    print('Правильно! +1 балл!')
                    score += 1
                if ans != num1+num2:
                    print('Неправильно! +0 баллов! Ответ:',num1+num2,'!')
                num1 = randint(0,100)
                num2 = randint(0,100)
                print(f'{num1} + {num2}')
                ans = input('Ответ: (stop - остановиться)')
            print('~'*60)
            print(f'Игра окончена!\nНабрано {score} балла(ов) из {steps}!')
            try:
                correct_percent = score/steps * 100
            except:
                correct_percent = 0
            print(f'Точность ответов - {correct_percent}% !')
            print('~'*60,'\n')
        elif q == '8' or 'крестик' in q:
            print('Открываю...')
            sleep(1)
            webbrowser.open_new_tab('https://learn.algoritmika.org/share/19006923')
            # edition = input('Какую версию игры вы хотите выбрать?\n1 - Tic_Tac_Toe (by Евгений Воробьёв)\n2 - Modernized Tic Tac Toe (by Алексей Кирюшин)')
            # while True:
            #     if edition == '1':
            #         print('Да начнётся игра!)')
            #         webbrowser.open_new_tab('https://learn.algoritmika.org/community?projectId=19006923')
            #         break
            #     elif edition == '2':
            #         print('Да начнётся игра!)')
            #         webbrowser.open_new_tab('https://learn.algoritmika.org/community?projectId=24867781')
            #         break
            #     else:
            #         print('Введите только число!')
            #         edition = input('Какую версию игры вы хотите выбрать?\n1 - Tic_Tac_Toe (by Евгений Воробьёв)\n2 - Modernized Tic Tac Toe (by Алексей Кирюшин)')
        elif q == '9' or 'погод' in q:
            webbrowser.open_new_tab('https://yandex.ru/pogoda/nowcast')
        elif q == '13' or 'рекомен' in q:
            catagory = input('Выберите жанр:\n1 - RPG\n2 - Simulator\n3 - Strategy\n4 - Fighting\n5 - Battle Royale\n')
            if catagory != '1' or catagory != '2'or catagory != '3' or catagory != '4' or catagory != '5':
                print('Вводите цифру!')
                catagory = input('Выберите жанр:\n1 - RPG\n2 - Simulator\n3 - Strategy\n4 - Fighting\n5 - Battle Royale\n')
            print('~'*62,'\n')
            platform = input('Выберете платформу:\n1 - PS\n2 - XBOX\n3 - ПК\n4 - Nintendo Switch\n5 - Телефон\n')
            if platform != '1' or platform != '2'or platform != '3' or platform != '4' or platform != '5':
                print('Вводите цифру!')
                platform = input('Выберете платформу:\n1 - PS\n2 - XBOX\n3 - ПК\n4 - Nintendo Switch\n5 - Телефон\n')
            print('~'*62,'\n')
            if catagory == '1':
                if platform == '1':
                    print('Я советую тебе - Ведьмак 3 ; Cyberpunk 2077 ; Ghost of Tsushima ; Kingdom Come: Deliverance ; TES 5')
                elif platform == '2':
                    print('Я советую тебе - Ведьмак 3 ; Cyberpunk 2077 ; TES 5 ; Kingdom Come: Deliverance')
                elif platform == '3':
                    print('Я советую тебе - Ведьмак 1/2/3 ; Cyberpunk 2077 ; TES 3/4/5 ; Kingdom Come: Deliverance')
                elif platform == '4':
                    print('Я советует ю тебе - Ведьмак 3 ; TES 5 ; Diablo 3')
                elif platform == '5':
                    print('Я советую тебе - не знаю норм игр на телефон ')
            elif catagory == '2':
                if platform == '1':
                    print('Я советую тебе - UFC 2/3 ; Kingdom Come: Deliverance ; NFS')
                elif platform == '2':
                    print('Я советую тебе - UFC 2/3 ; Forza ; Kingdom Come: Deliverance')
                elif platform == '3':
                    print('Я советую тебе - Ведьмак 3 ; Kingdom Come: Deliverance ; FrostPunk ; Fifa 19/20/21/22 ; Forza')
                elif platform == '4':
                    print('Я советую тебе - FrostPunk ; Fifa 19/20/21/22 ; Kingdom Come: Deliverance')
                elif platform == '5':
                    print('Я советую тебе - не знаю норм игр на телефон ')
            else:
                print('coming soon...')
        elif q == '10' or 'новост' in q:
            print('Новости мира "Алгоритмики"')
            sleep(0.5)
            print('Абоба стал добрым! Скоро начнётся масштабный конкурс в Зале Славы! Многим изменили ники! И многое другое!\nНа этом пока всё!')
            sleep(3.25)
        elif q == '-1' or 'доск' in q:
            print('Почётная доска тех кто украл этот проект:\nВнимание!\nПроект украли - Шарапова Светлана, Шерзод Хатамов, Ярмошевич Дмитрий, Мичников Илья, Марахонич Никита\nИх профили:\n\nШерзод - https://learn.algoritmika.org/community?profileId=635906 \n\nСветлана - https://learn.algoritmika.org/community?profileId=1017292 \n\nДмитрий - https://learn.algoritmika.org/community?profileId=756978 \n\nИлья - https://learn.algoritmika.org/community?profileId=767148 \n\nНикита - https://learn.algoritmika.org/community?profileId=1070322')
            print('~'* 60,'\n')
            sleep(0.5)
        elif q == '11' or 'секундомер' in q:
            circle = 0
            input('Нажмите клавишу "Enter" чтобы начать')
            start = time()
            time_action = input('Нажмите клавишу "Enter" чтобы закончить или любую другую + "Enter", чтобы запомнить круг!')
            while time_action != '':
                if time_action != '':
                    circle += 1
                    end_circle = time()
                    print(f'Круг {circle}: {end_circle - start} секунд!')
                time_action = input('Нажмите клавишу "Enter" чтобы закончить или любую другую + "Enter", чтобы запомнить круг!')
            end = time()
            print(f'Всего прошло {end - start} секунд!')   
        elif q == '14' or 'википед' in q:
            print('Открываю...')
            sleep(1.75)
            webbrowser.open('https://ru.wikipedia.org/wiki/Служебная:Случайная_страница')
        elif q == '15' or 'бал' in q:
            marks = input('Введите оценки через пробел:')
            while True:
                try:
                    marks_list = marks.split(' ')
                    for i, mark in enumerate(marks_list):
                        marks_list[i] = int(mark)
                    print('Анализ набора оценок:', marks_list)
                    print(f'Средний балл - {sum(marks_list)/len(marks_list)}')
                    break
                except:
                    print('Error! Некорректный ввод!')
                    marks = input('Введите оценки через пробел:')
            print('~'*62,'\n')
    #     elif q == '16':
    #         symbols = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-/()&[]{}#%_."
    #         count = input("Введите желаемое количество паролей")

    #         #проверка № 1
    #         while True:
    #             try:
    #                 count = int(count)
    #                 if count > 10:
    #                     print('Введите другое количество! Сайт или ваш компьютер может не выдержать такой нагрузки!')
    #                     count = input("Введите желаемое количество паролей")
    #                 else: break
    #             except:
    #                 print("Введите число!")
    #                 count = input("Введите желаемое количество паролей")
                

    #         length = input("Введите желаемую длину пароля (чем больше тем надёжней, но трудней запомнить)")

    #         #проверка № 2
    #         while True:
    #             try:
    #                 length = int(length)
    #                 if length > 10:
    #                     print('Введите другую длину (от 1 до 10)! Сайт или ваш компьютер может не выдержать такой нагрузки!')
    #                     length = input("Введите желаемую длину паролей")
    #                 else: break
    #             except:
    #                 print("Введите число!")
    #                 length = input("Введите желаемую длину паролей")


    #         #генерирование пароля
    #         print('~'*60)
    #         for i in range(count):
    #             password =''
    #             for n in range(length):
    #                 password += random.choice(symbols)
    #             print("Ваш пароль №",i+1,", состоящий из",length,"символов: \n",password)
    #             print('~'*60)
    # #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        else:
            print('✘Ошибка✘ Я вас не понял! 😡\n')
            print('Прости... Я могу поискать это в интернете!')
            q_search = input('Искать? (да/нет)').lower()
            if q_search == 'да':
                webbrowser.open_new_tab(browser + q)
            else:
                print('Не хотите, как хотите)')
            print('~'*62,'\n')
        q = input('Как я могу тебе помочь?').lower()
elif language == 'eng':
    print('🤪 Hi! I am your virtual assistant.')
    print('Nikita Pokhodnya created me!')
    print('My name is Atlas! 🤓')
    name = input("🧐 What's your name? 🧐")
    print('Nice to meet you',name,'! 😁')  
    rec_browser = input('Which browser do you prefer? 😊').lower()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    yandex_eng = rec_browser.find('yandex')
    yandex_ru = rec_browser.find('яндекс')
    google_ru = rec_browser.find('гугл')
    google_eng = rec_browser.find('google')
    DuckDuckGo_eng_classic = rec_browser.find('duckduckgo')
    DuckDuckGo_ru_classic = rec_browser.find('дакдакго')
    DuckDuckGo_ru_classic_correct = rec_browser.find('дакдакгоу')
    DuckDuckGo_ru = rec_browser.find('дак дак го')
    DuckDuckGo_ru_correct = rec_browser.find('дак дак гоу')
    DuckDuckGo_eng = rec_browser.find('duck duck go')
    bing_ru = rec_browser.find('бинг')
    bing_eng = rec_browser.find('bing')
    ecosia_ru = rec_browser.find('экозия')
    ecosia_eng = rec_browser.find('ecosia')
    yahoo_ru = rec_browser.find('яху')
    yahoo_eng = rec_browser.find('yahoo')
    mailru_rus = rec_browser.find('майл')
    mailru_rus_2 = rec_browser.find('мэйл')
    mailru_eng_ru = rec_browser.find('mail')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if yandex_eng != -1 or yandex_ru != -1:
        print('Oh, Russian browser? Respect!')
        browser = yandex
    elif DuckDuckGo_eng_classic != -1 or DuckDuckGo_ru != -1 or DuckDuckGo_ru_classic != -1 or DuckDuckGo_ru_classic_correct != -1 or DuckDuckGo_ru_correct != -1 or DuckDuckGo_eng != -1: 
        print('Mmmm ... you love privacy?')
        browser = DuckDuckGo
    elif bing_ru != -1 or bing_eng != -1:
        print('Microsoft, so Microsoft!')
        browser = bing
    elif ecosia_ru != -1 or ecosia_eng != -1:
        print('I am also for the ecology! Respect 😎')
        browser = ecosia
    elif yahoo_eng != -1 or yahoo_ru != -1:
        print ('You are true old!')
        browser = yahoo
    elif mailru_eng_ru != -1 or mailru_rus!= -1 or mailru_rus_2!= -1:
        print ("Wow, I haven't met such people for a long time!")
        browser = mailru
    else:
        print('Thank you for the honest answer!')
        browser = google
    print_menu_eu()
    q = input ('How can I help you?')

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    while q != '0':
        if q == '1':
            mode = input ('Who will guess? (1 - You / 2 - Computer)')
            if mode == '1':
                print ('Do you want to enter the maximum number yourself or choose the difficulty level?')
                print ('1 - Enter it yourself!')
                print ('2 - Choose from difficulty levels!')
                q_rand_num = int (input ('Choose:'))
                if q_rand_num == 1:
                    num_play = int (input ('Please enter:'))
                elif q_rand_num == 2:
                    print ('1 - Easy (5 max. number)')
                    print ('2 - Normal (10 max.number)')
                    print ('3 - Hard (30 max. number)')
                    num_play_q = int (input ('Please choose:'))
                    if num_play_q == 1:
                        num_play = 5
                    elif num_play_q == 2:
                        num_play = 10
                    elif num_play_q == 3:
                        num_play = 30
                num_play_a = randint (1, num_play)
                print ('Guess the number I am guessing from 1 to', num_play, '!')
                print ('I will tell you that my number is greater than (>) or less (<) than your number!')
                player_num = int (input ('Please enter a number:'))
                steps = 1
                while player_num != num_play_a:
                    if player_num < num_play_a:
                        print('The number I have envisioned >',player_num)
                        steps += 1
                        player_num = int(input('Please enter a number:'))
                    elif player_num> num_play_a:
                        steps += 1
                        print ('The number I have envisioned <', player_num)
                        player_num = int(input('Please enter a number:'))
                print ('You guessed the number and you win!')
                print ('Guess the number with', steps, 'try!')
                print ('~' * 62, '\ n')
                q = input ('How can I help you?')
            elif mode == '2':
                steps = 0
                arr = range (1, 102)
                print ("Think of any number from 1 to 100")
                input ("Press 'Enter' when you're ready!")
                low = 0
                high = len (arr) -1
                while low <high:
                    steps += 1
                    middle = (low + high) // 2
                    ans_form = randint (1,5)
                    if ans_form == 1:
                        print ('This number is' + str (arr [middle]) + '?')
                    elif ans_form == 2:
                        print ('Maybe this is' + str (arr [middle]) + '?')
                    elif ans_form == 3:
                        print ('I think this is' + str (arr [middle]) + '?')
                    elif ans_form == 4:
                        print ("I'm sure this is" + str (arr [middle]) + "?")
                    elif ans_form == 5:
                        print ('Maybe ' + str (arr [middle]) + '?')
                    num_search = input ('(< - less than / > - greater than / = - equal)')
                    if num_search == "=":
                        print (f"Number guessed with {steps} tries!")
                        break
                    elif num_search == "<":
                        high = middle
                    elif num_search == ">":
                        low = middle
                    if num_search == ">" and high == 100 and low == 99:
                        low = high
                        if low == high:
                            print ("Your guessed number <1 / >100 / you put the signs incorrectly!")
                            break
            print ('~' * 62)
            q = input ('How can I help you?')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '2':
            print ('1 - comedy')
            print ('2 - thrillers')
            print ('3 - detective')
            print ('4 - horror')
            print ('5 - romantic')
            catag = input ('What genre do you prefer?')
            if catag == '1':
                films_comedy = ["Operation Y and Shurik's other adventures", 'Dumb and even dumber', 'Ivan Vasilyevich changes his profession', 'The Diamond Arm', 'Home Alone', 'Back to the Future', 'Third Extra', 'snatch','HOT FUZZ','U.N.C.L.E.']
                film_comedy_rand = randint (0, len (films_comedy) -1)
                print (f'I advise you to watch: {films_comedy [film_comedy_rand]} ')
            elif catag == '2':
                films_triller = ["Escape from Pretoria', 'Amnesia', 'Human Wrath', 'Nobody', 'Locked Up', 'Who Hasn't Hidden"]
                film_triller_rand = randint (0, len (films_triller) -1)
                print (f'I advise you to watch: {films_triller [film_triller_rand]} ')
            elif catag == '3':
                films_d = ['Wish Room', 'Search', 'Enola Holmes']
                film_d_rand = randint (0, len (films_d) -1)
                print (f'See: {films_d [film_d_rand]} ')
            elif catag == '4':
                films_scream = ['Wrong Turn', 'Conjuring 3', 'Grettel & Hansel']
                film_scream_rand = randint (0, len (films_scream) -1)
                print (f'There is a good movie - {films_scream [film_scream_rand]} ')
            elif catag == '5':
                films_l = ['Emma', 'Life in a Year', '365 Days']
                film_l_rand = randint (0, len (films_l) -1)
                print (f'I recommend: {films_l [film_l_rand]} ')
            print ('~' * 62, '\n')
            q = input ('How can I help you?')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '3':
            input ("Press 'Enter' when you're ready to write !!")
            start_time = time ()
            play_phrase = input ('Write a review about me:')
            end_time = time ()
            total_time = end_time - start_time
            symbols = len (play_phrase)
            print_speed = round (symbols / total_time, 2)
            print ('\n', '~' * 62)
            print ('* Print speed of this text:', round (total_time, 2), 'seconds!')
            print ('* Total in this text:', symbols, 'symbols!')
            print ('* Your speed is:', print_speed, 'characters per second or', print_speed * 60, 'characters per minute!')
            if print_speed * 60 <150:
                lvl_print_speed = 'Newbie'
            elif print_speed * 60 >= 150 and print_speed <250:
                lvl_print_speed = 'Normal User'
            elif print_speed * 60>= 250 and print_speed <400:
                lvl_print_speed = 'Pro'
            elif print_speed>= 400 and print_speed * 60 <1080:
                lvl_print_speed = 'Unique'
            elif print_speed>= 1080:
                lvl_print_speed = 'Whaaaaat? !! This is a world record! Take a screenshot!!!'
            print ('* Your level:', lvl_print_speed, '!')
            print ('~' * 62, '\n')
            q = input ('How can I help you?')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '?':
            print ("🤪 Hi, I'm a your virtual assistant.")
            print ('My name is Atlas! 🤓')
            print ('And you, apparently,', name, '😅')  
            print_menu_eu()
            q = input ('How can I help you?')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '4':
            print ('Attention! Websites open in the default browser!')
            print ('Which site do you want to open?')
            print ('~' * 64)
            print ('* VK \ n * YouTube \ n * Steam \ n * Apple \ n * Start \ n * TNT \ n * STS')
            print ('~' * 64)
            site = input ('Enter a name from the suggestions:'). lower ()
            if site == 'youtube':
                print ('One second ...')
                sleep (1)
                webbrowser.open ('https://www.youtube.com')
            elif site == 'vk' or site == 'vkontakte' or site == 'v kontakte':
                print ('One second ...')
                sleep (1)
                webbrowser.open ('https://vk.com')
            elif site == 'steam' :
                print ('One second ...')
                sleep (1)
                webbrowser.open ('https://store.steampowered.com/?l=russian')
            elif site == 'apple' :
                print ('One second ...')
                sleep (1)
                webbrowser.open ('https://www.apple.com/ru/')
            elif site == 'start':
                print ('One second ...')
                sleep (1)
                webbrowser.open ('https://start.ru')
            elif site == 'tnt':
                print ('One second ...')
                sleep (1)
                webbrowser.open ('https://tnt-online.ru')
            elif site == 'sts':
                print ('One second ...')
                sleep (1)
                webbrowser.open ('https://ctc.ru')
            else:
                print ("Sorry! 🥺 I don't know such a site!")
                q_search = input ('Search? (yes / no)').lower()
                if q_search == 'yes':
                    webbrowser.open_new_tab (browser + site)
                else:
                    print ("Don't want it as you want)")
            print ('~' * 62, '\n')
            q = input ('How can I help you?')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '5':
            action = input ('\nSelect an action: \n- subtraction; \n+ addition; \n/ division; \n* multiplication; \n// division without remainder; \n% finding the remainder from division; \n** raising to a power; \n$ finding the square root of a number; \n! - finding the factorial of a number; \nlog - finding the lagorithm of a number; \nsum - finding the sum of all elements in the list \narifm - finding µ of all numbers in the list\nP - Find the perimeter of the shape \nS - Find the area of ​​the shape\ncos - find cosine by argument x\nsin - find sine by argument x\ntan - find tangent by argument x '). lower ()
            if action == '-':
                num1 = float (input ('\nEnter the decrement :'))
                num2 = float (input ('\nEnter the subtraction :'))
                print ('Answer:', num1, '-', num2, '=', num1-num2)
                print ('~' * 62)
            elif action == '*':
                num1 = float (input ('\nEnter the first factor :'))
                num2 = float (input ('\nEnter the second factor :'))
                print ('\n', 'Answer:', num1, '*', num2, '=', num1 * num2)
                print ('~' * 62)
            elif action == '/':
                num1 = float (input ('\nEnter the dividend :'))
                num2 = float (input ('\nEnter the divisor :'))
                print ('\n', 'Answer:', num1, '÷', num2, '=', num1 / num2)
                print ('~' * 62)
            elif action == '+':
                num1 = float (input ('\nEnter the first syllable :'))
                num2 = float (input ('\nEnter the second syllable :'))
                print ('\n', 'Answer:', num1, '+', num2, '=', num1 + num2)
                print ('~' * 62)
            elif action == '//':
                num1 = float (input ('\nEnter the dividend :'))
                num2 = float (input ('\nEnter the divisor :'))
                print ('\n', 'Answer without a remainder:', num1, '÷', num2, '=', num1 // num2)
                print ('~' * 62)
            elif action == '**':
                num1 = float (input ('\nEnter the number to be raised to the power :'))
                num2 = float (input ('\nEnter the power to raise :'))
                print ('\n', 'Answer:', num1, '^', num2, '=', num1 ** num2)
                print ('~' * 62)
            elif action == '%':
                num1 = float (input ('\ nEnter the dividend :'))
                num2 = float (input ('\ nEnter the divisor :'))
                print ('\n', 'Answer: Remainder of', num1, '÷', num2, '=', num1%num2)
                print ('~' * 62)
            elif action == '$':
                num1 = float (input ('\ nEnter the number to find the square root :'))
                sqrt = math.sqrt (num1)
                print ('\n', 'Answer: ⎷' + str (num1) + ' = ±' + str (sqrt))
                print ('~' * 62)
            elif action == '!':
                num1 = float (input ('\ nEnter the number to find the factorial :'))
                print ('Answer: !' + str (num1) + ' =', math.factorial (num1))
                print ('~' * 62)
            elif action == 'log':
                num1 = float (input ('\ nEnter a number to find the logarithm :'))
                base = float (input ('Enter base:'))
                print ('Answer: log' + str (num1) + 'base', base, '=', math.log (num1, base))
                print ('~' * 62)
            elif action == 'sum':
                numbers = []
                num_list = input ('Enter numbers and fill in the list (stop - stop)')
                while num_list != 'stop':
                    numbers.append (float (num_list))
                    num_list = input ('Enter numbers and fill in the list (stop - stop)')
                print ('\nAnswer: Sum of all items in the list', numbers, '=', math.fsum (numbers))
                print ('~' * 62)
            elif action == 'arifm':
                numbers = []
                num_list = input ('Enter numbers and fill in the list (stop - stop)')
                while num_list != 'stop':
                    numbers.append (float (num_list))
                    num_list = input ('Enter numbers and fill in the list (stop - stop)')
                print ('\nAnswer: µ of all elements in the list', numbers, '=', math.fsum (numbers) / len (numbers))
                print ('~' * 62)
            elif action == 'p':
                figure = input ('Enter a name for the figure (example: triangle)'). lower ()
                if figure == 'triangle':
                    len_1 = float (input ('Enter 1 side length:'))
                    len_2 = float (input ('Enter 2 side length:'))
                    len_3 = float (input ('Enter 3 side length:'))
                    perimetr = (len_1 + len_2 + len_3)
                    print ('Answer: Perimeter of this triangle =', perimetr)
                    print ('~' * 62)
                elif figure == 'square':
                    len_1 = float (input ('Enter the length of either side:'))
                    perimetr = (len_1 * 4)
                    print ('Answer: Perimeter of this square =', perimetr)
                    print ('~' * 62)
                elif figure == 'rectangle':
                    len_1 = float (input ('Enter the length of the rectangle:'))
                    len_2 = float (input ('Enter the width of the rectangle:'))
                    perimetr = len_1 * 2 + len_2 * 2
                    print ('Answer: Perimeter of this rectangle =', perimetr)
                    print ('~' * 62)
                elif figure == 'rhombus':
                    len_1 = float (input ('Enter the length of either side:'))
                    perimetr = (len_1 * 4)
                    print ('Answer: Perimeter of this rhombus =', perimetr)
                    print ('~' * 62)
                elif figure == 'parallelogram':
                    len_1 = float (input ('Enter the length of the parallelogram:'))
                    len_2 = float (input ('Enter the width of the parallelogram:'))
                    perimetr = len_1 * 2 + len_2 * 2
                    print ('Answer: Perimeter of this parallelogram =', perimetr)
                    print ('~' * 62)
                else:
                    print ('\n', '☒Error! ☒ I don’t understand what this figure is! Check the spelling of the figure name!', '\n')
                    print ('~' * 62)
            elif action == 's':
                figure = input ('Enter a name for the figure (example: triangle)').lower()
                if figure == 'triangle':
                    len_1 = float (input ('Enter 1 side length:'))
                    len_2 = float (input ('Enter 2 side length:'))
                    len_3 = float (input ('Enter 3 side length:'))
                    perimetr = (len_1 + len_2 + len_3) / 2
                    s = math.sqrt (p * (p-a) * (p-b) * (p-c))
                    print ('Answer: Area of ​​this triangle =', s)
                    print ('~' * 62)
                elif figure == 'square':
                    len_1 = float (input ('Enter the length of either side:'))
                    s = (len_1 ** 2)
                    print ('Answer: Area of ​​this square =', s)
                    print ('~' * 62)
                elif figure == 'rectangle':
                    len_1 = float (input ('Enter the length of the rectangle:'))
                    len_2 = float (input ('Enter the width of the rectangle:'))
                    s = len_1 * len_2
                    print ('Answer: Area of ​​this rectangle =', s)
                    print ('~' * 62)
                else:
                    print ('\n', '☒Error! ☒ I don’t understand what this figure is! Check the spelling of the figure name!', '\n')
                    print ('~' * 62)
                print_menu_eu()
            elif action == 'cos':
                num = float (input ('Enter the argument in radians:'))
                print ('Answer: cos' + str (num) + '=', math.cos (num))
                print ('~' * 62)
            elif action == 'sin':
                num = float (input ('Enter the argument in radians:'))
                print ('Answer: sin' + str (num) + '=', math.sin (num))
                print ('~' * 62)
            elif action == 'tan':
                num = float (input ('Enter the argument in radians:'))
                print ('Answer: tan' + str (num) + '=', math.tan (num))
                print ('~' * 62)
            else:
                print ('\n', '☒Error!☒ I did not understand the action!', '\n')
                print ('~' * 62)
            q = input ('How can I help you?')
            
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif q == '@':
            print ('I can find anything! 🤓')
            call = input ('Enter link or request:')
            if re.search(r'\.', call):
                webbrowser.open_new_tab('https://' + call)
            elif re.search(r'\ ', call):
                webbrowser.open_new_tab(browser + call)
            else:
                webbrowser.open_new_tab(browser + call)
            print('~'*62,'\n')
            print_menu_eu()
        elif q == '6':
            txt = input ('Enter text (you can copy and paste it here):'). capitalize ()
            print ('~' * 62)
            print ('Text: \n', txt, '\n')
            print ('Total in this text: \n' + str ('~' * 62), '\n *', len (txt), 'characters \ n *', txt.count ('') + txt.count (',') + txt.count (':') + txt.count (';'), 'words \n *', txt.count ('.'), 'suggestions\n '+ str (' ~ '* 62),' \n ')
            find_q = input ('Do you want to find some word or character in this text? (yes / no)'). lower (). find ('yes')
            if find_q!= -1:
                find_word = input ('Enter the character or word you want to find:')
                word_num = txt.find(find_word)
                if word_num == -1:
                    print ('Sorry, but there is no such character/word in this text!')
                else:
                    print ('Oh, I know! it starts with character number', word_num + 1, '!')
            else:
                print ("Don't want it as you want")
            print('~'*62,'\n')
            print_menu_eu()
        elif q == '7':
            affairs = list()
            affair = input ('Enter words or numbers and fill in the list: (stop - stop)'). lower ()
            while affair!= 'stop':
                affairs.append (affair)
                affair = input ('Keep typing words or numbers and filling the list: (stop - stop)'). lower ()
            len_affair = len (affairs)
            rand = randint (0, len_affair - 1)
            print ('\n' + 'Total entered items:', len_affair)
            print ('Randomly generate ... \nSelected:', affairs [rand], '\nChance of this item being selected is 1 to', len_affair,'or', round(100 / len_affair, 1),'% !\n')
            q = input ('How can I help you?')
        elif q == '8':
            print ('Let the game begin!')
            sleep (2)
            webbrowser.open_new_tab ('https://learn.algoritmika.org/community?projectId=19006923')
            q = input ('How can I help you?')
        elif q == '9':
            weather_city = input('Enter the name of your city in English!')
            print('One second ...')
            sleep(0.6)
            webbrowser.open_new_tab('https://yandex.ru/pogoda/nowcast')
            q = input ('How can I help you?') 
        elif q == '100':
            while True:
                print ('This game is endless!')
                print ('If you answered correctly, 1 point is added to your score! \nAnd if incorrectly 0 points! \nGood luck!')
                input ('Press "Enter" when ready!')
                score = 0
                steps = 0
                num1 = randint (0,100)
                num2 = randint (0,100)
                print(f'{num1} + {num2}')
                ans = int(input('Answer:'))
                if ans == num1 + num2:
                    print('Correct! +1 points')
                    steps += 1
                    score += 1
                else:
                    print(f'Wrong! Answer: {num1+num2}! +0 points')
                    steps += 1
                num1 = randint (0,100)
                num2 = randint (0,100)
                print(f'{num1} + {num2}')
                ans = int(input('Answer:'))
            print ('~' * 60)
            print ('Game over! \nYou have typed', score, 'points out of', steps, '!')
            print ('~' * 60, '\n')
            q = input ('How can I help you?')
        elif q == '10':
            print ('10 - News of the world "Algorithmics" ')
            print ("A new emote has been added to the comment emoticons! \nThe emote (apparently) expresses surprise! \nSpoiler! I'm sure it will appear as an emote for likes! Along with a heart, fire and thumbs up! \nThat's all for now!" )
            sleep(3.25)
            q = input ('How can I help you?')
        elif q == '11':
            circle = 0
            input ('Press Enter to start')
            start = time()
            time_action = input ('Press "Enter" to finish or any other + "Enter" to remember the circle!')
            while time_action  != '':
                if time_action != '':
                    circle += 1
                    end_circle = time()
                    print (f'Circle {circle}: {end_circle - start} seconds! ')
                time_action = input ('Press "Enter" to finish or any other + "Enter" to remember the time!')
            end = time()
            print (f"It's been {end - start} seconds in total!")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        else:
            print ('✘Error✘ I do not understand you! 😡 \ n')
            print ('Sorry ... I can search the internet for this!')
            q_search = input ('Search? (yes / no)'). lower ()
            if q_search == 'yes':
                webbrowser.open_new_tab (browser + q)
            else:
                print ("Don't want it as you want")
            print ('~' * 62, '\n')
            print ("Here's what I can do:")
            print_menu_eu()
            q = input ('How can I help you?')
