<template>
    <div class="windows-table-form">
        <div class="form-data">
            <input type="text" class="levels-count" value="5">
            <input type="text" class="rooms-per-level" value="4">
            <input type="text" class="rooms" value="2,2">
        </div>
        <div class="dormitories">
            <div class="dormitory">
                <div class="level" v-for="level_data in room_number">
                    <div class="window-selector" v-for="room_n in level_data" @click="active($event)">
                        {{ room_n }}
                    </div>
                </div>
            </div>
        </div>
        <div class="result">
            <div class="rooms">
                Комнаты: {{rooms_result}}
            </div>
            <div class="count">
                Количесво: {{rooms_count_result}}
            </div>
        </div>
        <button @click="show($event)">Показать</button>
        <button @click="calculate($event)">Расчитать</button>
    </div>
    <div class="windows-table">
        <div class="dates">
            <div class="date" @click="test($event)">
              22.02.2020
            </div>
            <div class="date">
              22.02.2020
            </div>
            <div class="date">
              22.02.2020
            </div>
            <div class="date">
              22.02.2020
            </div>
        </div>
        <div class="dormitories">
            <div class="dormitory">
                <div class="level">
                    <div class="window active">
                        1
                    </div>
                    <div class="window">
                        2
                    </div>
                    <div class="window">
                        3
                    </div>
                    <div class="window">
                        4
                    </div>
                    <div class="window">
                        5
                    </div>
                </div>
                <div class="level">
                    <div class="window">
                        1
                    </div>
                    <div class="window">
                        2
                    </div>
                    <div class="window">
                        3
                    </div>
                    <div class="window">
                        4
                    </div>
                    <div class="window">
                        5
                    </div>
                </div>
                <div class="level">
                    <div class="window">
                        1
                    </div>
                    <div class="window">
                        2
                    </div>
                    <div class="window">
                        3
                    </div>
                    <div class="window">
                        4
                    </div>
                    <div class="window">
                        5
                    </div>
                </div>
            </div>
            <div class="dormitory">
                <div class="level">
                    <div class="window">
                        1
                    </div>
                    <div class="window">
                        2
                    </div>
                    <div class="window">
                        3
                    </div>
                    <div class="window">
                        4
                    </div>
                    <div class="window">
                        5
                    </div>
                </div>
                <div class="level">
                    <div class="window">
                        1
                    </div>
                    <div class="window">
                        2
                    </div>
                    <div class="window">
                        3
                    </div>
                    <div class="window">
                        4
                    </div>
                    <div class="window">
                        5
                    </div>
                </div>
                <div class="level">
                    <div class="window">
                        1
                    </div>
                    <div class="window">
                        2
                    </div>
                    <div class="window">
                        3
                    </div>
                    <div class="window">
                        4
                    </div>
                    <div class="window">
                        5
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

import {ref} from "vue";

const levels_count = ref(0);
const rooms_per_level = ref(0);
const rooms = ref([]);

const room_number = ref([]);

const rooms_result = ref([]);
const rooms_count_result = ref(0);

const show = (event) => {
    let rooms_b = [];
    let room_per_level_b = 0;
    let levels_count_b = 0;

    const levels_count_buf = document.querySelector('.levels-count');
    const rooms_per_level_buf = document.querySelector('.rooms-per-level');
    const rooms_buf = document.querySelector('.rooms');
    if (levels_count_buf) {
        levels_count_b = Number(levels_count_buf.value);
        levels_count.value = levels_count_b;
    }
    if (rooms_per_level_buf) {
        room_per_level_b = Number(rooms_per_level_buf.value);
        rooms_per_level.value = room_per_level_b;
    }
    if (rooms_buf) {
        rooms_b = rooms_buf.value.split(',').map(Number);
        rooms.value = rooms_b;
    }

    let room_numb = 1;
    for (let level_index of Array(levels_count_b).keys()) {
        let rooms_buf = [];
        let counter = 0;
        for (let value in rooms_b) {
            for (let index of Array(rooms_b[value]).keys()) {
                rooms_buf[counter] = room_numb;
                counter = counter + 1;
            }
            room_numb = room_numb + 1;
            console.log(value);
        }
        room_number.value[level_index] = rooms_buf;
    }
};

const active = (event) => {
    if (event.currentTarget.classList.contains('active')){
        event.currentTarget.classList.remove('active');
    } else {
        event.currentTarget.classList.add('active');
    }
}

const calculate = (event) => {

    let counter = 0;
    let buf_counter = 0;
    let levels_data_buf = [];
    let levels_data = [];

    const levels = event.currentTarget.parentElement.querySelectorAll('.window-selector').forEach(
        (item) => {
            if (counter === rooms_per_level.value - 1) {
                levels_data_buf[counter] = Boolean(item.classList.contains('active'));
                levels_data[buf_counter] = levels_data_buf;
                levels_data_buf = [];
                buf_counter = buf_counter + 1;
                counter = 0;
            } else {
                levels_data_buf[counter] = Boolean(item.classList.contains('active'));
                counter = counter + 1;
            }
        }
    )

    const req = fetch('http://localhost:5000/api/v1/windows-table/calculate', {
        method: 'POST',
        mode: "cors",
        credentials: "include",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({"rooms_per_level": rooms.value, "level_count": levels_count.value, "rooms_state": levels_data})
    }).then((res) => {
        let buf = res.json();
        rooms_result.value = buf.rooms;
        rooms_count_result.value = buf.rooms_count;
    })
        .catch((ex) => console.log(ex));
};
</script>

<style scoped>
.windows-table {
    display: flex;
    flex-direction: row;

    height: 100%;
    width: 100%;
}

.windows-table-form {
    display: flex;
    flex-direction: row;

    height: 100%;
    width: 100%;
}

.dates {
    display: flex;
    flex-direction: column;
    padding: 1%;
    margin: .5%;
    flex: 1;

    border-radius: 10px;
    background-color: lightgray;
}

.form-data {
    display: flex;
    flex-direction: column;
    padding: 1%;
    margin: .5%;
    flex: 1;

    border-radius: 10px;
    background-color: lightgray;
}

.form-data input {
    display: flex;
    align-content: center;
    justify-content: center;

    margin: 5%;

    border-radius: 10px;

    background-color: darkgray;
}

.date {
    display: flex;
    align-content: center;
    justify-content: center;

    margin: 5%;

    border-radius: 10px;

    background-color: darkgray;
    cursor: pointer;
}

.dormitories {
    display: flex;
    flex-direction: column;
    padding: 1%;
    margin: .5%;
    flex: 9;

    border-radius: 10px;
    background-color: lightgray;
}

.dormitory {
    display: flex;
    flex-direction: column;

    margin: 1%;

    align-items: center;
    justify-content: center;
}

.level {
    display: flex;
    flex-direction: row;
}

.window {
    padding: 50%;
    background-color: gray;

    border-radius: 10px;
}

.window.active {
    background-color: yellowgreen;
}

.window-selector {
    padding: 50%;
    background-color: gray;

    border-radius: 10px;
    cursor: pointer;
}

.window-selector.active {
    background-color: yellowgreen;
}
</style>