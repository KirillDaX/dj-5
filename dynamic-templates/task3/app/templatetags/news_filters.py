from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    """
    format_date: форматирует дату по следующим правилам
    Если пост был меньше 10 минут назад, пишет "только что"
    Если пост был меньше 24 часов назад, пишет "X часов назад"
    Если пост был больше 24 часов назад, выводит дату в формате "Год-месяц-число"
    :param value
    :return: time_msg
    """
    date_value = datetime.fromtimestamp(value)
    now = datetime.now()
    delta = now - date_value
    seconds = delta.total_seconds()
    minutes = (seconds % 3600) // 60

    time_msg = ''
    if minutes < 10:
        time_msg = 'только что'
    elif 1440 >= minutes >= 10:
        time_msg = f'{int(minutes / 60)} часов {int(minutes)} мин. назад'
    elif minutes > 1440:
        time_msg = date_value.strftime('%Y-%m-%d')
    return time_msg


@register.filter
def score_modification(value):
    """
    Рейтинг меньше -5, пишет "все плохо"
    Рейтинг от -5 до 5 – "нейтрально"
    Рейтинг больше 5 – "хорошо"
    :param value
    :return: msg_score
    """
    msg_score = ''
    if value:
        if value < -5:
            msg_score = 'все плохо'
        elif -5 <= value <= 5:
            msg_score = 'нейтрально'
        elif value > 5:
            msg_score = 'хорошо'
    else:
        msg_score = value
    return msg_score


@register.filter
def format_num_comments(value):
    """
    Если комментариев 0, пишется "Оставьте комментарий"
    От 0 до 50, пишем число комментариев
    Больше 50, пишем "50+"
    :param value
    :return: msg_num_comments
    """
    msg_num_comments = ''
    if value == 0:
        msg_num_comments = 'Оставьте комментарий'
    elif 0 < value <= 50:
        msg_num_comments = value
    elif value > 50:
        msg_num_comments = '50+'
    return msg_num_comments


@register.filter
def format_selftext(value, count):
    """
    Оставляет count первых и count последних слов, между ними должно быть троеточие.
    count задается параметром фильтра.
    Пример c count = 5: "Hi all sorry if this ... help or advice greatly appreciated."
    :param value, count
    :return: msg_selftext
    """
    msg_selftext = value.split()
    all_out_str = ''
    if value:
        if count*2 < len(msg_selftext):
            for item in msg_selftext[0:count]:
                all_out_str += item + ' '

            all_out_str = all_out_str + '...'

            for item in msg_selftext[-count:]:
                all_out_str += item + ' '
        else:
            all_out_str = value
    else:
        all_out_str = '[empty message]'
    return all_out_str
