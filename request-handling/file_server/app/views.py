import datetime
import os
from django.shortcuts import render
from app import settings
from datetime import datetime


def modification_date(filename):
    m_date = os.path.getmtime(filename)
    return datetime.fromtimestamp(m_date)


def creation_date(filename):
    c_date = os.path.getctime(filename)
    return datetime.fromtimestamp(c_date)


def file_list(request, date=None):
    template_name = 'index.html'
    get_files = os.listdir(settings.FILES_PATH)
    info_files = {}
    for item in get_files:
        info_files[item] = {'ctime': creation_date(f'{settings.FILES_PATH}\\{item}')},\
                           {'mtime': modification_date(f'{settings.FILES_PATH}\\{item}')}
    server_list = []
    for item_name in get_files:
        server_dict = {}
        server_dict['name'] = item_name
        server_dict['ctime'] = info_files[item_name][0]['ctime']
        server_dict['mtime'] = info_files[item_name][1]['mtime']
        if not date:
            server_list.append(server_dict)
        if date:
            filter_date = datetime.strptime(date, '%Y-%m-%d').date()
            if filter_date == server_dict['mtime'].date():
                server_list.append(server_dict)

    context = {'files': server_list, 'date': date}
    return render(request, template_name, context)


def file_content(request, name=None):
    if name in os.listdir(settings.FILES_PATH):
        with open(f'{settings.FILES_PATH}\\{name}', 'r') as data_file:
            content_data = data_file.read()
            return render(
                request, 'file_content.html',
                context={'file_name': f'{name}', 'file_content': content_data}
            )
