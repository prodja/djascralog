#! coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from log_to_xl import Log_to_xl #класс перевода данных с файла-лога в xlsx-файл"""
from verifyes import verify_pathes #функции проверки имен и путей файлов, архивов"""
from dbox import upload_to_dropbox #функции загрузки данных с локального компьютера на dropbox"""
from sys import argv
from os import remove

""" имя команды = имя файла, в котором есть класс Command"""

class Command(BaseCommand):

	def handle(self, *args, **options):

		"""проверяем введенные с консоли имена/пути"""

		pathes=verify_pathes(argv)

		"""если все пути и имена корректны"""

		if(pathes!=0):

			"""создаем объект класса перевода логов в эксель"""

			Logxl=Log_to_xl(pathes['name'],pathes['path'],pathes['cols_of_log'])
			
			"""создаем списки файлов с распаковкой их из архива(переводим там лог в xl)"""

			list_of_xl_files=Logxl.hash_data_to_xls()
			list_of_files=Logxl.files_of_zip()

			"""записываем файлы из полученных списков в новый архив, новый архив создается в момент первой записи, открывается и закрывается после каждой записи"""

			Logxl.write_files_to_zip(list_of_xl_files,Logxl.zip_path + pathes['name_new_zip'],'w')
			Logxl.write_files_to_zip(list_of_files,Logxl.zip_path + pathes['name_new_zip'],'a')

			"""удаляем распакованные файлы - те, что переносили в новый архив"""

			Logxl.remove_extracted_files(list_of_xl_files)
			Logxl.remove_extracted_files(list_of_files)

			"""загружаем новый архив в dropbox"""

			upload_to_dropbox(Logxl.zip_path,pathes['name_new_zip'])
			
			"""удаляем новый архив из локального компьютера"""

			remove(Logxl.zip_path + pathes['name_new_zip'])
		else:
			print 'программа завершена по причине ошибок в указании путей'
			exit()
			

		"""говорим джанге, что прибавили еще аргумент в зависимости от их переданного количества в bash"""

	def add_arguments(self, parser):
		parser.add_argument('zip', nargs='+')
		if(len(argv)==5):
			parser.add_argument('path', nargs='+')
		elif(len(argv)==6):
			parser.add_argument('format', nargs='+')