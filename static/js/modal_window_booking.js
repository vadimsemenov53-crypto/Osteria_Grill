//Когда HTML-документ полностью загрузится — выполни эту функцию
document.addEventListener("DOMContentLoaded", function () {

//addEventListener - отслеживание события
//function () { - создание функции


    // ищет элементы HTML по CSS-селектору (class="restaurant-table") - наши столы
    const tables = document.querySelectorAll(".restaurant-table");

    // ищем modal по id  (class="modal fade" id="bookingModal"..)
    const modalElement = document.getElementById("bookingModal");

    // ищем элемент по id ( <h5 id="bookingTableNumber"> Стол </h5> )
    const bookingTableNumber = document.getElementById("bookingTableNumber");

    // ищем элемент по id ( <p id="bookingTableCapacity" class="text-body-secondary"> </p> )
    const bookingTableCapacity = document.getElementById("bookingTableCapacity");

    // ищем элемент по id ( <strong id="bookingTableCategory"></strong> )
    const bookingTableCategory = document.getElementById("bookingTableCategory");

    // ищем скрытый элемент по id ( <input type="hidden" name="table" id="bookingTableId"> )
    const bookingTableId = document.getElementById("bookingTableId");

    // присваиваем значение
    const selectedTableId = bookingTableId.value;

    // ищем элемент по id ( <input type="date" id="bookingDate" name="booking_date"....> )
    const bookingDate = document.getElementById("bookingDate")

    // ищем данные о времени бронирования из формы
    const bookingTime = document.getElementById("bookingTime");

    if (modalElement) { //проверка истинности существования окна

        //создание управляемого modal-окна
        const modal = new bootstrap.Modal(modalElement);

        // Проверка истинности ( data-form-errors="{% if form.errors %}true{% else %}false{% endif %}" )
        const hasFormErrors = modalElement.dataset.formErrors === "true";

        if (hasFormErrors) {
            // ищет элемент html по css-селектору
            const selectedTable = document.querySelector(
                `[data-table-id="${selectedTableId}"]`
            );

            if (selectedTable) {
                // заполнение данных
                const tableNumber = selectedTable.dataset.tableNumber;
                const tableCapacity = selectedTable.dataset.tableCapacity;
                const tableCategory = selectedTable.dataset.tableCategory;

                // передача данных
                bookingTableNumber.textContent = `Стол №${tableNumber}`;
                bookingTableCapacity.textContent = `Вместимость: ${tableCapacity} мест`;
                bookingTableCategory.textContent = "";

                if (tableCategory == "VIP") { // если статус ... то заполнить ..
                    bookingTableCategory.textContent = "Премиум";
                }
            }
            modal.show();
        }

        // Пользователь выбирает дату
        function loadBookingTimes() {
            // записываем полученные переменные
            const tableId = bookingTableId.value;
            const date = bookingDate.value;

            // Если стол или дата отсутствуют — return
            if (!tableId || !date) {
                return;
            }

            console.log("tableId:", tableId);
            console.log("date:", date);

            // Запрос к заранее подготовленной функции отслеживания бронирования на выбранную дату
            fetch(
                `/restaurant/table-bookings/?table_id=${tableId}&date=${date}`
            )
                .then(response => response.json()) // из JSON в JavaScript-объект
                .then(data => {
                    console.log("Ответ сервера:", data);

                    //data = {bookings: [{start: "22:00",end: "00:00"}]}
                    updateBookingTimes(data.bookings); // Передаем: bookings: [{start: "22:00",end: "00:00"}]
                });
        }

        bookingDate.addEventListener("change", function () { loadBookingTimes() });

        tables.forEach(function (table) {
        // forEach - пройдись по каждому элементу
        // table - текущий стол

            // отслеживание нажатия по столу (<button class="restaurant-table> №{{ table.number }} </button>)
            table.addEventListener("click", function () {
                // если нажал покажи modal window (модальное окно)

                // получаем данные с стола по которому нажали
                const tableId = table.dataset.tableId;
                const tableNumber = table.dataset.tableNumber;
                const tableCapacity = table.dataset.tableCapacity;
                const tableCategory = table.dataset.tableCategory;

                // записываем в найденные элементы
                bookingTableId.value = tableId;
                bookingTableNumber.textContent = `Стол №${tableNumber}`;
                bookingTableCapacity.textContent = `Вместимость: ${tableCapacity} мест`;

                // очищаем перед проверкой (исключение отображение статуса на обычных столах)
                bookingTableCategory.textContent = "";

                if (tableCategory == "VIP") {
                            bookingTableCategory.textContent = "Премиум";
                    }

                modal.show();
            });

        });

        loadBookingTimes();
    }
});


// Функция обновления времени бронирования - (bookings - параметр для передачи, передаем список словарей)
function updateBookingTimes(bookings) {
    // [<option>12:00</option>, <option>14:00</option>,.....]
    const options = bookingTime.options;

    // Возьми каждую <option> из нашего списка по очереди
    for (let option of options) {

        // Сброс данных с прошлой даты
        // заведомо отключаем все option
        option.disabled = false;
        // возвращаем первоначальный текст
        option.textContent = option.value;
    }

    // Пройдись по каждому существующему бронированию
    bookings.forEach(function (booking) {
        // Возьми каждую <option> из нашего списка по очереди
        for (let option of options) {
            // "22:00" === "22:00" (True)
            if (option.value === booking.start) {
                // Отключаем время
                option.disabled = true;
                // добавляем надпись о занятом времени
                option.textContent =
                    `${option.value} — занято`;
            }
        }
    });
}