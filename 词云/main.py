import requests 
import json
import jieba
from wordcloud import WordCloud
def get_ciyun(oid,path):
    cloud=[]
    def get_comment(oid):
        comment=[]
        a="no"
        p_number=0
        for i in range(1,1000000000000000000000000000000000000000000000000000):
            if a =="yes":
                i=n
                a="no"
            url = f"https://api.bilibili.com/x/v2/reply?&jsonp=jsonp&pn={i}&type=1&oid={oid}&sort=2"
            response = requests.get(url) 
            jsons = json.loads(response.text)
            for o in range(100000000000000):
                try:
                    comment.append(jsons["data"]["replies"][o]["content"]["message"])
                except:
                    break
            if json.loads(response.text) ==None or json.loads(response.text)=={"code": -412, "message": "请求被拦截", "ttl": 1, "data": None}:
                a="yes"
                n=i
                p_number+=1
                continue
            if json.loads(response.text) =={"code":-400,"message":f"strconv.ParseInt: parsing \"{i}\": value out of range","ttl":1} or json.loads(response.text)=={'code': 0, 'message': '0', 'ttl': 1, 'data': {'page': {'num': 25, 'size': 20, 'count': 0, 'acount': 1}, 'config': {'showtopic': 1, 'show_up_flag': True, 'read_only': False}, 'replies': None, 'upper': {'mid': 247987609, 'top': None, 'vote': None}, 'top': None, 'vote': 0, 'blacklist': 0, 'assist': 0, 'mode': 3, 'support_mode': [2, 3], 'control': {'input_disable': False, 'root_input_text': '发一条友善的评论', 'child_input_text': '', 'giveup_input_text': '不发没关系，请继续友善哦~', 'screenshot_icon_state': 3, 'upload_picture_icon_state': 3, 'answer_guide_text': '需要升级成为lv2会员后才可以评论，先去答题转正吧！', 'answer_guide_icon_url': 'http://i0.hdslb.com/bfs/emote/96940d16602cacbbac796245b7bb99fa9b5c970c.png', 'answer_guide_ios_url': 'https://www.bilibili.com/h5/newbie/entry?navhide=1&re_src=12', 'answer_guide_android_url': 'https://www.bilibili.com/h5/newbie/entry?navhide=1&re_src=6', 'bg_text': '', 'empty_page': None, 'show_type': 1, 'show_text': '', 'web_selection': False, 'disable_jump_emote': False}, 'folder': {'has_folded': False, 'is_folded': False, 'rule': ''}}}:
                break
            if p_number>=100:
                break
        return comment
    for i in get_comment(oid):
        words = jieba.lcut(i) 
        for i in words:
            cloud.append(i)

    newtxt = ''.join(cloud)
    wordcloud = WordCloud(font_path =  "msyh.ttc",width = 1600,height = 900,).generate(newtxt)
    wordcloud.to_file(path)
