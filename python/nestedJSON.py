#import pandas as pd
import json

data = '''
{
    "rows": [
        {
            "Glo - Web": {
                "rows": [
                    {
                        "attr_dependency": {
                            "campaign_id_network": "unknown",
                            "partner_id": "-300",
                            "partner": "Organic"
                        },
                        "app": "Test app",
                        "partner_name": "Organic",
                        "campaign": "unknown",
                        "campaign_id_network": "unknown",
                        "campaign_network": "unknown",
                        "installs": "10",
                        "network_installs": "0",
                        "network_cost": "0.0",
                        "network_ecpi": "0.0"
                    }
                ],
                "totals": {
                    "installs": 10.0,
                    "network_installs": 0.0,
                    "network_cost": 0.0,
                    "network_ecpi": 0.0
                },
                "warnings": [],
                "pagination": null
            }
        }
    ]
}
'''

# Load JSON data
json_data = json.loads(data)

# Extract rows from JSON and flatten them
rows = []
for row in json_data["rows"]:
    for key, value in row.items():
        rows += value["rows"]

print(rows)
# Convert rows to Pandas DataFrame
#df = pd.json_normalize(rows)

# Print DataFrame
#print(df)
