import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

index = []
data = []
임시 = []

# 크롤링할 웹 페이지 URL 설정
url1 = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio10190361.html'  # 가천대 url

# 웹 페이지에 GET 요청 보내고 응답 받기
response = requests.get(url1)
#가천대
# 응답이 성공적인지 확인
print("가천대")
if response.status_code == 200:
    # BeautifulSoup을 사용하여 HTML 파싱
    
    soup = BeautifulSoup(response.text, 'html.parser')

    target_div = soup.find('div', id='SelType436')
    table = target_div.find('table', class_ = 'tableRatio3')
    target_major = "인공지능전공"  # 찾고자 하는 전공명
    rows = soup.find_all('tr')  # 모든 <tr> 요소를 찾습니다.
    
    if target_div:
        # "인공지능전공"을 포함한 모든 <tr> 요소를 찾습니다.
        tbody = target_div.find('tbody')
        
        tr_elements = target_div.find_all('tr')
        name_list = ['소프트웨어전공','인공지능전공']  
        for n in name_list:
            print(n)
        print("총계")
        for tr_element in tr_elements:
            # 각 <tr> 요소 안에서 원하는 정보를 추출하거나 출력합니다.
            # 이 부분에서 필요한 정보를 추출하거나 출력할 수 있습니다.
            # name = tr_elements.find_all('td', class_ = 'unit')

            
            td_elements = tr_element.find_all('td', class_='rate4') 
                        
            for n in td_elements:
                임시.append(n.text.strip())
                print(n.text.strip())
        
        index.append('가천대 SW')
        data.append(임시[0])
        index.append('가천대 AI')
        data.append(임시[1])

    else:
        print("id가 'SelType436'인 <div> 요소를 찾을 수 없습니다.")
else:
    print("웹 페이지에 접근할 수 없습니다. 상태 코드:", response.status_code)
        
url2 = 'https://ratio.uwayapply.com/Sl5KMCYlVzpKXiUmOiZKemZUZg=='  # 유니스트 url
response = requests.get(url2, verify=False)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    Unist_Ratio = soup.find('td', class_='txtFieldValue2', id='yogang_003_010')
    Unist_Ratio = Unist_Ratio.find('b')
    
    유니스트_경쟁률 = Unist_Ratio.text.strip()
    index.append('UNIST')
    data.append(유니스트_경쟁률)
    
else:
    print("웹 페이지에 접근할 수 없습니다. 상태 코드:", response.status_code)

#GIST
url3 = 'https://ratio.uwayapply.com/Sl5KMCYlclZKXiUmOiZKemZUZg=='  # DGIST url
response = requests.get(url3, verify=False)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    DGIST_Ratio = soup.find('tr', class_='trFieldValue', id='Tr_00E_0')
    DGIST_Ratio = DGIST_Ratio.find('b')
    디지스트_경쟁률 = DGIST_Ratio.text.strip()
    print(f"DGIST 특기자 전형 경쟁률 : {디지스트_경쟁률}")
    index.append("DGIST")
    data.append(디지스트_경쟁률)

else:
    print("웹 페이지에 접근할 수 없습니다. 상태 코드:", response.status_code)
    
url5 = 'https://ratio.uwayapply.com/Sl5KMCYlckpeJSY6Jkp6ZlRm'
response = requests.get(url5, verify=False)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    GIST_Ratio = soup.find('tr', class_='trFieldValue', id='Tr_00EUA02_50_0')
    List = GIST_Ratio.find_all('td',rowspan=1, class_='txtFieldValue')
    Ratio = List[3]
    지스트_특기자_경쟁률 = Ratio.text.strip()
    index.append("GIST")
    data.append(지스트_특기자_경쟁률)
    
else:
    print("웹 페이지에 접근할 수 없습니다. 상태 코드:", response.status_code)

#한밭대
url5 = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio30040391.html'
response = requests.get(url5)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    base = soup.find('div', id='SelType423')
    target_major = base.find_all('td',class_='unit')
    for n in target_major:
        if n.text.strip() == '인공지능소프트웨어학과':
            index_content = base.find('strong')
            data_content = base.find('td',class_='rate2',rowspan='1').text.strip()
            index.append(index_content)
            data.append(data_content)
            
        else:   
            pass

    
else:
    print("웹 페이지에 접근할 수 없습니다. 상태 코드:", response.status_code)

#한밭대
url5 = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio30040391.html'
response = requests.get(url5, verify=False)




column = ['경쟁률']
df = pd.DataFrame(data=data,index=index,columns=column)
print(df)
st.dataframe(df)