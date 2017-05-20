import requests
import sys
import webbrowser
from bs4 import BeautifulSoup
from datetime import datetime


def kqxs(numbers):
    r = requests.get("http://ketqua.net")
    soup = BeautifulSoup(r.text, 'html5lib')
    for table in soup.find_all("table"):
        if table["id"] == "result_tab_mb":
            table_tag = table
            break
    table_tag.thead.decompose()
    bingo = []
    for result in table_tag.strings:
        bingo.append(result)
    is_win = False
    if len(numbers) > 0:
        for number in numbers:
            for result in bingo:
                if number == result[-2:]:
                    print("Trúng lô với số {} với số {}"
                          .format(number, result))
                    is_win = True
                else:
                    pass
        if not is_win:
            print("Không trúng số nhé! Xem kết quả xs hôm nay")
            print_kqxs(table_tag)
    else:
        print_kqxs(table_tag)


def print_kqxs(table_tag):
    kqxs_today = datetime.today()
    soup_result = BeautifulSoup(str(table_tag), 'html5lib')
    meta_tag = soup_result.new_tag("meta")
    meta_tag.attrs["charset"] = "utf-8"
    tr_tag = soup_result.new_tag("tr")
    tr_tag.string = "Ngày {}, Tháng {}, Năm {}".format(kqxs_today.day,
                                                       kqxs_today.month,
                                                       kqxs_today.year)
    soup_result.head.append(meta_tag)
    soup_result.tbody.append(tr_tag)
    soup_result.table["class"] = ""
    file_name = ("homework" + str(kqxs_today.day) + str(kqxs_today.month) +
                 str(kqxs_today.year) + ".html")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(soup_result.prettify())
    webbrowser.open_new_tab(file_name)


def main():
    numbers = sys.argv[1:]
    kqxs(numbers)


if __name__ == '__main__':
    main()
