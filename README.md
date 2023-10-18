# weather_widget
# ویجت آب وهوا

[![Python](https://img.shields.io/badge/Python-3.11.4-yellow.svg)](http://www.python.org/download/)
[![PyQt6](https://img.shields.io/badge/PYQt6-6.4.2-green.svg)](https://pypi.org/project/PyQt6/) 
[![beautifulsoup4](https://img.shields.io/badge/beautifulsoup4-4.7.1-white.svg)](https://pypi.org/project/beautifulsoup4/) 
[![pyautogui](https://img.shields.io/badge/pyautogui-0.9.54-blue.svg)](https://pypi.org/project/PyAutoGUI/)  
[![requests](https://img.shields.io/badge/requests-2.21.0-blue.svg)](https://pypi.org/project/requests/)  

### تصاویر
![frameless mode](resource/1.png)
![windows mode](resource/2.png)

### نصب پیش نیاز ها
```console
pip install pyautogui
pip install requests
pip install beautifulsoup4
pip install PyQt6
```

### اجرا به صورت ویندوز
برای اجرای برنامه به صورت ویندوز میتوانید از دستور ‍‍```python weather.py frameless``` استفاده کنید 
در این حالت پنچره بسته نمیشود و شما باید خودتان ان را ببندید

### اجرا به صورت ویجت
بعد از پین کردن میانبر برنامه یا فایل exe ان به تسکبار میتوانید روی ان کلیک کنید و ان را اجرا کنید
اگر برنامه بدون ارگومان ```frameless``` اجرا شود در محل کلیک باز شده و بعد از زمان تعیین شده در فایل تنظیمات بسته میشود
دستور اجرا به صورت ویجت به صورت مقابل است : ```python waether.py``` 


### تنظیمات 
در فایل ‍‍‍```config.json``` میتوانید شهر و استان خود را تغییر داده و همچنین مقدار ثانیه باز ماندن برنامه در حالت ویجت را تغییر دهید . دقت کنید نیازی به وارد کردن کامل شهر و استان نیست اگر دو شهر با اسم مشایه وجود دارد استان یا حتی کشور را هم وارد کنید

### نکته نهایی
برنامه بعد از اجرا شدن نیاز به چند ثانیه برای دریافت اطلاعات میباشد و بعد از آن ویجت نمایش داده میشود . (رفع خواهد شد)
