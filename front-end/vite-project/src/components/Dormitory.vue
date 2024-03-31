<template>
    <div class="windows-table">
        <div class="dates">
            <div class="date">
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

</script>

<style scoped>
.windows-table {
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
</style>