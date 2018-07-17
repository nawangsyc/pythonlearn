import time
import locale
locale.setlocale(locale.LC_CTYPE, 'chinese')
t = time.localtime()
ft = time.strftime('%Y年%m月%d日 %H:%M',t)
print(ft)