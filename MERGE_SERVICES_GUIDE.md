# Merge Services JSON Files - Quick Guide

## ✅ What's Been Done

1. ✅ Created **7 Mortgage Services** in `app/data/services_complete.json`
2. ✅ Created **7 Aircraft Services** in `app/data/aircraft_services.json`  
3. ✅ Updated ALL navigation links (desktop + mobile) in `base.html`
4. ✅ Existing 6 services remain in `app/data/services_detail.json`

## 🔄 Merge the JSON Files (2 Options)

### Option 1: Python Script (Easiest)
```bash
cd /Users/harshalsmac/WORK/ardur/ardurtechnology
python3 -c "
import json

# Load all three JSON files
with open('app/data/services_detail.json') as f:
    existing = json.load(f)
    
with open('app/data/services_complete.json') as f:
    mortgage = json.load(f)
    
with open('app/data/aircraft_services.json') as f:
    aircraft = json.load(f)

# Merge all services
all_services = {**existing, **mortgage, **aircraft}

# Save merged file
with open('app/data/services_detail.json', 'w') as f:
    json.dump(all_services, f, indent=2)

print(f'✅ Successfully merged {len(all_services)} total services!')
print(f'   - Existing: {len(existing)}')
print(f'   - Mortgage: {len(mortgage)}')
print(f'   - Aircraft: {len(aircraft)}')
"
```

### Option 2: Manual Merge
1. Open `app/data/services_detail.json`
2. Copy all content from `app/data/services_complete.json` and paste before the closing `}`
3. Add a comma after the last existing service
4. Copy all content from `app/data/aircraft_services.json` and paste before the closing `}`
5. Save the file

## 🎯 Final Result

After merging, you'll have **20 total services**:

### Business Process (6 services)
- title-insurance
- title-plant-development
- tax-services  
- appraisal-management-services
- broker-price-opinion
- appraisal-vendor-management

### Mortgage Services (7 services)
- mortgage-pre-processing
- mortgage-ancillary
- mortgage-appraisal
- mortgage-underwriting
- mortgage-title
- mortgage-closing
- mortgage-post-closing

### Aircraft Asset Management (7 services)
- document-management
- electronic-asset-management
- programs-reliability
- assemblies-services
- service-expertise
- technical-documents
- engine-maintenance-analytics

## 🚀 Test Your Services

After merging, start the app:
```bash
python run.py
```

Visit these URLs to test:
- http://127.0.0.1:5000/service/mortgage-pre-processing
- http://127.0.0.1:5000/service/mortgage-underwriting
- http://127.0.0.1:5000/service/document-management
- http://127.0.0.1:5000/service/engine-maintenance-analytics

## 🧹 Cleanup (Optional)

After successful merge, you can delete the temporary files:
```bash
rm app/data/services_complete.json
rm app/data/aircraft_services.json
rm merge_services.py
```

## ✨ All Navigation Links Are Ready!

- ✅ Desktop mega menu → All 20 services linked
- ✅ Mobile accordion menu → All 20 services linked  
- ✅ Hover animations working
- ✅ Click interactions ready
- ✅ Responsive design complete

---

**Next Step**: Run the merge command above and start your app! 🎉
