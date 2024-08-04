# -*- coding: utf-8 -*-
# Standard library imports.
import sqlite3,os,json,re,requests
# Related third party imports.
from flask import Flask, Blueprint,render_template,request,jsonify,url_for,current_app
from loguru import logger
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama
from werkzeug.utils import secure_filename
# Local application/library specific imports.


bp = Blueprint("weibo_UI", __name__, url_prefix='/weibo_UI',static_folder='static',template_folder='templates')

@bp.route('/index' )
def show():
    username="lnform"
    return render_template('index.html',username=username)

@bp.route('/choose_model')
def choose_model():
    username="lnform"
    return render_template('choose_model.html',username=username)
        
@bp.route('/choose_model_post',methods=["POST"])
def choose_model_post():
    if request.method == "POST":
        type_name=request.form.get('type_name')
        print('+++',type_name)
        choose_dict={}
        choose_dict['result']=1
        return jsonify(choose_dict)
        
@bp.route('/model_run',methods=["POST"])
def model_run():
    if request.method == "POST":
        data = request.get_json()
        type_name=data['type_name']
        model_select=data['model_name']
        split_document=data['split_document']
        vector_select=data['vector_select']
        query=data['query']
        print(query)
        #json_1 = request.json
        #print(json_1)
        #split
        url = 'http://127.0.0.1:4010/private/inference'
        json_data = {
            "messages": [
                {
                  "role": "user",
                  "content": query
                }
            ],
            "inference_service": "ollama",
            "model": "qwen2:1.5b-instruct-fp16",
            "max_tokens": 4096,
            "stream": False,
            "temperature": 0.8,
            "timeout": 60
        }
        # 发送请求并存储响应
        response = requests.post(url, json=json_data)
        print(response.json())
        # 检查响应状态代码
        res=''
        answer=response.json()
        if answer['message'] == 'success':
            # 打印响应文本
            res=answer['data']['result']
        choose_dict={}
        choose_dict['result']=1
        choose_dict['content']=res
        #choose_dict['content']=response
        return jsonify(choose_dict)
    
@bp.route('/upload',methods=['GET','POST'])
def upload():
    username='lnform'
    print('111')
    print('111',request.method)
    if request.method == "POST":
        f = request.files['file']
        _filename_ascii_add_strip_re = re.compile(r'[^A-Za-z0-9_\u4E00-\u9FBF\u3040-\u30FF\u31F0-\u31FF.-]')
        filename = str(_filename_ascii_add_strip_re.sub('', '_'.join( # 新的正则
                f.filename.split()))).strip('._')
        filename=secure_filename(filename)
        save_path=os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        print(save_path)
        content="1234"
        with open(save_path,"w") as fp:
	        fp.write(content)
        #f.save(save_path)
        return 'upload success'
    return render_template('upload_Document.html',username=username)

@bp.route('/self_media',methods=["POST","GET"])
def self_media():
    if request.method == "POST":
        data = request.get_json()
        type_name=data['type_name']
        model_select=data['model_name']
        split_document=data['split_document']
        vector_select=data['vector_select']
        title=data['title']
        thumb_media_id=data['thumb_media_id']
        query='以'+str(title)+'为题，写一篇文章'
        url = 'http://127.0.0.1:4010/private/inference'
        json_data = {
            "messages": [
                {
                  "role": "user",
                  "content": query
                }
            ],
            "inference_service": "ollama",
            "model": "qwen2:1.5b-instruct-fp16",
            "max_tokens": 4096,
            "stream": False,
            "temperature": 0.8,
            "timeout": 60
        }
        # 发送请求并存储响应
        response = requests.post(url, json=json_data)
        print(response.json())
        # 检查响应状态代码
        res=''
        answer=response.json()
        choose_dict={}
        choose_dict['result']=0
        if answer['message'] == 'success':
            # 打印响应文本
            res=answer['data']['result']
            url_self_media= 'http://127.0.0.1:6050/wpp/draft_add'
            json_data_self_media = {
                "title": title,
                "content": res,
                "thumb_media_id": thumb_media_id
            }
            # 发送请求并存储响应
            response_self_media = requests.post(url_self_media, json=json_data_self_media)
            self_media_res=response_self_media.json()
            if self_media_res['success']:
                choose_dict['result']=1
        choose_dict['content']=res
        #choose_dict['content']=response
        return jsonify(choose_dict)
    username="lnform"
    return render_template('self_media.html',username=username)
  
@bp.route('/submit_kb',methods=["POST","GET"])
def submit_kb():
    if request.method == "POST":
        data = request.get_json()
        formFile=data['formFile']
        model_select=data['model_select']
        mvector_select=data['mvector_select']
        desc=data['desc']
        url = 'http://127.0.0.1:4010/private/inference'
        json_data = {
            
        }
        # 发送请求并存储响应
        response = requests.post(url, json=json_data)
        print(response.json())
        # 检查响应状态代码
        res=''
        answer=response.json()
        choose_dict={}
        choose_dict['result']=0
        
        choose_dict['content']=res
        #choose_dict['content']=response
        return jsonify(choose_dict)
    username="lnform"
    return render_template('upload_Document.html',username=username)