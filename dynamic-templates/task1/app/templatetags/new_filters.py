from django import template

register = template.Library()


@register.filter
def styleze(value, row):
    if value:
        index = row.index(value)
        val = float(value)

        if index == len(row) - 1:
            return 'grey'
        elif index != 0 and index != 13:
            if val < 0:
                return 'green'
            elif 0 <= val <= 1:
                return 'white'
            elif 1 < val <= 2:
                return '#f99'
            elif 2 < val <= 5:
                return '#f44'
            elif val > 5:
                return '#F27'
