from flask import Flask,session,request,redirect
from view.account import account#账号相关
from view.users import users#教师相关
from view.myclass import myclass#班级
from view.student import student#学生
from view.score import score#分数
from models import db
def create_app():
	app=Flask(__name__)
	app.config.from_object('config.Dev')
	
	db.init_app(app)

	app.register_blueprint(account)
	app.register_blueprint(users)
	app.register_blueprint(myclass)
	app.register_blueprint(student)
	app.register_blueprint(score)
	@app.before_request
	def check_need_login():#判断登录
		# print(request.endpoint)
		if 'logged_in' not in session and request.endpoint not in ('account.login','static'):
			return redirect('/login')
	return app


if __name__ == '__main__':
	app=create_app()
	app.run()