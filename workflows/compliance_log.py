from datetime import datetime
from notion_client import notion

def log_compliance(grant_code, update_type, notes, log_db_id):
    try:
        notion.pages.create(
            parent={"database_id": log_db_id},
            properties={
                "Grant Code": {
                    "rich_text": [{"text": {"content": grant_code}}]
                },
                "Date": {
                    "date": {"start": datetime.utcnow().isoformat()}
                },
                "Type": {
                    "select": {"name": update_type}
                },
                "Notes": {
                    "rich_text": [{"text": {"content": notes}}]
                }
            }
        )
        print(f"📝 Logged update for {grant_code}")
    except Exception as e:
        print(f"❌ Error logging compliance update: {e}")
