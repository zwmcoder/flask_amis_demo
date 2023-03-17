from flask import Flask,session,request,redirect
from view.account import account#账号相关
from view.chat_bot import chat_bot
from models import db
def create_app():
	app=Flask(__name__)
	app.config.from_object('config.Dev')
	
	db.init_app(app)

	app.register_blueprint(account)
	app.register_blueprint(chat_bot)
	@app.before_request
	def check_need_login():#判断登录
		# print(request.endpoint)
		if 'logged_in' not in session and request.endpoint not in ('account.login','static'):
			return redirect('/login')
	return app


if __name__ == '__main__':
	app=create_app()
	app.run()