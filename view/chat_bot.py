from flask import Blueprint,render_template,Flask,request,redirect,session,json,current_app as app
import hashlib,time
from models import db, Class
from public import r

chat_bot=Blueprint('chat_bot',__name__)

@chat_bot.route('/chat_bot')
def index():
	return render_template('/chat_bot.html')
@chat_bot.route('/chat',methods=['GET'])
def chat():

	return r({},0,'添加成功')