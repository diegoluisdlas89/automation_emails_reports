from modules.email_handler import EmailHandler
from modules.report_generator import ReportGenerator
import os

def main():
    # Configuração dos caminhos
    config_dir = os.path.join(os.getcwd(), 'config')
    data_input_dir = os.path.join(os.getcwd(), 'data', 'input')
    data_output_dir = os.path.join(os.getcwd(), 'data', 'output')

    # Inicializa o gerador de relatórios
    report_generator = ReportGenerator(config_dir, data_input_dir, data_output_dir)
    report_path = report_generator.generate_report()

    # Inicializa o manipulador de e-mails
    email_handler = EmailHandler(config_dir)
    email_handler.send_email_with_attachment(
        to=['example@domain.com'],
        subject='Relatório de Vendas',
        body='Segue em anexo o relatório de vendas.',
        attachment_path=report_path
    )

if __name__ == "__main__":
    main()