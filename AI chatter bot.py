
# coding: utf-8

# In[ ]:


from urllib import request
from lxml import etree
import re
import spacy



#利用爬虫获取网页信息
#实时获取，股票信息
#web_info = request.urlopen('https://money.cnn.com/data/markets/').read().decode('gbk')
web_info = request.urlopen('https://money.cnn.com/data/us_markets/').read()
#字符串转换为html对象
web_info = etree.HTML(web_info)
#根据网页信息，name of the stock, tbody 不要
#//div[@id='wsod_marketMoversContainer']/table/tbody/tr[2]/td/a/text()
#price
#//div[@id='wsod_marketMoversContainer']/table/tbody/tr[2]/td[2]/span/text()
#change
#//div[@id='wsod_marketMoversContainer']/table/tbody/tr[2]/td[3]/span/span/text()
#percentage change
#//div[@id='wsod_marketMoversContainer']/table/tbody/tr[2]/td[4]/span/span/text()

#创建列表，保存网页上的各支股票数据
item_stock = []
for each in web_info.xpath("//div[@id='wsod_marketMoversContainer']/table//tr"):
#创建字典
    item_stock_each = {}
    if each.xpath("./td/a/text()") != [] :
        item_stock_each['stock_name'] = each.xpath("./td/a/text()")
        item_stock_each['stock_price'] = each.xpath("./td[2]/span/text()")
        item_stock_each['stock_change'] = each.xpath("./td[3]/span/span/text()")
        item_stock_each['stock_percentage'] = each.xpath("./td[4]/span/span/text()")
        item_stock.append(item_stock_each)






nlp = spacy.load('en_core_web_md')
# Define included entities
include_entities = ['ORG']
# Define extract_entities()，利用spacy提取用户所想找的股票名称，打上ORG的标签
def extract_entities(message):
    ents = dict.fromkeys(include_entities)
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ in include_entities:
            ents[ent.label_] = ent.text
    return ents




def send_message(policy, state, message):
    new_state, response = respond(policy, state, message)
    friend.send(u"{}".format(response))
    return new_state




def respond(policy, state, message):
    (new_state, response) = policy[(state, interpret(message))]
    return new_state, response



#状态机的状态
def interpret(message):
    msg = message
    if 'stock' in msg:                         #关键词 stock
        return 'stock'
    if item_stock[0]['stock_name'][0] in msg:  #关键词：各个股票的名称缩写（要求大写）
        return 'specify_stock'
    if item_stock[1]['stock_name'][0] in msg:
        return 'specify_stock'
    if item_stock[2]['stock_name'][0] in msg:
        return 'specify_stock'
    if item_stock[3]['stock_name'][0] in msg:
        return 'specify_stock'
    if item_stock[4]['stock_name'][0] in msg:
        return 'specify_stock'
    if item_stock[5]['stock_name'][0] in msg:
        return 'specify_stock'
    if item_stock[6]['stock_name'][0] in msg:
        return 'specify_stock'
    if item_stock[7]['stock_name'][0] in msg:
        return 'specify_stock'
    if item_stock[8]['stock_name'][0] in msg:
        return 'specify_stock'
    if item_stock[9]['stock_name'][0] in msg:
        return 'specify_stock'
    if 'job' in msg:                          #关键词 job
        return 'ask_explanation_1'
    if 'have' in msg:                          #关键词 have
        return 'ask_explanation_2'
    if 'yes' in msg:                           #关键词 yes
        return 'agree'
    return 'none'


#用于判断是在尬聊还是想问股票
def another_interpret(message):
    msg = message
    if 'stock' in msg:                         #关键词 stock
        return 'stock'
    if item_stock[0]['stock_name'][0] in msg:  #关键词：各个股票的名称缩写（要求大写）
        return 'stock'
    if item_stock[1]['stock_name'][0] in msg:
        return 'stock'
    if item_stock[2]['stock_name'][0] in msg:
        return 'stock'
    if item_stock[3]['stock_name'][0] in msg:
        return 'stock'
    if item_stock[4]['stock_name'][0] in msg:
        return 'stock'
    if item_stock[5]['stock_name'][0] in msg:
        return 'stock'
    if item_stock[6]['stock_name'][0] in msg:
        return 'stock'
    if item_stock[7]['stock_name'][0] in msg:
        return 'stock'
    if item_stock[8]['stock_name'][0] in msg:
        return 'stock'
    if item_stock[9]['stock_name'][0] in msg:
        return 'stock'
    if 'job' in msg:                       
        return 'stock'
    if 'have' in msg:                        
        return 'stock'
    if 'yes' in msg:                          
        return 'stock'
    return 'no'





