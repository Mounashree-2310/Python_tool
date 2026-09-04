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

        df = pd.DataFrame(data)

        file_name = "pr_report.xlsx"

        df.to_excel(
            file_name,
            index=False,
        )

        workbook = load_workbook(
            file_name
        )

        worksheet = workbook.active

        for column in worksheet.columns:

            max_length = 0

            column_letter = (
                column[0].column_letter
            )

            for cell in column:

                if cell.value:

                    max_length = max(
                        max_length,
                        len(str(cell.value))
                    )

            worksheet.column_dimensions[
                column_letter
            ].width = max_length + 5

        workbook.save(
            file_name
        )