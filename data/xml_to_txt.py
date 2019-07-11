import xml.dom.minidom
import  os

#bug = 0
def opera_file(file):
    '''读取xml文件信息'''
    dom = xml.dom.minidom.parse(file)
    root = dom.documentElement
    name = root.getElementsByTagName('name')
    xmin = root.getElementsByTagName('xmin')
    ymin = root.getElementsByTagName('ymin')
    xmax = root.getElementsByTagName('xmax')
    ymax = root.getElementsByTagName('ymax')
    i = 0
    message = ''
    while i <= 2:
        if name[i].firstChild.data == 'cola':
            message = message + ' ' + '0' + ' ' + xmin[i].firstChild.data + ' '\
                      + ymin[i].firstChild.data + ' ' + xmax[i].firstChild.data + ' ' +\
                      ymax[i].firstChild.data
        elif name[i].firstChild.data == 'kangshifu':
            message = message + ' ' + '1' + ' ' + xmin[i].firstChild.data + ' '\
                      + ymin[i].firstChild.data + ' ' + xmax[i].firstChild.data + ' ' +\
                      ymax[i].firstChild.data
        elif name[i].firstChild.data == 'yogurt':
            message = message + ' ' + '2' + ' ' + xmin[i].firstChild.data + ' '\
                      + ymin[i].firstChild.data + ' ' + xmax[i].firstChild.data +  ' '+\
                      ymax[i].firstChild.data
        else:
            pass
        i+=1
    return message

#print(os.path.abspath('.'))
    
path = os.getcwd()
filelist = os.listdir(path)
#print(filelist)

with open("train.txt",'w') as file_object:
    for file in filelist:
        if file[-4:] == '.xml':
#            bug+=1
#            print(bug)
            line = opera_file(file)
            file_object.write( '../data/' + str(file[:-4]) + '.jpg' + str(line) + '\n')

    
#while i 
#dom = xml.dom.minidom.parse()
