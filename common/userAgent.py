from fake_useragent import UserAgent

def GetUA():
    ua = UserAgent(cache=False).random
    #print(ua)
    return ua
    