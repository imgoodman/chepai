import requests
from time import sleep
import hashlib
import os

def get_reddit_worldnews(subreddit='worldnews',n_pages=5):
    USER_AGENT='python:huangjian.wang/worldnews (by /u/goodmanha)'
    token=login_reddit()

    stories=[]
    after=None

    for page_number in range(n_pages):    
        url='https://oauth.reddit.com/r/{0}?limit=100'.format(subreddit)
        headers={
            'Authorization':'bearer {0}'.format(token['access_token']),
            'User-Agent':USER_AGENT
        }
        if after:
            url+='&after={}'.format(after)
        response=requests.get(url,headers=headers)
        result=response.json()

        after=result['data']['after']
        sleep(5)

        stories.extend( [ (story['data']['title'],story['data']['url'],story['data']['score']) for story in result['data']['children'] ] )
    # print(stories)
    download_webpage(stories)
    return stories

def download_webpage(stories):
    number_errors=0
    idx=0

    data_folder=os.path.join('d:/python/ml-20m/reddit/','raw')
    for title,url,score in stories:
        print(' the {0}th download'.format(idx))
        idx+=1
        print('begin download {0}'.format(url))
        output_file_name = hashlib.md5(url.encode()).hexdigest()
        fullpath= os.path.join(data_folder,output_file_name+'.txt')
        if os.path.exists(fullpath):
            print('already downloaded')
            continue
        
        try:
            response = requests.get(url)
            data =response.text
            with open(fullpath,'w',encoding='utf-8') as outf:
                outf.write(data)
            print('successfully')
        except Exception as e:
            number_errors+=1
            print("fail")
            print(e)

def login_reddit():
    CLIENT_ID='bRe-pIIRemrjGw'
    CLIENT_SECRET='A_8dVhOyxcFH8yFYj8uVVvfqAdo'
    USER_AGENT='python:huangjian.wang/worldnews (by /u/goodmanha)'

    USERNAME='goodmanha'
    PASSWORD=''

    headers={ 'User-Agent' : USER_AGENT}

    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID,CLIENT_SECRET)    

    post_data={
        'grant_type':'password',
        'username':USERNAME,
        'password':PASSWORD
    }

    response = requests.post('https://www.reddit.com/api/v1/access_token',auth=client_auth,data=post_data,headers=headers)

    token=response.json()
    print(token)
    return token

if __name__=='__main__':
    get_reddit_worldnews()