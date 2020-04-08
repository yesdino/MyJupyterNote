import os

def rename_func(path):
    if os.path.isfile(path):
        rename_file(path)
    else:
        for sub_path in os.listdir(path):
            # print(sub_path)
            rename_func(os.path.join(path, sub_path))

def rename_file(file):
    tmp = file.split('.')
    # print(tmp)
    fileNew = '.'.join([tmp[0], tmp[1].lower()])
    # if(file.find(".JPG")):
    #     fileNew = str(file).replace(".JPG", ".jpg")
    # if(file.find(".PNG")):
    #     fileNew = str(file).replace(".PNG", ".png")

    print("[Old]: {} [New]: {}".format(file, fileNew))
    if(fileNew != file):
        print('replace')
        os.rename(file, fileNew)


path2 = "/home/dino/jupyter_file/images/"


rename_func(path2)