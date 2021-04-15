from typing import List, Optional
from django.db import connection


def sql_fetch_all(sql: str, params: list = []) -> Optional[List[dict]]:
    result = []

    with connection.cursor() as cursor:
        cursor.execute(sql, params)

        if cursor.description is None:
            return None

        columns = [column[0] for column in cursor.description]

        for item in cursor.fetchall():
            result.append(dict(zip(columns, item)))

    return result


def sql_fetch_one(sql: str, params: list = []) -> Optional[dict]:
    result = []

    with connection.cursor() as cursor:
        cursor.execute(sql, params)

        if cursor.description is None:
            return None

        columns = [column[0] for column in cursor.description]

        item = cursor.fetchone()

        if item:
            result = dict(zip(columns, item))

    return result
