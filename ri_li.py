import calendar

def get_days_in_month(year, month):
    first_day, days = calendar.monthrange(year,month)
    return days

def get_weekday(year, month, day):
    weekday = calendar.weekday(year, month, day)
    return weekday + 1

#从键盘输入获取年月并转换为int类型
# year = int(input("请输入年份："))
# month = int(input("请输入月份："))
year, month = 2025, 7
#获取年月对应的天数
days = get_days_in_month(year, month)

print("一 二 三 四 五 六 日")
print("-" * 20)
for i in range(1,days + 1):
    #获取年月日对应的星期数字1-7
    weekday = get_weekday(year, month, i)
    if i == 1:
        #每月第一天打印相应的空格
        print(" " * (3 * weekday - 3), end = "")
    print(f"{i:2d}", end = " ")
    #在周日之后打印回车
    if weekday == 7 and i != days:
        print("")