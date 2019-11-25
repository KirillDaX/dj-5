from django.shortcuts import render, redirect
from game.models import Game, Player, PlayerGameInfo


def show_home(request):
    context = {'test': request.session.items()}
    if request.method == 'POST':

        player = Player.objects.create(owner=True)  # создаем игрока который загадал число и делаем его владельцем игры
        game = Game.objects.create(guessed_number=request.POST['guessed_number'])  # создаем игру c загаданным числом
        PlayerGameInfo.objects.create(player=player, game=game)

        request.session['member_id'] = player.id
        request.session['game_id'] = game.id

        context['guessed_number'] = Game.guessed_number
        context['player'] = player.id
        return redirect('game')

    if request.method == 'GET':
        if Player.objects.filter(pk=1):  # если игрок 1 уже есть, создаем 2ого и заносим его в сессию
            if not request.session.get('member2_id'):  # если нет в сессиях 2ого игрока, создаем
                player2 = Player.objects.create()  # создаем играющего, id и owner проставятся сами
                request.session['member2_id'] = player2.id
                request.session['try_count'] = 0
                return redirect('game')  # отправлем игрока2 на шаблон игры

    return render(request, 'home.html', context)


def game_view(request):  # вью для отгадывания, срабатывает по редиректу из show_home из if

    guessed_number = list(Game.objects.values_list('guessed_number').get(pk=1))  # загаданное число, ::qs, int
    context = {

               'info': list(PlayerGameInfo.objects.values_list('try_count'))[0][0],
               'guessed_number': guessed_number[0],
               'show_form': request.session.get('member2_id')}
    if request.session.get('member2_id') == 2:

        if request.method == 'POST':
            attempt_to_guess = int(request.POST['attempt_to_guess'])  # число которое ввели для отгадывания:: str
            request.session['try_count'] += 1

            if attempt_to_guess == guessed_number[0]:
                context['text_msg'] = 'Вы уагадали!'
                PlayerGameInfo.objects.update(guessed=True)
                context['guessed'] = list(PlayerGameInfo.objects.values_list('guessed'))[0][0]

            elif attempt_to_guess > guessed_number[0]:
                context['text_msg'] = 'Вы не угадали, загаданное число меньше, сделано попыток: ' + str(request.session['try_count'])

            elif attempt_to_guess < guessed_number[0]:
                context['text_msg'] = 'Вы не угадали, загаданное число больше, сделано попыток: ' + str(request.session['try_count'])

            PlayerGameInfo.objects.update(try_count=request.session['try_count'])

        if request.method == 'GET':
            try_count_in_game = list(PlayerGameInfo.objects.values_list('try_count'))[0][0]
            guessed = list(PlayerGameInfo.objects.values_list('guessed'))[0][0]
            context['guessed'] = guessed

            if guessed:
                context['text_msg2'] = 'Ваше число уагадали с ' + str(try_count_in_game) + ' раз'

    return render(request, 'game.html', context)


