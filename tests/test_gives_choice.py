import pytest
from src.gives_choice import gives_choice


def test_input_user(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '11')
    assert gives_choice() == print('Работа завершена!')

    answers = iter(['1', '', '100', 'нет', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['1', 'Python', 'й', '1', 'нет', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['1', 'Python', '111', '', 'нет', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['1', 'Python', '100', 'да', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['2', 'url', 'да', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['3', 'url', 'да', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['4', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['5', 'python', 'да', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['6', '50000', 'да', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['7', 'Москва', 'да', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['8', 'да', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['9', 'да', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None

    answers = iter(['10', '11'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert gives_choice() is None
