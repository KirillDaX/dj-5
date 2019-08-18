from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        values = []
        for item_row in reader:
            key_item = ''.join(item_row)
            values.append(item_row[key_item].split(';'))
        heads = key_item.split(';')

    context = {'heads': heads, 'values': values}
    return render(request, template_name, context)




