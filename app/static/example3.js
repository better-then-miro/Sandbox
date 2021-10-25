
async function send_messageExample3()
{
    //строим урл для запроса. итоговое значение будет 
    //  http://127.0.0.1:5000/example3
    const url = location.protocol + '//' + document.domain + ':' + location.port + '/example3';
    // вытаскиваем данные из текстового поля по id
    const data = { msg: document.getElementById("MessageBox").value };

    try {
        //строим и отправляем POST-запрос на запрос 
        const response = await fetch(url, {
            method: 'POST', // или 'PUT'
            body: JSON.stringify(data), // данные могут быть 'строкой' или {объектом}!
            headers: {
            'Content-Type': 'application/json'
            }
        });
        //пишем в консоль  браузера ответ от сервера
        if (response.ok) {
            console.log(response)
        }    
    }
    
    catch (error) {
    console.error('Ошибка:', error);
    }

    
}