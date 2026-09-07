import json, re

def check_all_fields():
    files = [
        ('stull', 'data/stull-data.js'),
        ('dispense', 'data/dispense-data.js'),
        ('cards', 'data/progetto-cards-data.js'),
        ('krug', 'data/krug-data.js'),
        ('arte', 'data/arte-data.js')
    ]
    
    for label, path in files:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        start_arr = text.find('[')
        start_obj = text.find('{')
        if start_arr != -1 and (start_obj == -1 or start_arr < start_obj):
            end = text.rfind(']') + 1
            data = json.loads(text[start_arr:end])
        else:
            end = text.rfind('}') + 1
            data = json.loads(text[start_obj:end])
            
        items = data if isinstance(data, list) else (data.get('chapters') or data.get('modules') or list(data.values()))
        if isinstance(items, dict):
            items = list(items.values())
            
        print(f"\n=================== {label.upper()} ({path}) ===================")
        for item in items:
            item_id = item.get('id') or item.get('number')
            for field, val in item.items():
                if isinstance(val, str):
                    check_text(f"{item_id}.{field}", val)
                elif isinstance(val, list):
                    for idx, sub in enumerate(val):
                        if isinstance(sub, str):
                            check_text(f"{item_id}.{field}[{idx}]", sub)
                        elif isinstance(sub, dict):
                            for sub_k, sub_v in sub.items():
                                if isinstance(sub_v, str):
                                    check_text(f"{item_id}.{field}[{idx}].{sub_k}", sub_v)
                                elif isinstance(sub_v, list):
                                    for opt_idx, opt_str in enumerate(sub_v):
                                        if isinstance(opt_str, str):
                                            check_text(f"{item_id}.{field}[{idx}].{sub_k}[{opt_idx}]", opt_str)

def check_text(location, s):
    # Cerca $$
    if '$$' in s:
        print(f"[$$] in {location}: {s[:100]}")
    # Cerca \text{
    if '\\text{' in s:
        print(f"[\\text] in {location}: {s[:100]}")
    # Cerca \frac
    if '\\frac' in s:
        print(f"[\\frac] in {location}: {s[:100]}")
    # Cerca ```
    if '```' in s:
        print(f"[```] in {location}: {s[:100]}")
    # Cerca $ single
    singles = re.findall(r'(?<!\$)\$([^\$\n]+)\$(?!\$)', s)
    for m in singles:
        if any(c in m for c in ['\\', 'pm', 'cdot', 'times', 'log']):
            print(f"[single $ math] in {location}: ${m}$")

check_all_fields()
