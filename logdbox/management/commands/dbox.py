# coding=utf-8
from dropbox import session, client, rest
from os import path

def upload_to_dropbox(what_upload_path,what_upload_name,APP_KEY="mbetl5jbnb0hjk6",APP_SECRET="e86wepfxsw8acpd"):

	sess = session.DropboxSession(APP_KEY, APP_SECRET, "dropbox")
	request_token = sess.obtain_request_token()
	try:
		url = sess.build_authorize_url(request_token)
	except urllib3.exceptions.MaxRetryError:
		print 'не удалось установить соединение с dropbox, программа прервана'
		return 0

	#подтверждение передачи нового архива на dropbox
	print u"Перейдите по ссылке ", url," и нажмите 'можно' для закачки на дропбокс, затем здесь нажмите на 'enter'"
	try:
		raw_input()
	except EOFError:
		return u"Вы нажали не 'enter', авторизация в dropbox не произошла, программа прервана"

	#закачка нового архива на dropbox
	try:
		access_token = sess.obtain_access_token(request_token)
		ACCESS_KEY = access_token.key
		ACCESS_SECRET = access_token.secret
		#sess = session.DropboxSession(APP_KEY, APP_SECRET, "dropbox")
		sess.set_token(ACCESS_KEY, ACCESS_SECRET)
		client_upload = client.DropboxClient(sess)

		size = path.getsize(what_upload_path + what_upload_name)
		uploader = client_upload.get_chunked_uploader(open(what_upload_path + what_upload_name, 'rb'), size)
		while uploader.offset < size:
			upload = uploader.upload_chunked()
		uploader.finish("/" + path.basename(what_upload_path + what_upload_name), True)
	except rest.ErrorResponse:
		print u'Ошибка авторизации в dropbox (возможно не перешли по ссылке, не нажали на кнопку "можно"), программа прервана'
	print u'Данные переданы на dropbox'
	return 1