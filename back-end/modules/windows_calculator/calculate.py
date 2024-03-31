from typing import Union

from modules.windows_calculator.calculate_schema import GetRoomsNumbersReq, GetRoomsNumbersRes


def get_rooms_numbers(req: GetRoomsNumbersReq) -> Union[GetRoomsNumbersRes, None]:
    if sum(req.rooms_per_level) != len(req.rooms_state[0]):
        return None

    active_rooms = []
    rooms_counter = 0
    for level_index in range(len(req.rooms_state)):
        for room_number in req.rooms_per_level:
            rooms_counter += 1
            if sum(req.rooms_state[level_index][:room_number]):
                active_rooms.append(rooms_counter)
            req.rooms_state[level_index] = req.rooms_state[level_index][room_number:]

    return GetRoomsNumbersRes(rooms=active_rooms, rooms_count=len(active_rooms))



