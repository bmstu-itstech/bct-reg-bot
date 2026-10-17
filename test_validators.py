from pathlib import Path

from bot.templates import render
from bot.validators import normalize_passport, validate_full_name, validate_group

for group in Path(__file__).with_name("groups.csv").read_text("utf-8").split():
    assert validate_group(group) is None, group
assert validate_group("иу7-63б") is None
for bad in ("", "ИУ7", "ИУ7-", "XX7-63Б", "ИУ7-63Б-22"):
    assert validate_group(bad) is not None, bad

assert normalize_passport("4510123456") == "4510 123456"
assert normalize_passport(" 4510 123456 ") == "4510 123456"
for bad in ("451 0123456", "4510-123456", "45101234567", "AB10 123456", ""):
    assert normalize_passport(bad) is None, bad

assert validate_full_name("Иванов  Иван Иванович") is None
assert validate_full_name("Иванов") is not None
assert validate_full_name("Ivanov Ivan") is not None

assert "&lt;b&gt;" in render("team_joined", team_name="<b>")

print("ok")
