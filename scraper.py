import json
from datetime import datetime

data = [
    {"name": "Product A", "price": "৳100"},
    {"name": "Product B", "price": "৳200"}
]

filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Saved dummy data to {filename}")
