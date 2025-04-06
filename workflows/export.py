import pandas as pd
from notion_client import notion

def export_database_to_csv(database_id, filename="export.csv"):
    try:
        response = notion.databases.query(database_id=database_id)
        rows = []

        for page in response["results"]:
            props = page["properties"]
            row = {
                "ID": page["id"],
                "Name": props["Name"]["title"][0]["plain_text"] if props["Name"]["title"] else ""
                # Add more fields based on your database structure
            }
            rows.append(row)

        df = pd.DataFrame(rows)
        df.to_csv(filename, index=False)
        print(f"📤 Exported {len(rows)} records to {filename}")
    except Exception as e:
        print(f"❌ Error exporting data: {e}")
