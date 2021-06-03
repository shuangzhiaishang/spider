import requests
from bs4 import BeautifulSoup
from encrypt import encrypt
import re
import pandas as pd

class NetWork:
    def __init__(self):
        self.username = ''
        self.password = ''

        self.urlLoginEAS = 'http://csujwc.its.csu.edu.cn/jsxsd/xk/LoginToXk'
        self.urlEASGrade = 'http://csujwc.its.csu.edu.cn/jsxsd/kscj/cjcx_list'
        self.urlCourseSchedule = 'http://csujwc.its.csu.edu.cn/jsxsd/xskb/xskb_list.do?Ves632DSdyV=NEW_XSD_WDKB'
        
        self.headers = { 
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
        }
        self.session = requests.Session()
    
    def loginEAS(self, username, password):
        self.username = username
        self.password = password
        passkey = encrypt(self.username, self.password)
        loginData = {
            "encoded": passkey
        }
        try:
            self.session = requests.Session()
            self.session.post(self.urlLoginEAS, data=loginData, headers=self.headers)
            response = self.session.get(self.urlEASGrade)
        except:
            return False
        title = BeautifulSoup(response.text, 'html.parser').title.string
        if title != '学生个人考试成绩':
            return False
        return True

    def getStudentInfoFromEAS(self):
        response = self.session.get(self.urlEASGrade)
        htmlText = BeautifulSoup(response.text, 'html.parser')
        info = htmlText.find('div', id="Top1_divLoginName")
        name = re.sub("[A-Za-z0-9\!\%\[\]\,\。()\n\t\xa0]", "", info.contents[4])
        return name.replace(' ', '')
        
    def getResultsFromEAS(self):
        response = self.session.get(self.urlEASGrade)
        htmlText = pd.read_html(response.text)[0]
        col = htmlText.columns.values
        col[0] = ''
        htmlText.columns = col
        for row in range(htmlText.shape[0]):
            if str(htmlText[''][row]) == 'nan':
                htmlText.drop([row], axis=0, inplace=True)
        htmlText.index = range(htmlText.shape[0])
        htmlText.drop([''], axis=1, inplace=True)
        htmlText.drop(['序号'], axis=1, inplace=True)
        return htmlText

    def getCourseScheduleFromEAS(self):
        response = self.session.get(self.urlCourseSchedule)
        htmlText = pd.read_html(response.text)[0]
        col = htmlText.columns.values
        col[0] = ''
        htmlText.columns = col  
        htmlText.drop([htmlText.shape[0]-1], axis=0, inplace=True)
        for col in htmlText.columns.values:
            for row in range(htmlText.shape[0]):
                if str(htmlText[col][row]) == 'nan':
                    htmlText[col][row] = ''
        return htmlText

            