import json
import base64

config = {
    "organization": [
        {
            "token": "",
        },
        # Optional: Add additional orgs or GitHub Enterprise instances
        # {
        #     "token": "ghp_enterprise_token",
        #     "url": "https://github.example.com/api/graphql",
        #     "name": "enterprise-org-name",
        # },
    ]
}

# Encode the configuration
encoded = base64.b64encode(json.dumps(config).encode()).decode()
print(encoded)
