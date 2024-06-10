from src.gives_choice import gives_choice


def test_input_user(monkeypatch):
    # Проверка только ввода "11".
    # Остальные функции проверены в test_work_with_file
    monkeypatch.setattr('builtins.input', lambda _: '11')
    assert gives_choice() == print('Работа завершена!')
