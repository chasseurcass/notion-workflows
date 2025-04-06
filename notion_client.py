from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))
