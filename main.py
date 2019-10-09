# -*- coding: UTF-8 -*-

import dataformat

import requests,json,os,re,shutil
#from jinja2 import FileSystemLoader,Environment
#import tarfile,zipfile
import fire
import datetime


base_url = "http://127.0.0.1:8000/cmdb"


key="7cce374700bbff24f838f5a744ad0463"

client_version = "0.0.1"


def version():
    '''
    查询版本号
    :return:
    '''
    url = base_url + "/get_version"
    r = requests.get(url)
    back_data = r.json()
    back_data['client_version'] = client_version
    # print(type(back_data))
    print(back_data)

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj,datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def addMachine(fname):
    '''
    添加机器:
    :param fname: fname--文件名，add_data目录下的machinedata.yaml文件名
    :return:
    '''
    data = dataformat.yamlFileToBaseData(fname)
    data['key'] = key
    # print(data)
    url = base_url + "/machine/add"
    r = requests.post(url, json.dumps(data))
    print(r.text)


def queryMachine(**kwargs):
    '''
    查询机器
    :param kwargs: 目前查询所有
    :return:
    '''
    # url = base_url + "/add_task/"
    # r = requests.post(url, ddata)
    # print(r.text)
    url = base_url + "/machine/query"
    kwargs['key'] = key
    r = requests.post(url, kwargs)
    print(r.text)


def deleteMachine(name):
    '''
    删除项目
    :param pname: pname--项目名，指定删除哪个项目名
    :return: nothing
    '''
    url = base_url + "/machine/delete"
    r = requests.post(url, {'name': name, 'key': key})
    print(r.text)


def editMachine(fname):
    data = dataformat.yamlFileToBaseData(fname)
    data['key'] = key
    url = base_url + "/machine/edit"
    r = requests.post(url, json.dumps(data))
    print(r.text)


def addProject(fname):
    data = dataformat.yamlFileToBaseData(fname)
    data['key'] = key
    # print(data)
    url = base_url + "/project/add"
    r = requests.post(url, json.dumps(data))
    print(r.text)


def queryProject(**kwargs):
    url = base_url + "/project/query"
    kwargs['key'] = key
    r = requests.post(url, kwargs)
    print(r.text)


def deleteProject(name):
    url = base_url + "/project/delete"
    r = requests.post(url, {'name': name, 'key': key})
    print(r.text)


def editProject(fname):
    data = dataformat.yamlFileToBaseData(fname)
    data['key'] = key
    url = base_url + "/project/edit"
    r = requests.post(url, json.dumps(data))
    print(r.text)


def addApp(fname):
    data = dataformat.yamlFileToBaseData(fname)
    data['key'] = key
    # print(data)
    url = base_url + "/app/add"
    r = requests.post(url, json.dumps(data))
    print(r.text)


def queryApp(**kwargs):
    url = base_url + "/app/query"
    kwargs['key'] = key
    r = requests.post(url, kwargs)
    print(r.text)


def deleteApp(name):
    url = base_url + "/app/delete"
    r = requests.post(url, {'name': name, 'key': key})
    print(r.text)


def editApp(fname):
    data = dataformat.yamlFileToBaseData(fname)
    data['key'] = key
    url = base_url + "/app/edit"
    r = requests.post(url, json.dumps(data))
    print(r.text)


def addRule(fname):
    data = dataformat.yamlFileToBaseData(fname)
    data['key'] = key
    # print(data)
    url = base_url + "/rule/add"
    r = requests.post(url, json.dumps(data))
    print(r.text)


def queryRule(**kwargs):
    url = base_url + "/rule/query"
    kwargs['key'] = key
    r = requests.post(url, kwargs)
    print(r.text)


def deleteRule(name):
    url = base_url + "/rule/delete"
    r = requests.post(url, {'name': name, 'key': key})
    print(r.text)


def editRule(fname):
    data = dataformat.yamlFileToBaseData(fname)
    data['key'] = key
    url = base_url + "/rule/edit"
    r = requests.post(url, json.dumps(data))
    print(r.text)


def getProjectfile(id):
    url = base_url + "/project/file"
    r = requests.post(url, {'id': id, 'key': key})
    data = r.json()
    # print(type(data))
    if data.get('errorNo') == 0:
        fdata = data['results']['data'][0]
        # print(data['results']['data'][0])
        dataformat.makeYamlFile(fdata, 'temp/project_file.yaml')
        print(r.text)
    else:
        print(r.text)


def getMachinefile(id):
    url = base_url + "/machine/file"
    r = requests.post(url, {'id': id, 'key': key})
    data = r.json()
    # print(type(data))
    if data.get('errorNo') == 0:
        fdata = data['results']['data'][0]
        # print(data['results']['data'][0])
        dataformat.makeYamlFile(fdata, 'temp/machine_file.yaml')
        print(r.text)
    else:
        print(r.text)


def getAppfile(id):
    url = base_url + "/app/file"
    r = requests.post(url, {'id': id, 'key': key})
    data = r.json()
    # print(type(data))
    if data.get('errorNo') == 0:
        fdata = data['results']['data'][0]
        # print(data['results']['data'][0])
        dataformat.makeYamlFile(fdata, 'temp/app_file.yaml')
        print(r.text)
    else:
        print(r.text)


def getRulefile(id):
    url = base_url + "/rule/file"
    r = requests.post(url, {'id': id, 'key': key})
    data = r.json()
    # print(type(data))
    if data.get('errorNo') == 0:
        fdata = data['results']['data'][0]
        # print(data['results']['data'][0])
        dataformat.makeYamlFile(fdata, 'temp/rule_file.yaml')
        print(r.text)
    else:
        print(r.text)


def export(**kwargs):
    url = base_url + "/export"
    if kwargs.get('help'):
        kwargs.pop('help')
    r = requests.post(url, kwargs)
    if r.headers.get("Content-Disposition") is not None:
        zip_file_name = r.headers["Content-Disposition"].split("=")[-1].strip()
        path = 'data/' + zip_file_name
        with open(path, "wb") as fw:
            for chunk in r.iter_content(1024):
                fw.write(chunk)
    else:
        print(r.text)


if __name__ == "__main__":
  fire.Fire()

