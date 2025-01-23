import pandas as pd
import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, config_dir, input_dir, output_dir):
        self.config_dir = config_dir
        self.input_dir = input_dir
        self.output_dir = output_dir

    def generate_report(self):
        # Carrega os dados de entrada
        sales_data = pd.read_csv(os.path.join(self.input_dir, 'sales_data.csv'))
        report = sales_data.groupby('Category').sum()

        # Gera o caminho do relatório
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = os.path.join(self.output_dir, f'report_{timestamp}.xlsx')
        
        # Salva o relatório
        report.to_excel(report_path)
        return report_path