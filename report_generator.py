import json
 
import pandas as pd
from openpyxl import load_workbook
 
 
class ReportGenerator:
 
    def create_json(
        self,
        data,
    ):
 
        with open(
            "pr_report.json",
            "w",
            encoding="utf-8",
        ) as file:
 
            json.dump(
                data,
                file,
                indent=4,
            )
 
    def create_excel(
        self,
        data,
    ):
 
        file_name = (
            "pr_report.xlsx"
        )
 
        pd.DataFrame(
            data
        ).to_excel(
            file_name,
            index=False,
        )
 
        workbook = load_workbook(
            file_name
        )
 
        sheet = workbook.active
 
        for column in sheet.columns:
 
            max_length = max(
                len(str(cell.value))
                if cell.value
                else 0
                for cell in column
            )
 
            sheet.column_dimensions[
                column[0].column_letter
            ].width = max_length + 5
 
        workbook.save(
            file_name
        )