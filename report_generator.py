import json
import pandas as pd


class ReportGenerator:

    def create_json(self, data):

        with open(
            "pr_report.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    def create_excel(self, data):

        df = pd.DataFrame(data)

        df.to_excel(
            "pr_report.xlsx",
            index=False
        )