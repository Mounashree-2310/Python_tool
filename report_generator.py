import json
import pandas as pd


class ReportGenerator:

    def create_json(
        self,
        data,
        filename="pr_report.json"
    ):

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    def create_excel(
        self,
        data,
        filename="pr_report.xlsx"
    ):

        df = pd.DataFrame(data)

        df.to_excel(
            filename,
            index=False
        )