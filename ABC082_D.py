from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="082"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc087_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''FTF
1 -11
'''
y = '''
'''
additional_case = [x]
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  s=input()
  x,y=map(int,input().split())
  ud=[]
  rl=[]
  ini=0
  i=0
  now=0
  while i<len(s) and s[i]=='F':
    ini+=1
    i+=1
  while i<len(s):
    tmp=1
    while i<len(s)-1 and s[i]==s[i+1]:
      tmp+=1
      i+=1
    if s[i]=='F':
      if now==0:
        rl.append(tmp)
      else:
        ud.append(tmp)
    else:
      if tmp%2==1:
        now^=1
    i+=1
  ans='Yes'
  if (sum(rl)-abs(x-ini))%2==1 or (sum(ud)-abs(y))%2==1 or sum(rl)<abs(x-ini) or sum(ud)<abs(y):
    ans='No'
  a,b=[0]*8001,[0]*8001
  a[0]=1
  b[0]=1
  c,d=(sum(rl)-abs(x-ini))//2,(sum(ud)-abs(y))//2
  for i in range(len(rl)):
    tmp=a.copy()
    for j in range(8001):
      if a[j]==1 and j+rl[i]<8001: tmp[j+rl[i]]=1
    a=tmp
  if a[c]==0: ans='No'
  for i in range(len(ud)):
    tmp=b.copy()
    for j in range(8001):
      if b[j]==1 and j+ud[i]<8001: tmp[j+ud[i]]=1
    b=tmp
  if b[d]==0: ans='No'
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])