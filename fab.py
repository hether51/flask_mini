from asyncio.windows_events import NULL
import re,requests,json

headers={
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        }

vedioApiUrl='https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='
vedioUrl='https://aweme.snssdk.com/aweme/v1/play/?video_id='


def expToUrl(text):
    try:
        if text!="" or text !=None:
            pattern="(ht|f)tp(s?)\:\/\/[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*)*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&%\$#_]*)?"
            c=re.compile(pattern=pattern)
            url=c.search(text).group()
            return url
    except Exception as err:
        print("正则取值异常，请输入正确地址："+str(err))

def __getVid(r_url):
    vedioId=None
    try:
        res=requests.get(r_url,headers=headers,allow_redirects=False)
        locationStr=res.headers.get('location')
        if res.headers.get('location'):
            print(locationStr)
            longUrl=locationStr
            pattern='(?<=/video/).*?(?=\/)'
            vedioId=re.compile(pattern).search(locationStr).group()
            print('获取vedioId成功---'+vedioId)
        else:
            print('没找到location:'+str(res.headers))
    except Exception as err:
        print('获取视频Id出错：'+str(err))
    return vedioId

def getVideoUrl(videoId):
    vid = None
    if videoId=='' or videoId==None:
        print('输入的连接为空！')
        return

    print(vedioApiUrl+videoId)
    try:
        res=requests.get(vedioApiUrl+videoId,headers=headers)
        vedioInfo=json.loads(res.text)
        if vedioInfo['status_code']==0:

            uri = vedioInfo['item_list'][0]['video']['play_addr']['uri']
            vid_list = vedioInfo['item_list'][0]['video']['play_addr']['url_list']
            print("the uri is ",vid_list[0])

            for info in vedioInfo['item_list']:
                vid=info['video']['vid']
                print('获取视频vid成功--------'+vid)
                vid_music=info['music']['play_url']['uri']
                #-----------获取视频封面
                if info['video']['origin_cover']['url_list']!=None:
                    for cover in info['video']['origin_cover']['url_list']:
                        vid_bgImage=cover
                        break
                elif info['video']['origin_cover']['url_list']!=None:
                    for cover in info['video']['cover']['url_list']:
                        vid_bgImage=cover
                        break
                else:
                    vid_bgImage=""
                break
        else:
            print("服务器返回异常！")
    except Exception as err:
        print('获取视频信息错误：'+str(err))
    return vid
        
        
        
        
        
        
        
        



if __name__ == '__main__':
    URL ="7.17 eBG:/ 复制打开抖音，看看【黑袍的作品】周六保证不休息，周日休息不保证，违法吗？# 内容过于... https://v.douyin.com/6GmdLd5/"
    real_url = expToUrl(URL)
    print(real_url)
    videoId =  __getVid(real_url)
    videoUrl = getVideoUrl(videoId)
    print('https://aweme.snssdk.com/aweme/v1/play/?video_id='+str(videoUrl))
    #requests.post()
        