import json
import os

import pandas as pd
from openpyxl import load_workbook


class ReportGenerator:

    def create_json(
        self,
        data,
    ):

        os.makedirs(
            "reports",
            exist_ok=True,
        )

        with open(
            "reports/pr_report.json",
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

        os.makedirs(
            "reports",
            exist_ok=True,
        )

        file_name = (
            "reports/pr_report.xlsx"
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

        worksheet = workbook.active

        workbook.save(
            file_name
        )
