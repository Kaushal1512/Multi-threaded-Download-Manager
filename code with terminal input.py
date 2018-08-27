#Note: This code will not work on online IDE
 
# Importing the required packages
import click
import requests
from tqdm import tqdm
import threading
 
# The below code is used for each chunk of file handled
# by each thread for downloading the content from specified 
# location to storage
def Handler(start, end, url, filename):
    
    # specify the starting and ending of the file
    headers = {'Range': 'bytes=%d-%d' % (start, end)}
 
    # request the specified part and get into variable    
    r = requests.get(url, headers=headers, stream=True)
 
    # open the file and write the content of the html page 
    # into file.
    with open(filename, "r+b") as fp:
     
        fp.seek(int(start))
        var = fp.tell()
        fp.write(r.content)
 
@click.command(help="It downloads the specified file with specified name")
@click.option('--number_of_threads',default=4, help="No of Threads")
@click.option('--name',type=click.Path(),help="Name of the file with extension")
@click.argument('url_of_file',type=click.Path())
@click.pass_context


def download_file(ctx,url_of_file,name,number_of_threads):
    r = requests.head(url_of_file)
    file_name = ''
    if name:
        file_name = name
    else:
        file_name = url_of_file.split('/')[-1]
    try:
        file_size = int(r.headers['content-length'])
        #print("Hello")
    except:
        print ("Please enter a valid URl")
        return

    part = int(file_size) / number_of_threads
    #	print(part);
    fp = open(file_name, "wb")
    fp.write(b'\0' * file_size)
    fp.close()


    for i in tqdm(range(number_of_threads)):
        start = part * i
        end = start + part
    
        # create a Thread with start and end locations
        t = threading.Thread(target=Handler,
            kwargs={'start': start, 'end': end, 'url': url_of_file, 'filename': file_name})
        t.setDaemon(True)
        t.start()


    main_thread = threading.current_thread()
    for t in tqdm(threading.enumerate()):
        if t is main_thread:
            continue
        t.join()
    print ('%s downloaded' % file_name)
 
if __name__ == '__main__':
    download_file(obj={})
