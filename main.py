import requests
from datetime import datetime, timezone, timedelta

with open('token.txt', 'r') as f:
    token = f.read()

mutation = """
mutation($message: String, $emoji: String, $expiresAt: DateTime) {
  changeUserStatus(input: {
    message: $message,
    emoji: $emoji,
    expiresAt: $expiresAt
  }) {
    status {
      message
      emoji
      expiresAt
    }
  }
}
"""

def set_status(message: str, emoji: str = None, expires_at: str = None):
    variables = {
        "message": message,
        "emoji": emoji,          # None = no emoji
        "expiresAt": expires_at, # None = no expiration, else ISO 8601 string
    }
    resp = requests.post(
        "https://api.github.com/graphql",
        headers={"Authorization": f"Bearer {token}"},
        json={"query": mutation, "variables": variables},
    )
    return resp.json()

# No expiration


# Expires in 4 hours
expires = (datetime.now(timezone.utc) + timedelta(hours=2)).isoformat()
print(set_status("Coding", "", expires))
