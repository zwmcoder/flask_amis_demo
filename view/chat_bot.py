from flask import Blueprint,render_template,Flask,request,redirect,session,json,current_app as app
import hashlib,time
from models import db, Class
from public import r

chat_bot=Blueprint('chat_bot',__name__)

@chat_bot.route('/chat_bot')
def index():
	return render_template('/chat_bot.html')
@chat_bot.route('/myclass',methods=['POST'])
def add_class():
	data = request.get_data()
	j_data =  json.loads(data)
	user=db.session.query(Class).filter_by(name=j_data['name']).first()
	if user is not None:
		return r({},0,'',{'admin':'名称已存在'})
	
	cl = Class(j_data['t_id'], j_data['name'],int(time.time()),0)
	db.session.add(cl)
	db.session.commit()
	return r({},0,'添加成功')