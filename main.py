from workflows.archive import archive_closed_grants
from workflows.compliance_log import log_compliance
from workflows.export import export_database_to_csv

# Replace with your actual Notion database IDs
GRANT_DB_ID = "your-grant-database-id"
LOG_DB_ID = "your-log-database-id"

# Example usage
archive_closed_grants(GRANT_DB_ID)
log_compliance("23F01", "SAM Renewal", "Reminder sent to OSBI", LOG_DB_ID)
export_database_to_csv(GRANT_DB_ID, filename="grant_report.csv")
