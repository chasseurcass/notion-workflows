from notion_client import errors
from notion_client import Client
from datetime import datetime
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import Client
from notion_client import errors
from notion_client import notion

def archive_closed_grants(database_id):
    today = datetime.utcnow().isoformat()
    try:
        response = notion.databases.query(
            database_id=database_id,
            filter={
                "property": "End Date",
                "date": {"before": today}
            }
        )
        for page in response["results"]:
            notion.pages.update(page_id=page["id"], archived=True)
            print(f"✅ Archived: {page['id']}")
    except errors.APIResponseError as e:
        print(f"❌ Error archiving pages: {e}")
