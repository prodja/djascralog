# coding=utf-8
from os import remove,getcwd,path
from zipfile import ZipFile,is_zipfile
from openpyxl import Workbook
from re import search
from sys import exit

class Log_to_xl:
	def __init__(self, zip_name, zip_path, cols_of_log):
		self.zip_name=zip_name #путь к архиву
		self.zip_path=zip_path #имя архива
		try:
			self.zip_archive=ZipFile(self.zip_path + self.zip_name,'r')# архив, с которого будем брать логи, файлы
		except IOError:
			print u'В заданном каталоге zip не найден' + self.zip_path +'|'+ self.zip_name
			exit()
		self.dict_cells={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
		self.dict_templates={'ip':'(.*(?= - -))','date':'((?<=\[).*(?=:\d\d:\d\d:\d\d))','time':'(?<=:)\d\d:\d\d:\d\d','path':'\"(.+)\"','code':'((?<= )\d\d\d(?= \d*))','size_response':'((?<= \d\d\d )\d+)'}# словарь соответствия столбцов и поиска их данных
		if(cols_of_log!=''):
			self.format_str=cols_of_log
		else:
			self.format_str='ip-date-code'

	#Преобразование данных входного лога в хеш-массив списков искомых лога(ip, date  и т.д.)	
	def parse_log_data_to_hash(self,file_log):
		try:
			list_format_str=self.format_str.split('-')
		except IndentationError:
			print "функия:parse_log_data_to_hash(): Невозможно создать список из файла лога ="+file_log 
			exit()
		hash_results=[]

		try:
			log=open(self.zip_path+file_log)
		except IOError:
			print 'не найден файл ='+file_log
			exit()

		for need_col in list_format_str:
			x=[]
			x.append(need_col)
			hash_results.append(x)
		iterator_finded_str=0

		for line in log:
			if(len(line)>1):
				for need_col in hash_results:
					m = search(self.dict_templates[need_col[0]],line)
					if(m!=None):
						need_col.append(m.group())
					else: 
						need_col.append('')
			iterator_finded_str=iterator_finded_str+1	
		return hash_results

#загрузка списков данных с лога в xlsx файл 
	def hash_data_to_xls(self):
		list_zip_files=self.zip_archive.namelist()
		#если в заданном архиве есть файлы
		if(len(list_zip_files)>0):
			out_list_xl=[]
			access_found=False
			for file_zip in list_zip_files:
				#если есть файл с access: переносим из него данные в xlsx
				if(file_zip.find('access')>-1):
					access_found=True
					self.zip_archive.extract(file_zip,self.zip_path)
					hash_data=self.parse_log_data_to_hash(file_zip)
					out_xlsx = Workbook()
					curr_sheet = out_xlsx.active
					try:
						i_cells=0
						for key_hash_xlsx in hash_data:
							key_cell_1=self.dict_cells[i_cells]
							i_cells+=1
							i=1
							for key_hash_datas in key_hash_xlsx:
								curr_sheet[key_cell_1+str(i)]=key_hash_datas
								i+=1		
					except TypeError:
						print 'не удалось преобразовать лог в списки'
						return 0;
					out_xlsx.save(self.zip_path+file_zip+".xlsx")
					out_list_xl.append(file_zip+".xlsx")
					remove(self.zip_path+file_zip)		
		return out_list_xl

#список извлеченных файлов (не access)
	def files_of_zip(self):
		list_zip_files=self.zip_archive.namelist()
		out_list=[]
		for file_zip in list_zip_files:
			if(file_zip.find('access')==-1):
				self.zip_archive.extract(file_zip,self.zip_path)

		if(len(list_zip_files)>0):
			for file_zip in list_zip_files:
				if(file_zip.find('access')==-1):
					out_list.append(file_zip)

		return out_list

#запись списка файлов в архив
	def write_files_to_zip(self,list_of_files,path_new_archive,mode):
		arhiv=ZipFile(path_new_archive,mode)
		for file_of_list in list_of_files:
			arhiv.write(self.zip_path+file_of_list,file_of_list)
		arhiv.close()
		return 0

#удаление списка файлов
	def remove_extracted_files(self,list_of_files):
		for file_of_list in list_of_files:
			remove(self.zip_path+file_of_list)
		return 0



