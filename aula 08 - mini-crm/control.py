from pathlib import Path
import json, csv

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

def read_leads():
    if not DB_PATH.exists():
        return []
    try:
        text = DB_PATH.read_text(encoding="utf-8").strip()
        if not text:
            return []
        return json.loads(text)
    except json.JSONDecodeError:
        return []

def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

def query_leads(query):
    leads = read_leads()
    results = []

    for lead in leads:
        txt_lead = f"{lead.get('name', '')} {lead.get('company', '')} {lead.get('email', '')}".lower()
        if query in txt_lead:
            results.append(lead)

    return results

def export_csv():
    path_csv = DATA_DIR / "leads.csv"
    leads = read_leads()

    if not leads:
        print("Nenhum lead para exportar.")
        return None

    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=leads[0].keys())
            writer.writeheader()
            for row in leads:
                writer.writerow(row)
        return path_csv
    except PermissionError:
        return None

def update_lead(index, new_lead_dict):
    leads = read_leads()
    if 0 <= index < len(leads):
        leads[index] = new_lead_dict
        DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")
        return True
    return False

def delete_lead(index):
    leads = read_leads()
    if 0 <= index < len(leads):
        leads.pop(index)
        DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")
        return True
    return False