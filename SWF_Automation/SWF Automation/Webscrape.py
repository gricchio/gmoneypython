'''
Created on Jan 31, 2017

@author: riccga
'''
import scrapy
import os
from __builtin__ import file


new_project_location = r'C:\Users\riccga\Google Drive\Python Test Materials\Webscrape Project'
crawl_url = "https://thenewbowston.com"
project_name = 'thenewboston'
os.chdir(new_project_location)

def write_file(path,data):
    f = open(path)
    f.write(data)
    d.close()

def append_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')
    
def delete_file_contents(path):
    with open(path,'w'):
        pass

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project ' + directory)
        os.makedirs(directory)
    return

def create_data_files(project_name,crawl_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue,crawl_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')
    return

create_data_files(project_name, crawl_url)





