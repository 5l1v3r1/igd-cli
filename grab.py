#sertakan sumber kalo rikod njir :')
#facebook: ardho ainullah
#-*- coding: utf 8 -*-

import requests
import os,sys,time
import json

def banner(user):
    print '''   
                     __ 
                    [__]=== @~~~~
                  (______)Kalsel Exploit

[*] instagram downloader by muh4k3mos'''
    time.sleep(1)
    if user == None:
       pass
    else:
         print '[*] grabbing content from username account %s '%(user)
    time.sleep(1)

class looking:

      def __init__(self):
         self.point = "https://igdown.net/instagram-service.php"
         self.url = url
         self.files = filename

      def senja(self):
          self.head = {
                          'origin': 'https://igdown.net',
                          'x-requested-with': 'XMLHttpRequest',
                          'pragma': 'no-cache',
                          'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
                          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                          'accept': 'application/json, text/javascript, */*; q=0.01',
                          'cache-control': 'no-cache',
                          'authority': 'igdown.net',
                          'referer': 'https://igdown.net/',
                          }

          self.data = {"url":self.url}
          self.reqs = json.loads(requests.post(self.point,data=self.data,headers=self.head).text)
          banner(self.reqs['username'])

          if self.reqs['status'] == 'fail':
             sys.exit('[*] The url address entered is incorrect, maybe')

          try:
              self.content = self.reqs['image'] 
              print '[-] type of content taken : image'
          except KeyError:
                 self.content = self.reqs['videourl']
                 print '[-] type of content taken : video'

          self.save = requests.get(self.content).content
          with open(filename,'wb') as self.create:
               self.create.write(self.save)
               self.create.close()
          print '[*] downloaded, filename : %s\n'%(filename)




if __name__=='__main__':
  if len(sys.argv) < 3:
     sys.exit('''                           
                     __
                    [__]=== @~~~~
                  (______)Kalsel Exploit

instagram content downloader by @muh4k3mos 

usage: python2 grab.py {url} {filename}.extension
''')

  url = sys.argv[1]
  filename = sys.argv[2]
  start = looking()
  start.senja()




