from src.decorators import log
import pytest

def test_log_success_console(capsys):
    @log()
    def calculate(a, b):
        return a + b

    result = calculate(2, 3)

    captured = capsys.readouterr()

    assert result == 5
    assert captured.out == "calculate ok\n"


def test_log_success_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def calculate(a, b):
        return a + b

    result = calculate(2, 3)

    assert result == 5
    assert log_file.read_text(encoding="utf-8") == "calculate ok\n"


def test_log_error_console(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()

    assert captured.out == (
        "divide error: ZeroDivisionError. Inputs: (10, 0), {}\n"
    )


def test_log_error_file(tmp_path):
    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    content = log_file.read_text(encoding="utf-8")

    assert content == (
        "divide error: ZeroDivisionError. Inputs: (10, 0), {}\n"
    )


def test_log_keyword_arguments(capsys):
    @log()
    def greet(name, age):
        return f"Hello, {name}! You are {age}."

    result = greet(name="BlaBla", age=21)

    captured = capsys.readouterr()

    assert result == "Hello, BlaBla! You are 21."
    assert captured.out == "greet ok\n"


def test_log_error_with_kwargs(capsys):
    @log()
    def calculate(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        calculate(10, b=0)

    captured = capsys.readouterr()

    assert captured.out == (
        "calculate error: ZeroDivisionError. Inputs: (10,), {'b': 0}\n"
    )