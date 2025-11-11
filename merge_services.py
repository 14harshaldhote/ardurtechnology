import json

# Load all service files
with open('app/data/services_detail.json', 'r') as f:
    existing_services = json.load(f)

with open('app/data/services_complete.json', 'r') as f:
    mortgage_services = json.load(f)

with open('app/data/aircraft_services.json', 'r') as f:
    aircraft_services = json.load(f)

# Merge all services
all_services = {**existing_services, **mortgage_services, **aircraft_services}

# Write merged services
with open('app/data/services_detail.json', 'w') as f:
    json.dump(all_services, f, indent=2)

print(f"✅ Merged {len(all_services)} services successfully!")
print(f"   - Existing services: {len(existing_services)}")
print(f"   - Mortgage services: {len(mortgage_services)}")
print(f"   - Aircraft services: {len(aircraft_services)}")
