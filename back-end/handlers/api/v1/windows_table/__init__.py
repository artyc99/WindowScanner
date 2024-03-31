import json
from dataclasses import asdict

from flask import Blueprint, request, Response

from modules.windows_calculator.calculate import get_rooms_numbers
from modules.windows_calculator.calculate_schema import GetRoomsNumbersReq

WINDOWS_TABLE = Blueprint('windows_table', url_prefix='/windows-table', import_name=__name__)


@WINDOWS_TABLE.route(rule='/', methods=['GET'])
def get_windows_table():
    return '!'


@WINDOWS_TABLE.route(rule='/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json()

        if 'rooms_per_level' not in data.keys():
            return Response(
                response='{"error": "Invalid schema: rooms_per_level not found"}',
                mimetype='application/json'
            )

        if 'level_count' not in data.keys():
            return Response(
                response='{"error": "Invalid schema: level_count not found"}',
                mimetype='application/json'
            )

        if 'rooms_state' not in data.keys():
            return Response(
                response='{"error": "Invalid schema: rooms_state not found"}',
                mimetype='application/json'
            )

        res = get_rooms_numbers(
            GetRoomsNumbersReq(
                rooms_per_level=data['rooms_per_level'],
                level_count=data['level_count'],
                rooms_state=data['rooms_state'],
            )
        )

        return Response(
            response=json.dumps(asdict(res)),
            mimetype='application/json'
        )

    except Exception as ex:
        return Response(
            response=f'{"error": "{ex}"}',
            mimetype='application/json'
        )
