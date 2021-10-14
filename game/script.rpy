# Определение персонажей игры.
define dan = Character('', color="#c8ffc8")
define k = Character('Кирилл', color="#c8ffc8", image='kirill')
define gg = Character('[ggname]', color="#000000")

# Переменные
# Вася и Петя спорят
define vasa_i_petia_eror = False
define katia_i_sveta_eror = False

#Анимация моргает
image danil blink:
    "danil"
    choice:
        pause 3
    choice:
        pause 5
    choice:
        pause 8
    "danil bl"
    pause 0.25
    repeat

#Анимация облооко 1
image obloco:
    "obloco_1"
    0.3
    "obloco_2"
    0.3
    "obloco_3"
    0.3
    repeat

#Анимация тап по экрану
image tap:
    "tap 1"
    0.2
    "tap 2"
    0.2
    "tap 3"
    0.2
    "tap 4"
    0.2
    repeat

# помощник

# пояснение
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
# hide что бы персонаж пропал
# {cps=25}{cps=25} - залупа для эмуляции печатной машинки
# with dissolve - это переход проявление
# hide dima - что бы персонаж исчез
# moveoutright, moveoutleft, moveouttop, moveoutbottom уход объекта
# moveinright, moveinleft, moveintop, moveinbottom вход объекта
# отступ {space=12}
# пространство между "Строка 1{vspace=30}Строка 2"#начало игры
# новая строка \n
# "{cps=25}{color=#000000}{cps=25}"

# Начало игры
label start:


    scene bg purple with dissolve

    show danil blink with moveinleft



    show danil hi
    pause 1
    hide danil hi

    show danil blink

    show obloco zorder (100) with dissolve
    show tap
    dan "{cps=25}{color=#000000}Привет, меня зовут Данил и я здесь что бы помочь. Раз уж ты оказался(-ась) на этой страницы, значит ты столкнулся или столкнулась с проблемой буллинга.{cps=25}"
    hide tap
    dan "{cps=25}{color=#000000}Вот что я хочу тебе сейчас предложить. Далее тебе нужно будет создать своего персонажа и от его лица ответить на несколько несложных вопросов.{cps=25}"
    dan "{cps=25}{color=#000000}Постарайся не пропускать часть с вопросами, так как как они повлияют на конечный результат.{cps=25}"
    "{cps=25}{color=#000000} А конечным результатом будет смоделированная специально для тебя игра в жанре интерактивная новелла.{cps=25}"
    menu:
        "{cps=25}{color=#000000}Давай приступим к созданию персонажа?{cps=25}"
        "Давай":
            jump makecharacter
return

# Создание персонажа
label makecharacter:
    ""

    $ ggname = renpy.input("{cps=25}{color=#000000}\nКак зовут твоего персонажа?{cps=25}").strip()
    if ggname == "":
        $ggname = "Саша"
        dan"{cps=25}{color=#000000}Ну тогда я сам назову твоего персоажа. Пусть это будет Саша{cps=25}"
    dan"{cps=25}{color=#000000}[ggname]- это очень красивое имя{cps=25}"

    menu:
        "{cps=25}{color=#000000}Какого пола будет твой персонаж?{cps=25}"
        "Мужского":
            jump male
        "Женского":
            jump female
return

###############  Ветка для мальчиков  ###############
label male:
    dan"{cps=25}{color=#000000}Как-то давно, когда я был еще ребенком, мой отец сказал, что трудности закаляют мужчину. Он забыл добавить, что трудности и травля это совершенно разные вещи.{cps=25}"
return

###############  Ветка для девочек  ###############
label female:
    dan"{cps=25}{color=#000000}Бытует мнение, что буллинг это история про мальчиков, драки и соперничесво, но это далеко не так.{cps=25}"
    dan"{cps=25}{color=#000000}Теперь нам надо понять как выглядит [ggname]. {cps=25}"
    hide danil blink with moveoutleft
    pause 1
    show danil look out zorder (99) with moveinleft
    dan"{cps=25}{color=#000000}Да, и используй стрелочки, что бы изменять внешний вид твоего персонажа{cps=25}"
    hide danil look out with moveoutleft
    hide obloco with dissolve
    jump editor
