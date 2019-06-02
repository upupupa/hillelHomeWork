#!/bin/usr/python3
# -*- coding: utf-8 -*-

"""
4. Создать папку и в ней для каждого города который встретится в логах, создать файл (вида “new_jersey.tsv”) 
в котором вывести все поисковые запросы и количество уникальных user_id с которыми они встречались (через \t)
"""

import csv
import os
import os.path
from time import time

def cache(func):
    cache.cities = []
    cache.result = {}
    """общий вид {city: {search_request: unique_users} => unique_users:list,
    количество уникальных пользователей len(unique_users)"""
    def wrapper(file_path):
        func(file_path)
    return wrapper

@cache
def parcer(file_path):
    start_time = time()
    fulldata = [] 
    with open(file_path, "r") as f:
        for line in f:
            data = line.split("\t")
            data[-1] = data[-1].strip()
            fulldata.append(data)
        f.close()
    #0 - platform, 1 - age, 2 - sex, 3 - city, 4 - user_id, 5 - search request, 6 - domain, 7 - url, 8 - type(what is it??)
    for data in fulldata:
        user_id = data[4]
        search_request = data[5]
        city = data[3]
        if city not in cache.cities:
            cache.result[city] = {}
            cache.result[city][search_request] = []
            cache.result[city][search_request].append(user_id)
            cache.cities.append(city)
        elif search_request not in cache.result[city].keys():
            cache.result[city][search_request] = []
            cache.result[city][search_request].append(user_id)
        elif user_id not in cache.result[city][search_request]:
            cache.result[city][search_request].append(user_id)
    print("file {} parsed in {:0.2f} seconds".format(file_path, (time()-start_time)))

def writer():
    try:
        os.mkdir("./output/")
    except FileExistsError:
        pass
    for city in cache.cities:
        with open("./output/{}.tsv".format(city), 'wt') as outfile:
            writer = csv.writer(outfile, delimiter="\t")
            for search in cache.result[city].keys():
                unique = len(cache.result[city][search])
                writer.writerow([search, unique])
            outfile.close()
        print("file {}.tsv has been written".format(city))

def file_searcher(fileformat, search_directory):
    """
    searches files in directory and sub directories
    
    returns list of paths to files
    
    params:
    fileformat - file format to search example: ".txt"
    search_directory - path to directory to search "./"
    """
    dirpaths = []
    for dirpath, _, filenames in os.walk(search_directory):
        for filename in [f for f in filenames if f.endswith(fileformat)]:
            dirpaths.append(os.path.join(dirpath, filename))
    return dirpaths

if __name__ == "__main__":
    paths = file_searcher(".txt", "./")
    for path in paths:
        parcer(path)
    writer()