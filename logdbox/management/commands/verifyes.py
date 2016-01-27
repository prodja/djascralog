# coding=utf-8
from sys import argv
from os import getcwd, access, R_OK
from os.path import isdir
from re import search

#возвращает рабочие пути - иначе - сообщение об ошибке
def verify_pathes(argv,name_new_zip='new_zip.zip'):

	pathes={}
	pathes['path']=''
	pathes['name']=''
	pathes['cols_of_log']=''

	if(len(argv)==3):
		pathes['path'] = getcwd()+'/'
	elif(len(argv)>3):
		if(access(argv[3],R_OK)==True and isdir(argv[3])==True):
			pathes['path'] = argv[3]+'/'
			if(len(argv)==5):
				finded_argv=search('(ip|date|code|time)',argv[4])
				if(finded_argv!=None):
					pathes['cols_of_log']=argv[4]
				else:
					print 'параметр после архива не является путем или столбцом лога'
					exit()

		else:
			pathes['path']=getcwd()+'/'
			finded_argv=search('(ip|date|code|time)',argv[3])
			if(finded_argv!=None):
				pathes['cols_of_log']=argv[3]
			else:
				print 'параметр после архива не является путем или столбцом лога'
				exit()
	try:
		pathes['name']=argv[2]
	except IndexError:
		print u'не задано имя архива'
		return 0
	pathes['name_new_zip']=name_new_zip
	return pathes