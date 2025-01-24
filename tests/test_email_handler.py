import pytest
from modules.email_handler import EmailHandler


def test_send_email():
    config_dir = "config"
    email_handler = EmailHandler(config_dir)

    subject = "Teste de envio de e-mail"
    body = "Este é um teste para verificar o envio de e-mails no projeto."
    recipients = ["diego.luis@prf.gov.br"]  # Atualize com um e-mail válido

    try:
        email_handler.send_email(subject, body, recipients)
        assert True  # Passa se não houver exceções
    except AssertionError as e:
        pytest.fail(str(e))
