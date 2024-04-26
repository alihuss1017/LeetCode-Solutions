n = 4
if n % 7 != 0:
    weeks = n // 7 + 1
else:
    weeks = n // 7
copy_n = n
start = 0
daily = 0
ans = 0
for week in range(weeks):
    start += 1
    daily = start

    if copy_n // 7 >= 1:
        days = 7
        copy_n -= 7

    else:
        days = copy_n % 7

    for day in range(days):
        ans += daily
        daily += 1
print(ans)