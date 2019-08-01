import re  # 导入正则表达式模块
import requests  # python HTTP客户端 编写爬虫和测试服务器经常用到的模块
import random  # 随机生成一个数，范围[0,1]
import os #导入OS包


# 定义函数方法
def spiderPic(html, keyword, pathword):
    print('正在查找 ' + keyword + ' 对应的图片,下载中，请稍后......')
    list = re.findall('"objURL":"(.*?)"', html, re.S)
    #print(list)
    for addr in list:  # 查找URL
        print('正在爬取URL地址：' + str(addr)[0:30] + '...')  # 爬取的地址长度超过30时，用'...'代替后面的内容

        try:
            pics = requests.get(addr, timeout=20)  # 请求URL时间（最大10秒）
        except requests.exceptions.ConnectionError:
            print('您当前请求的URL地址出现错误！')
            continue
        fq = open('D:\\img\\'+pathword+'\\' + (keyword + '_' + str(random.randrange(0, 1000, 4)) + '.jpg'), 'wb')  # 下载图片，并保存和命名
        fq.write(pics.content)#存入图片到路径对应文件夹中
        fq.close()


# python的主方法
if __name__ == '__main__':
    cur_dir = 'D:\\img'
    flie = input('输入一个您要保存图片的文件夹名称：')
    path = 'D:\\img\\'+ flie + ''
    y = os.path.exists(path)#查看路径是否存在
    if y == 1:
        print('该文件已存在！')
    else:
        if os.path.isdir(cur_dir):
            os.mkdir(os.path.join(cur_dir, flie))#创建路径下输入文件夹名称+
    word = input('请输入你要搜索的图片关键字：')
    folder_name = word
    result = requests.get(
        'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn=')

# 调用函数
spiderPic(result.text, word, flie)
