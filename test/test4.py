import csv
import json
import requests

title_1 = ["进口商品", "食品饮料", "粮油副食", "美容洗护", "家居家电","家庭清洁", "母婴用品"]
headers = {
    "cookie": "cna=5kffEqqIyS0CATz3G4EbJmmu; x=__ll%3D-1%26_ato%3D0; enc=U19dXW1RWwJGX5fx%2FUGPKVKY4HK2wkennV0%2B82F25XJSRdbOYEdw7V4V%2F4i6bYLymIrdyQOtuwPRimOyweWtJA%3D%3D; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; Hm_lvt_9d483e9e48ba1faa0dfceaf6333de846=1519798501; UM_distinctid=161df2f314442b-0a17747307fb63-5d4e211f-100200-161df2f31453b0; CNZZDATA1262561595=735344301-1519862474-https%253A%252F%252Fwww.so.com%252F%7C1519862474; cq=ccp%3D1; hng=CN%7Czh-CN%7CCNY%7C156; t=9b35ae456d1875923fa20b8aca3cf7b4; _tb_token_=7b33333951161; cookie2=10390a989ce41588325fcb5ec430a727; _m_h5_tk=b0b863213b8e7c342482f93375646f42_1520305928812; _m_h5_tk_enc=d31d3685818cc6c1488668887384952d; sm4=110100; isg=BJqaON7ylAvCMBhTS2Czdxa860C2y2bFcgiBtqQcIy3vFzlRjF5AtbMN4-OLx5Y9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}


def get_tmall_url():
    with open(r"C:\Users\chen\Desktop\天猫超市商品列表链接.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            yield line


def parse_tmall_product_list():
    title_list = []
    tem = 0
    for url in get_tmall_url():
        response = requests.get(url.strip("\n"), headers=headers)
        content_json = json.loads(response.text)
        product_cats = content_json["data"]["cats"]
        for product_item in product_cats:
            title_2 = product_item["title"]
            for item in product_item["cats"]:
                title_3 = item["text"]
                title_list.append([title_1[tem], title_2, title_3])
        tem += 1
    return title_list


def write_to_csv():
    category_list = parse_tmall_product_list()
    with open(r"C:\Users\chen\Desktop\天猫商品列表.csv", "w+", newline="", encoding='gbk') as file:
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
    # print(parse_tmall_product_list())

if __name__ == '__main__':
    main()
