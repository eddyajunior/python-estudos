from src.app.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Projeto Python iniciado com sucesso."
    