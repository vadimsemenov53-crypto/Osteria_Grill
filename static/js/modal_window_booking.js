//Когда HTML-документ полностью загрузится — выполни эту функцию
document.addEventListener("DOMContentLoaded", function () {

//addEventListener - отслеживание события
//function () { - создание функции


    // ищет элементы HTML по CSS-селектору (class="restaurant-table") - наши столы
    const tables = document.querySelectorAll(".restaurant-table");

    // ищем modal по id  (class="modal fade" id="bookingModal"..)
    const modalElement = document.getElementById("bookingModal");

    if (modalElement) { //проверка истинности существования окна

        //создание управляемого modal-окна
        const modal = new bootstrap.Modal(modalElement);

        tables.forEach(function (table) {
        // forEach - пройдись по каждому элементу
        // table - текущий стол

            // отслеживание нажатия по столу (<button class="restaurant-table> №{{ table.number }} </button>)
            table.addEventListener("click", function () {
                // если нажал покажи modal window (модальное окно)
                modal.show();
            });

        });
    }
});