'''
?????? ?? ????????????????: ??????????? ??????
?????? ?????? ???????? ?????????? ????????? n ? ??????????? ??????? W.
?????? ?? ????????? n ????? ?????? ????????? c ? ????? w ???????? (????? ?????).
???????? ???????????? ????????? ?????? ????????? (?? ??????? ???????? ????? ???????? ????? ?????, ????????? ? ????? ??? ???? ??????????????? ??????????),
???????????? ? ?????? ??????, ? ????????? ?? ????? ???? ?????? ????? ???????.
https://stepic.org/lesson/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-13238/step/10?unit=3424
'''
item_number, bag_volume  = (int(x) for x in input().split())

items = []

for x in range(item_number):
    item_value, item_volume = (int(x) for x in input().split())
    items.append((item_value, item_volume, item_value / item_volume))

print(items)
items= sorted(items,key=lambda x: x[2], reverse=True)
print(items)

bag_value = 0.0
for (total_value, total_volume, value_avg) in items:
    if bag_volume >= total_volume :
        bag_value += total_value
        bag_volume -= total_volume
    else :
        bag_value += bag_volume * value_avg
        break

print("%.3f" % bag_value)


