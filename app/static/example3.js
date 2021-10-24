
async function send_messageExample3()
{

    const url = location.protocol + '//' + document.domain + ':' + location.port + '/example3';
    const data = { msg: document.getElementById("MessageBox").value };

    try {
        const response = await fetch(url, {
            method: 'POST', // или 'PUT'
            body: JSON.stringify(data), // данные могут быть 'строкой' или {объектом}!
            headers: {
            'Content-Type': 'application/json'
            }
        });
        if (response.ok) {
            console.log(response)
        }    
    }
    
    catch (error) {
    console.error('Ошибка:', error);
    }

    
}