# reza-project



download python app and install 

برنامه پایتون رو دانلود کن بعد نصب کن 

اینارو تو ترمینال یا سی ام دی میزنیم یا ترمینال برنامه های وی اس کد یا پایچرم میزنیم || vscode , pycharm ,... میزنیم 

بعد پکیج پیپ رو نصب کن 

sudo easy_install pip

بعد ویژوال را نصب میکنیم

pip install virtualenv

بعد ویژوال درست میکنیم 

virtualenv env

یا در ویندوز

python -m venv env

برای فعال کردن ویژوال این را میزنیم

source env/bin/activate

یا در ویندوز

env\Scripts\activate

برای غیر فعال کردن ویژوال این را میزنیم

deactivate

بعد پکیج جنگو را نصب میکنیم  

Pip install Django

یا 

pip install django==1.5.12

یا در ویندوز

python -m pip install --upgrade pip

بعد یه فایل در پوشه ام ام ای درست کن به نام requirements.txt 

داخل این فایل بنویس 

Django~=2.2.4

بعد این کد را بزن

pip install -r requirements.txt

یا در ویندوز 

python -m pip install -r requirements.txt

نصب پکیج پیلو || pillow

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

یا 

pip install Pillow

بعد دوباره این کد را بزن 

python -m pip install -r requirements.txt

بعد برنامه رو اجرا میگیریم با کد زیر

python manage.py runserver


