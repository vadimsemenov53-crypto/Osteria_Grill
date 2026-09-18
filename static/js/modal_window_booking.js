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

    if (modalElement) { //проверка истинности существования окна

        //создание управляемого modal-окна
        const modal = new bootstrap.Modal(modalElement);

        const hasFormErrors = modalElement.dataset.formErrors === "true";

        if (hasFormErrors) {
            modal.show();
        }

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
    }
});