return

# Редоктор персонажа
label editor:

    menu:
        "[ggname]"
        "Лицо":
            jump male
        "Очки":
            jump male
        "Прическа":
            jump male
        "Одежда":
            jump male
        "Готово":
            jump what_is_bullying
return

# Что такое буллинг
label what_is_bullying:
    show danil blink with moveinleft

    show obloco zorder (100) with dissolve
    "{cps=25}{color=#000000}[ggname] получилось очень красивой, жаль что я не захватил с собой букет цветов или хотябы шоколадку.{cps=25}"
    "{cps=25}{color=#000000}Ну ладно, давай вернемся к проблеме с которой столкнулась [ggname]. А может это просто предрасутки? Давай начнем с определения буллинга.{cps=25}"
    "{cps=25}{color=#000000}Травля( буллинг)- это вид группового эмоционального и/или физического насилия. Говоря белее простым языком, это регулярные издевательства...{cps=25}"
    "{cps=25}{color=#000000}причинения вреда,злые шутки и обидные действия по отношению к какому-либо участнику коллектива (класса, отряда, кружка) или к нескольким его участникам.{cps=25}"
    "{cps=25}{color=#000000}Если кто то ругается между собой или кто то кого то обидел, то это ещё не являться буллингом. Это обычный конфликт.{cps=25}"

    menu:
        "{cps=25}{color=#000000}[ggname] точно столкнулась именно с травлей?{cps=25}"
        "Да":
            jump this_is_bullying
        "Нет":
            jump this_is_not_bullying
        "Сомневаюсь":
            jump this_is_bullying_I_wonder
return

# Это буллинг
label this_is_bullying:
return

# Это не буллинг
label this_is_not_bullying:
return

# Я сомневаюсь буллинг ли это
label this_is_bullying_I_wonder:
    "{cps=25}{color=#000000}Окей. Давай попробуем разобраться. Сейчас ты увидишь 5 ситуаций и тебе нужно будет определить буллинг это или нет. Думаю это может развеять твои сомнения.{cps=25}"
    hide danil blink
    show danil_with_picture
    menu:
        "{cps=25}{color=#000000}Петя сказал Васе, что он абсолютный нуб в CS GO. Вася ответил, что Петя просто ему завидует. После долгого спора, Вася толкнул Петю и пошел домой{cps=25}"
        "Это булинг":
            "{cps=25}{color=#000000}Я считаю, что это больше похоже на обычный конфликт. Такие моменты возникают и у детей и у взрослых, ведь не всегда получается договориться. Это нормально.{cps=25}"
            $ vasa_i_petia_eror = True
        "Это конфликт":
            "{cps=25}{color=#000000}Я тоже так думаю. Ребята просто конфликтуют между собой. {cps=25}"

    hide danil_with_picture
    show danil_with_picture_2
    menu:
        "{cps=25}{color=#000000}Катя постоянно смеется над тем, как одевается Света. Смеяться громко, объясняя всему классу, чем плохи Светины наряды и почему так одеваться нельзя. Одноклассники смеются вместе с Катей.{cps=25}"
        "Это булинг":
            "{cps=25}{color=#000000}Я тоже так думаю. Она делает это систематически и привлекает всесь класс к травле. {cps=25}"
        "Это конфликт":
            "{cps=25}{color=#000000}Оброти внимание, что в этой ситуации Катя систематически обижает Свету.{cps=25}"
            $ katia_i_sveta_eror = True

    "{cps=25}{color=#000000}Решающий момент! Барабанная дробь!!! Трррррррррр-трррррррр-трррррр{cps=25}"
    if vasa_i_petia_eror and katia_i_sveta_eror:
        jump dolboeb
    if vasa_i_petia_eror:
        jump poludolboeb
    if  katia_i_sveta_eror:
        jump poludolboeb

    jump molodec
return


label dolboeb:
    "{cps=25}{color=#000000}Ты абсолютный добаеб{cps=25}"
return

label poludolboeb:
    "{cps=25}{color=#000000}Ты полудолбаеб{cps=25}"
return

label molodec:
    "{cps=25}{color=#000000}Ты молодец{cps=25}"
return