#利用状态机，作为机器人问询股票时候的应答
def stock_function(message):
    #状态机的各个状态
    #初始状态
    INIT = 0

    #选择选择股票
    CHOOSE_STOCK = 1

    #确认哪只股票
    COMFIRM = 2

    #显示数据
    SHOW = 3

    policy = {
        (INIT, "stock"): (CHOOSE_STOCK, "I have the information of " +  
                                                            item_stock[0]['stock_name'][0] + " 、 " +
                                                            item_stock[1]['stock_name'][0] + " 、 " +
                                                            item_stock[2]['stock_name'][0] + " 、 " +
                                                            item_stock[3]['stock_name'][0] + " 、 " +
                                                            item_stock[4]['stock_name'][0] + " 、 " +
                                                            item_stock[5]['stock_name'][0] + " 、 " +
                                                            item_stock[6]['stock_name'][0] + " 、 " +
                                                            item_stock[7]['stock_name'][0] + " 、 " +
                                                            item_stock[8]['stock_name'][0] + " 、 " +
                                                            item_stock[9]['stock_name'][0] + " , " +
                                                            "which one would you like to check ??? "),    
                                                           #"you could also browse website https://money.cnn.com/data/us_markets/ for deatils"),  #提到market时，视为询问股票行情
        (INIT, "ask_explanation_1"): (INIT, "I'm a bot to help you check your stock information."),
        (INIT, "specify_stock"): (COMFIRM, "Here we go !"),
        (INIT, "agree"): (SHOW, "I will show you the information!"),
        (CHOOSE_STOCK, "specify_stock"): (COMFIRM, "Do you like to see its price and change?"),
        (CHOOSE_STOCK, "ask_explanation_2"): (CHOOSE_STOCK,  "I have the information of " +  
                                                            item_stock[0]['stock_name'][0] + " 、 " +
                                                            item_stock[1]['stock_name'][0] + " 、 " +
                                                            item_stock[2]['stock_name'][0] + " 、 " +
                                                            item_stock[3]['stock_name'][0] + " 、 " +
                                                            item_stock[4]['stock_name'][0] + " 、 " +
                                                            item_stock[5]['stock_name'][0] + " 、 " +
                                                            item_stock[6]['stock_name'][0] + " 、 " +
                                                            item_stock[7]['stock_name'][0] + " 、 " +
                                                            item_stock[8]['stock_name'][0] + " 、 " +
                                                            item_stock[9]['stock_name'][0] + " , " +
                                                            "you could also browse website https://money.cnn.com/data/us_markets/ for deatils"),
        (CHOOSE_STOCK, "specify_stock"): (SHOW, "Do you like to see its price and change?"),
        (COMFIRM, "agree"): (SHOW, "The information is here !"),
        (COMFIRM, "none"): (COMFIRM, "choose again, pls"),
    }      

    state = INIT    
    state =  send_message(policy, state, message)
    print(state)
    #friend.send(u'response 1')
    #在用户输入股票名之后，就是COMFIRM状态，利用spacy提取股票名称
    print(state)
    #friend.send(u'response 2')
    if state == 2:
        #friend.send(u'response 3')
        stock_seeking = extract_entities(message)['ORG']
        print(stock_seeking)
    if state == 2:
        #在确认要查询哪只股票之后，给出信息 
        #friend.send(u'response 4')
        i = 0
        #friend.send(u'response 5')
        while True:
            #friend.send(u'response 6')
            stock_name = item_stock[i]['stock_name'][0]
            #friend.send(u'response 7')
            if stock_name == stock_seeking:
                #friend.send(u'response 8')
                friend.send(item_stock[i]['stock_name'][0] + 
                      ' is at a price of ' + 
                      item_stock[i]['stock_price'][0] + 
                      '  with a change of ' + 
                      item_stock[i]['stock_change'][0] + 
                      ' ,or to say, a percentage change of ' +
                      item_stock[i]['stock_percentage'][0])
                #friend.send(u'response 9')
                break
            elif i == len(item_stock):
                #friend.send(u'response 10')
                break
            #friend.send(u'response 11')
            i += 1      


keywords = {
            'greet': ['hello', 'hi', 'hey'], 
            'thankyou': ['thank', 'thx', 'thanks'], 
            'goodbye': ['bye', 'farewell']
           }
patterns = {}
for intent, keys in keywords.items():
#构建正则表达式
    patterns[intent] = re.compile('|'.join(keys))
responses = {'greet': 'Hello you! :)', 
             'thankyou': 'you are very welcome', 
             'default': 'Received',
             'goodbye': 'goodbye, then'
            }


#聊天尬聊（hello，thx，bye）功能时的send message函数
def another_send_message(message):
    response = another_respond(message)
    friend.send(response)
    
    
#尬聊功能时的，意图匹配
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        if pattern.search(message):
            matched_intent = intent
    return matched_intent




#尬聊功能时的，respond函数
def another_respond(message):
    intent = match_intent(message)
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]



#主程序，微信机器人获得信息
@bot.register()
def receive_msg(msg):
    message = msg.text                #获取微信消息文本
    switch = another_interpret(message) #判断是尬聊还是正事
    if switch == 'no':
        another_send_message(message)     #打招呼函数
    else:
        stock_function(message)           #传递给股票查询函数

    
    
    

    
    
    


# In[ ]:


# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()


# In[ ]:



 
friend = bot.friends().search(u'奶牛')[0]              #这里把‘奶牛’改成自己微信里好友的名字
 
friend.send(u"测试开始！!")
 
#查到好好友列表的某个好友并向他发送消息
 

