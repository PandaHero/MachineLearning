import csv

import requests
from bs4 import BeautifulSoup

category_list = []
url = "https://www.jd.com/allSort.aspx"
# 发送请求，获取响应
content = requests.get(url).text
# 解析网页
soup = BeautifulSoup(content, "lxml")
category_col = soup.find_all("div", {"class": "col"})
for col in category_col:
    category_item = col.find_all("div", {"class": "category-item m"})
    for item in category_item:
        item_title_1 = item.find("h2", {"class": "item-title"}).get_text()
        clearfixs = item.find_all("dl", {"class": "clearfix"})
        for clear_fix_1 in clearfixs:
            item_title_2 = clear_fix_1.find("dt").a.get_text()
            # print(item_title_2)
            clear_fix_a = clear_fix_1.find("dd").find_all("a")
            for clear_fix_2 in clear_fix_a:
                item_set = []
                item_title_3 = clear_fix_2.get_text()
                item_set.append(item_title_1.strip("\n"))
                item_set.append(item_title_2)
                item_set.append(item_title_3)
                category_list.append(item_set)


def write_to_csv():
    with open(r"C:\Users\chen\Desktop\京东商品列表.csv", "w+", newline="", encoding='gbk') as file:
        tem = 1
        writer = csv.writer(file)
        writer.writerow(["item_title1", "item_title2", "item_title3"])
        for item in category_list:
            writer.writerow(item)
            print("第" + str(tem) + "次写入成功")
            tem += 1
        print("写入完毕")


def main():
    write_to_csv()


if __name__ == '__main__':
    main()
