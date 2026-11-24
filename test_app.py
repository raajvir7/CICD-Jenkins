from app import main


def test_main_prints_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Jenkins!"