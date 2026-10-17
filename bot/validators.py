from __future__ import annotations

import re

_FULL_NAME_RE = re.compile(r"^[а-яА-ЯёЁ-]+(\s+[а-яА-ЯёЁ-]+)+$")
# https://github.com/bmstu-itstech/bmstu-group-regex
_GROUP_RE = re.compile(
    r"^(ИУ|ИБМ|МТ|СМ|БМТ|РЛ|Э|РК|ФН|Л|СГН|РКТ|АК|ПС|РТ|ЛТ|К|ЮР|ЮР.ДК|МК|ИУК)"
    r"([1-9]\d?)?[КИЦ]?-[1-9]\d?([1-9]|(\.1\d))[АМБ]?В?(\/\d)?$"
)
_PASSPORT_RE = re.compile(r"^(\d{4})\s?(\d{6})$")
_TEAM_ID_RE = re.compile(r"^[a-z0-9]{8}$")


def validate_full_name(value: str) -> str | None:
    value = " ".join(value.split())
    if not _FULL_NAME_RE.match(value):
        return "ФИО должно содержать минимум 2 слова и только кириллицу/дефис."
    return None


def validate_group(value: str) -> str | None:
    if not _GROUP_RE.match(value.strip().upper()):
        return "Неверный формат группы. Пример: ИУ7-63Б."
    return None


def normalize_passport(value: str) -> str | None:
    """Return passport as '1234 567890', or None if it is not a valid RF passport."""
    m = _PASSPORT_RE.match(value.strip())
    if m is None:
        return None
    return f"{m.group(1)} {m.group(2)}"


def validate_team_id(value: str) -> str | None:
    if not _TEAM_ID_RE.match(value.strip().lower()):
        return "ID команды должен содержать 8 символов (a-z, 0-9)."
    return None


def validate_team_name(value: str) -> str | None:
    name = value.strip()
    if not name:
        return "Название команды не может быть пустым."
    if len(name) > 31:
        return "Название команды не должно превышать 31 символ."
    return None
