document.addEventListener("DOMContentLoaded", function (){ //Когда HTML-документ полностью загрузится — выполни эту функцию
    const modalElement = document.getElementById( //Найди в текущем HTML элемент с таким id
    "registrationSuccessModal"
    );
    if (modalElement){   //  bootstrap.Modal — это объект Bootstrap, который умеет управлять модальными окнами.
    const modal = new bootstrap.Modal(modalElement); //этот HTML-элемент является твоим Modal. Создай для него объект управления
    modal.show(); //открой этот Modal
    } });