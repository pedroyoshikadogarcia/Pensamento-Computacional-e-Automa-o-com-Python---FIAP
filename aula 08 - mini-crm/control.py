

from pathlib import Path
import json, csv

DATA_DIR = Path(__file__).resolve().parent /"data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

# CRUD
# CREATE - create_lead()
# READ - read_leads()
# UPDATE
# DELETE

def read_leads():
    if not DB_PATH.exists():
        return[]
    try: json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")
def read_lead_search(query):
    leads = read_leads() #Lista de leads
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["company"]} {lead["email"]}".lower()

        if query in txt_lead:
            results.append(lead)

    if not results:
        print("No results")
        return[]
    else:
        return results

def export_csv():
    # Exporta os leads para um CSV
    path_csv = DATA_DIR / "leads.csv"
    leads = read_leads()

    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=leads[0].keys())
            writer.writeheader()
            for row in leads:
                writer.writerow(row)
        return path_csv
    except PermissionError:
        return None