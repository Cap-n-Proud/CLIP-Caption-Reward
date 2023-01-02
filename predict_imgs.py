import requests
import json
import os

# path = "/home/paolo/NAS/Photos/001-Process"
path = "/mnt/Photos/005-PhotoBook/"

search_ext = [".jpg", ".JPG", ".png"]

url = 'http://192.168.1.121:9111/predictions'
# img="http://192.168.1.140:8089/005-PhotoBook/2022/01/_DSC1392.JPG"
img_base_url="http://192.168.1.163:8089"
headers = {'content-type': 'application/json'}

# payload='{"input": {"image":"'+ str(img) +'" ,"reward": "clips_grammar"}}'


# cd to photo dirname
# python3 -m http.server 8089 --bind 192.168.1.163
files_scanned = 0
files_processed = 0


def walk_through_files(path, search_ext):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if (os.path.splitext(filename)[1]).lower() in search_ext:
                yield os.path.join(dirpath, filename)


fpath = list(walk_through_files(path, search_ext))

print("Total files: " + str(len(list(fpath))))
# print(path, search_ext, list(fpath))

for fname in fpath:
    # print("----------------------------------------------", fname)
    try:
        payload='{"input": {"image":"'+ str(img_base_url)+str(fname) +'" ,"reward": "clips_grammar"}}'
        print("payload", payload)
        r = requests.post(url, headers=headers,data=payload).content
        caption=json.loads(r.decode('utf-8'))
        print(caption['output'])

        command = "exiftool -overwrite_original -Caption-Abstract='" + str(caption['output']) + "' '" + fname + "'"
        print(command)
        res = os.system(command)

        # print("copy_tags_to_IPTC")
        # media.copy_tags_to_IPTC(fname)

    except Exception as e:
        print(e)
