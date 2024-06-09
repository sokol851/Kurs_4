import pytest
from src.gives_choice import gives_choice


def test_input_user(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '11')
    assert gives_choice() == print('Работа завершена!')
