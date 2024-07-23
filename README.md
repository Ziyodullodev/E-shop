# `E-shop` simple online shop

## Loyihani Localda ishga tushurish

Loyihani o'z kompyuteringizga yuklab olish uchun quyidagi qadamlarni bajaring:

1. Git repositoryni klon qiling:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   
2. `.env` file yarating. misol tariqasida `.env.example` filedan ko'ring yoki:
    ```bash 
    cp .env.example .env

3. Komputeringizga `python`, `docker` o'rnatib oling va:

    ```bash
    python3 -m venv venv 
    # agar sizda virtualenv bolsa
    virtualenv venv

4. `venv` fileingizni ishga tushuring:
    ```bash
    source venv/bin/activate
5. kerakli kutubxonalarni o'z komputeringizga o'rnating. Bu sizga localda ishlayotganingizda yordam beradi:
    ```bash
    pip install -r requirements.txt
6. Dockerni ishga tushuring. Ish tushurishda bir narsaga etibor bering `.env` file ichida `PIPELINE` o'zgaruvchisi bor shuni localda ishlayotganingizda `dev` qilib olishni unutmang!!!:
    ```bash
    docker compose up --build
    # yoki
    docker-compose up --build

dasturni online komputerga yani serverga deploy qilish uchun quyidagi qadamlar mavjud.

1. Loyihani serverga clone qilib oling (buni teparoqda ko'rsatib ketdim).
2. Serverni yangilab oling:
    ```bash
    sudo apt update & sudo apt upgrade
3. Serverga kerakli texnologyalarni o'rnatish:
    ```bash
    # dockerni o'rnatish
    sudo apt install docker.io

    # Python 3 o'rnatish
    sudo apt install python3 python3-pip

    # Nginx o'rnatish
    sudo apt install nginx

    # Gunicorn o'rnatish (Python uchun)
    sudo apt install gunicorn
4. kegin tepada ko'rsatganimdek: loyiha papka ichiga kirib olasiz, virtual muxit yaratasiz (buni ham tepada misol ko'rsatib qoydim), `.env` file yaratasiz `.env.example` misolida ichidagi ma'lumotlarni o'zingizga moslab olasiz, so'ng loyihani serverda ishga tushurasiz. 
5. serverda loyihani ishga tushurish
    ```bash
    docker compose -f docker-compose-production.yml up --build
    # yoki
    docker-compose -f docker-compose-production.yml up --build


### PS: --------
- Qanday qilib superuser yarata olaman?
    ```bash 
    docker compose run web python manage.py createsuperuser
- docker compose run web dan kegin python commandalaridan foydalana olasiz.
- Qanday qilib docker container ichiga kira olaman?
    ```bash
    docker ps
    # sizga kontainerlar ro'yixati ko'rinadi ular ichidan siz web ni tanlab uni container id sini kiritasiz, yani:
    docker exec -it containerID bash
    

## Kelajakda qo'shilishi mumkin bo'lgan yangilanishlar

- CI/CD pipline with github action
- auto testing project


#### Loyihada xato kamchiliklar topsangiz xabar berish yoki pull request ochishingiz mumkin! xammaga raxmat.
