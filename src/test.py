'''
Created on 2017-11-13

@author: chen
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv


# import re
def get_all_weather_url():
    response = urlopen("http://www.tianqihoubao.com/lishi/beijing/month/201101.html")
    bs_obj = BeautifulSoup(response.read(), "lxml")
    months = bs_obj.find("div", {"class": "months"})
    #    print(months,type(months))
    month_all = months.find_all("a")
    for month in month_all:
        #        print(type(month),len(month_all))
        #        print(month.a["href"]+" "+month.a["title"])
        #        print(month.attrs)
        yield month.attrs


# url处理
def get_page_url_weather():
    for url in get_all_weather_url():
        half_url = url["href"]
        title = url["title"]
        weather_url = "http://www.tianqihoubao.com/" + str(half_url)
        yield weather_url, title


def get_weather_data():
    url_set = set([])
    for url, title in get_page_url_weather():
        if url not in url_set:
            url_set.add(url)
            weather_content = urlopen(url).read()
            weather_page_obj = BeautifulSoup(weather_content, "lxml")
            tbody_page = weather_page_obj.table
            #        print(tbody_page.find_all("tr"),title)
            tr_weather_page = tbody_page.find_all("tr")
            #        print(title)
            for tr_each in tr_weather_page:
                #            print(tr_each)
                td_weather = tr_each.find_all("td")
                data = td_weather[0].get_text(" ", strip=True).replace("\r\n", "").replace(" ", "")
                weather = td_weather[1].get_text(" ", strip=True).replace("\r\n", "").replace(" ", "")
                temperature = td_weather[2].get_text(" ", strip=True).replace("\r\n", "").replace(" ", "")
                wind = td_weather[3].get_text(" ", strip=True).replace("\r\n", "").replace(" ", "")
                #            if (str(data) != "日期" | str(weather) != "天气状况" | str(temperature) != "气温" | str(wind) != "风力风向"):
                #                print(data, ",", weather, ",", temperature, ",", wind)
                #                print(url_set)
                yield data, weather, temperature, wind

            else:
                continue


def main():
    #    book = xlsxwriter.Workbook(r"C:\Users\chen\Desktop\北京天气数据每日更新.xlsx")
    with open(r"C:\Users\chen\Desktop\北京天气数据每日更新.csv", "w+", newline="") as file:
        writer = csv.writer(file)
        tem = 1
        for data, weather, temperature, wind in get_weather_data():
            #            temp = book.add_worksheet()
            #            temp.write_row(data, weather, temperature, wind)
            #            print(data , ",", weather, ",", temperature, ",", wind)
            day_weather = [data, weather, temperature, wind]
            writer.writerow(day_weather)
            #            writer.writerows([str(data) + str(weather) + str(temperature) + str(wind)])
            print("第" + str(tem) + "次写入成功")
            tem += 1
        print("写入完毕")


if __name__ == '__main__':
    main()
