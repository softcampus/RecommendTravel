# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def get_attractions(keywords):
    """이 get_attractions 함수는 Tripadvisor에서 키워드로 검색한 내용의 결과를 얻습니다.
    입력
    keywords: 검색 키워드
    리턴: 검색 결과 dict의 list
    """
    att_list = []
    url = "https://www.tripadvisor.co.kr/Search-q" + quote(keywords) + "%26actionType=updatePage%26ssrc=A%26dist=%26o=0%26ajax=search"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    for attraction in soup.find_all('div', {"class": "result"}):
        att_type = attraction.find('div', {"class": "type"})
        title = attraction.find('div', {"class": "title"})
        reviews = attraction.find('div', {"class": "reviews"})
        address = attraction.find('div', {"class": "address"})
        if att_type:
            att_list.append(
                {"type":att_type.text, "title":title.text, 
                 "reviews":reviews.text, "address":address.text}
            )
    return att_list

if __name__ == "__main__":
    #print( get_attractions("서울, 대한민국, 아시아") )
    print( get_attractions("홍콩, 중국, 아시아") )
    """
    [{'address': '100 Chatham Rd S, Tsim Sha Tsui East, Kowloon, 홍콩, 중국',
      'reviews': ' 2,886건의 리뷰 ',
      'title': '홍콩 역사 박물관',
      'type': '역사박물관'},
            {'address': 'Sai Kung District, New Territories East, 홍콩, 중국',
      'reviews': ' 1,017건의 리뷰 ',
      'title': 'Sai Kung',
          'type': '인근 지역'},
     {'address': 'Lamma Island, Islands Distict, 홍콩, 중국',
      'reviews': ' 1,427건의 리뷰 ',
      'title': '람마 섬',
      'type': '하이킹 트레일'},
     {'address': 'Chi Lin Rd, Diamond Hill, 홍콩, 중국',
      'reviews': ' 2,675건의 리뷰 ',
      'title': '\xa0치린 수도원',
      'type': '가든'},
     {'address': '1 Austin Road West, Kowloon,, 홍콩, 중국',
      'reviews': ' 1,348건의 리뷰 ',
      'title': '스카이 100',
      'type': '전망대 & 타워'},
     {'address': 'No.180 Wong Chuk Hang Road, 홍콩, 중국',
      'reviews': ' 8,345건의 리뷰 ',
          'title': '오션 파크',
      'type': '아쿠아리움'},
     {'address': 'All Over The City, 홍콩, 중국',
      'reviews': ' 1,497건의 리뷰 ',
      'title': '빅 버스',
      'type': '무제한 승하차 투어'},
     {'address': 'Hong Kong Island, along Victoria Harbor, 홍콩, 중국',
      'reviews': ' 11,101건의 리뷰 ',
      'title': '홍콩 스카이라인',
      'type': '흥미거리 & 랜드마크'},
     {'address': 'Chatham Rd. South , 홍콩, 중국',
      'reviews': ' 1,083건의 리뷰 ',
      'title': '침사추이',
      'type': '인근 지역'},
     {'address': '홍콩, 중국',
      'reviews': ' 1,546건의 리뷰 ',
      'title': '드래곤스 백',
      'type': '하이킹 트레일'},
     {'address': 'South District, Hong Kong Island, 홍콩, 중국',
      'reviews': ' 2,398건의 리뷰 ',
      'title': 'Stanley, Hong Kong',
      'type': '벼룩시장 & 재래시장'},
     {'address': 'No.60 Fung Tak Road, Diamond Hill, 홍콩, 중국',
      'reviews': ' 3,087건의 리뷰 ',
      'title': '난 리안 가든',
          'type': '공원'},
     {'address': '19 Cotton Tree Dr, Central, 홍콩, 중국',
      'reviews': ' 2,487건의 리뷰 ',
      'title': '홍콩 공원',
      'type': '공원'},
     {'address': '홍콩, 중국',
      'reviews': ' 4,484건의 리뷰 ',
      'title': '란타우 섬',
      'type': '섬'},
     {'address': 'Central and Western District, Hong Kong Island, 홍콩, 중국',
      'reviews': ' 5,197건의 리뷰 ',
      'title': '빅토리아 하버',
      'type': '마리나'},
     {'address': 'Lots 358-359,IN D D 185, Shatin, 홍콩, 중국',
      'reviews': ' 1,782건의 리뷰 ',
      'title': '만불사',
      'type': '종교적인 장소'},
     {'address': 'Kowloon Point, Tsim Sha Tsui, Kowloon, 홍콩, 중국',
      'reviews': ' 15,504건의 리뷰 ',
      'title': '스타 페리',
      'type': '페리'},
     {'address': 'Whitty Street Tram Depot, Connaught Road West, Western District, 홍콩, 중국',
      'reviews': ' 7,686건의 리뷰 ',
      'title': '이층 케이블 카',
      'type': '전차'},
     {'address': 'Kansu Street and Jordan Road, Mongkok, Kowloon, 홍콩, 중국',
      'reviews': ' 1,860건의 리뷰 ',
      'title': 'Temple Street Night Market',
      'type': '벼룩시장 & 재래시장'},
     {'address': 'Tung Choi Street, 홍콩, 중국',
      'reviews': ' 2,200건의 리뷰 ',
      'title': 'Ladies Market',
      'type': '벼룩시장 & 재래시장'},
     {'address': 'South of Hollywood Road, 홍콩, 중국',
      'reviews': ' 727건의 리뷰 ',
      'title': '소호',
      'type': '인근 지역'},
     {'address': 'Central, 홍콩, 중국',
      'reviews': ' 1,228건의 리뷰 ',
      'title': 'Lan Kwai Fong',
      'type': '흥미거리 & 랜드마크'},
     {'address': 'Tsim Sha Tsui, 홍콩, 중국',
      'reviews': ' 4,050건의 리뷰 ',
      'title': '침사추이 산책로',
      'type': '흥미거리 & 랜드마크'},
     {'address': 'Lantau Island, 홍콩, 중국',
      'reviews': ' 10,750건의 리뷰 ',
      'title': '빅 부다',
      'type': '흥미거리 & 랜드마크'},
     {'address': '1 Lugard Rd, 홍콩, 중국',
      'reviews': ' 25,799건의 리뷰 ',
      'title': '빅토리아 피크',
      'type': '전망대 & 타워'},
     {'address': 'Lantau Island, 홍콩, 중국',
      'reviews': ' 12,216건의 리뷰 ',
      'title': '홍콩 디즈니랜드',
      'type': '놀이공원 & 테마파크'},
     {'address': 'Kowloon, 홍콩, 중국',
      'reviews': ' 2,433건의 리뷰 ',
      'title': '몽콕',
      'type': '인근 지역'},
     {'address': '11 Tat Tung Road, Tung Chung, Lantau Island, 홍콩, 중국',
      'reviews': ' 4,627건의 리뷰 ',
      'title': '옹핑 360',
      'type': '전망대'},
     {'address': 'No.1 Lugard Road, 홍콩, 중국',
      'reviews': ' 6,413건의 리뷰 ',
      'title': '피크 트램',
      'type': '전차'},
     {'address': 'No.4 Sun Wui Road, Causeway Bay, 홍콩, 중국',
      'reviews': ' 274건의 리뷰 ',
      'title': 'Walk in Hong Kong-Day Tour',
      'type': '개인 여행'}]
    """