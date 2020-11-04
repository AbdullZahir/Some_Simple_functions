import os
import shutil

folder1=os.lisdir('path to your imagefolder')
folder2=os.listdir('path to your xml labeled folder')

cnt= 0

for item1 in folder1: 
	for item2 in folder2: 
		if cnt<2001: 
			if(item1.strip('.jpg')==item2.strip('.xml')):
				shutil.copy('path to your imagefolder'+item1,'destination folder for image folder')
				shutil.copy('path to your xml folder'+item2,'destination folder for xml files') 
