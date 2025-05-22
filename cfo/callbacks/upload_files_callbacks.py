from dash import Dash, callback, Input, Output, dash_table
import pandas as pd
import io
import base64


def create_upload_files_callbacks(dash_app: Dash, server) -> None:
    """
    Initialise callbacks
    """

    def _check_columns_exist(df: pd.DataFrame) -> pd.DataFrame:
        """
        Internal method to check if a required columns exist. If not, add
        empty column.
        """
        required_cols = ["date", "income", "category name", "amount"]
        for col in required_cols:
            if col not in df.columns:
                df[col] = pd.Series(dtype="object")
        return df

    # TODO: Add loading state for the table while it processes
    @dash_app.callback(
        Output("displayed_table", "children"), Input("upload_data", "contents")
    )
    def parse_and_display_table(contents) -> dash_table.DataTable | None:
        # Handle the case when Dash app is first initialised and all the callbacks are
        #   called; otherwise, this callback will throw an error
        if not contents:
            return None

        # Create df
        _, content_string = contents.split(",")
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(
            io.StringIO(decoded.decode("utf-8")),
        )

        # Check if columns and exist and add if not
        df = _check_columns_exist(df)

        # process date column
        # TODO: do further data processing in the next step (e.g. remove trailing and leading whitespaces)
        # TODO: Be able to display table and then further edit so validate when submitting to database
        # TODO: Inform user what is missing and what they should add
        # TODO: change to datetime before submitting to database
        # TODO: Split date and time to only show date and remove time
        df[["date", "time"]] = df["date"].str.split(" ", expand=True)

        # add row number column
        df["index"] = df.index

        # Filter df for specific columns
        filtered_df = df[["index", "date", "income", "category name", "amount"]]

        # Display uploaded csv file as a table
        common_table_config = {
            "data": filtered_df.to_dict("records"),
            "style_header": {
                "overflow": "hidden",
                "textOverflow": "ellipsis",
                "maxWidth": 0,
                "backgroundColor": "#6e6a86",
            },
            "style_data": {"backgroundColor": "#56526e"},
            "style_table": {"overflowX": "auto"},
        }

        if len(df) <= 30:
            return dash_table.DataTable(
                **common_table_config,
                page_action="none",
                fixed_rows={"headers": True},
            )
        return dash_table.DataTable(
            **common_table_config,
            page_size=10,
        )
