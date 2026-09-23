document.addEventListener("DOMContentLoaded", function () {
    const bookingId = document.getElementById("bookingId");

    const bookingTable = document.getElementById("id_table");

    const bookingDate = document.getElementById("bookingDate");

    const bookingTime = document.getElementById("bookingTime");

    console.log("Booking ID:", bookingId.value);
    console.log("Table:", bookingTable.value);
    console.log("Date:", bookingDate.value);
    console.log("Time:", bookingTime.value);

    // Функция загрузки занятых времён
    function loadBookingTimes() {
            // записываем полученные переменные
            const currentBookingId = bookingId.value;
            const tableId = bookingTable.value;
            const date = bookingDate.value;

            // Если стол или дата отсутствуют — return
            if (!tableId || !date) {return;}

            console.log("bookingId:", currentBookingId);
            console.log("tableId:", tableId);
            console.log("date:", date);


            // Запрос к заранее подготовленной функции отслеживания бронирования на выбранную дату
            fetch(
               `/restaurant/table-bookings/?table_id=${tableId}&date=${date}&booking_id=${currentBookingId}`
            )
                .then(response => response.json()) // из JSON в JavaScript-объект
                .then(data => {
                console.log("Ответ сервера:", data);

                //data = {bookings: [{start: "22:00",end: "00:00"}]}
                updateBookingTimes(data.bookings); // Передаем: bookings: [{start: "22:00",end: "00:00"}]
                });
    }

    // Пользователь выбирает стол
    bookingTable.addEventListener("change", function () { loadBookingTimes(); });
    // Пользователь выбирает дату
    bookingDate.addEventListener("change", function () { loadBookingTimes(); });

    loadBookingTimes();

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