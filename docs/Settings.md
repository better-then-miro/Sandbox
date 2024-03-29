## Первоначальная настройка  

Привет. Как и обещал - пишу маленький гайд по веб разработке и тому как у нас все будет  устроено в проекте.  
Прежде чем мы начнем разбираться с непосредственно кодом мы должны настроить наше окружение, установить  
все пакеты и все необходимое для работы.

Начнем с виртуального окружения или виртуальной среды разработки. Почему она нужна? Потому что  
во время разработки придется срать в операционную систему: устанавливать странные версии пакетов,  
устанавливать глобальные переменные, использовать неочевидные версии питона и так далее.  

У нас из этих развлечений будет почти все, так что вам самим захочется изолировать проект от остальной  
операционки, чтобы после каждого раза не откатывать все, что вы там поменяли. На наше счастье у питона  
из под коробки есть собственная виртуальная среда. Устанавливаем её:  
`$ pip install virtualenv`   

Следующим шагом клоним реп в любую удобную папку. Надеюсь не надо подсказывать, как сделать то :)   
После этого заходим в папку и делаем следующую магию:  
`$ python3 -m venv venv`  

Кстати есть вероятность, что вместо **python3** нужно написать **python**, но это мелочи  
На это этапе питон задумается на какое то время, после чего в вашей директории появится папка venv  
Чтобы войти в виртуальную среду исполняем скрипт активации:   
`$ ./venv/Scripts/activate`  

После этого ваш терминальчик поменяется и перед знаком **$** появится приписка **(venv)**  
Поздравляю! Теперь вы в безопасной среде разработки (не докер, но пойдет). Кстати чтобы выйти из нее  
в той же папке есть скрипт `Deactivate`

Переходим к настройке пакетов. Нам понадобятся: flask, Flask-SocketIO. В действительности пакетов сильно  
больше, но pip из под коробки разрулит все зависимости и будет хорошо. После того, как пакеты встанут обновляем  
их до чуть более низкой версии, потому что девелоперы сокетИО лохи:  

`(venv) $ pip install --upgrade python-socketio==4.6.0`  

`(venv) $ pip install --upgrade python-engineio==3.13.2`  

`(venv) $ pip install --upgrade Flask-SocketIO==4.3.1`  

Осмысленности в этом нет, просто ребята несколько заруинили обратную совместимость с жабаскриптом и все тут  
Директория с проектом должна выглядеть у вас примерно так:  
```
Sandbox:  
    -app/  
        -static/  
            ...  
        -templates/  
            ...  
        ...  
    venv/  
        ...  
    docs/
        ...
    sandbox.py  
```
Теперь нам нужно сообщить фласку, что для него приложение. Делается это следующей командой:

`(venv) $ export FLASK_APP = sandbox.py`  

Кстати если кто то на шизоиндус, то вместо **export** нужно использовать **set**  

Теперь вы можете запустить приложение запросом  

`(venv) $ flask run`  

вывод должен быть примерно следующим

```
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Теперь заходим на http://127.0.0.1:5000/ и наслаждаемся нашим приложением