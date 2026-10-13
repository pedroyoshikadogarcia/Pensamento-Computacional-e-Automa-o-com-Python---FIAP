import csv
import json
from pathlib import Path
from typing import List, Optional
from model import Lead


class CRMController:

    def __init__(self, data_dir_name: str = "data"):
        self.data_dir = Path(__file__).resolve().parent / data_dir_name
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "leads.json"

    def read_leads(self) -> List[Lead]:
        if not self.db_path.exists():
            return []
        try:
            text = self.db_path.read_text(encoding="utf-8").strip()
            if not text:
                return []
            leads_data = json.loads(text)
            return [Lead.from_dict(item) for item in leads_data]
        except json.JSONDecodeError:
            return []

    def _save_all(self, leads: List[Lead]) -> None:
        """Método privado para salvar a lista de objeto Lead de volta no JSON."""
        data = [lead.to_dict() for lead in leads]
        self.db_path.write_text(json.dumps(data,
                                           ensure_ascii=False,
                                           indent=2),
                                encoding="utf-8")

    def create_lead(self, lead: Lead) -> None:
        leads = self.read_leads()
        leads.append(lead)
        self._save_all(leads)

    def query_leads(self, query: str) -> List[Lead]:
        leads = self.read_leads()
        query = query.lower()
        return [
            lead for lead in leads if query in
            f"{lead.name} {lead.company} {lead.email}".lower()
        ]

    def update_lead(self, index: int, new_lead: Lead) -> bool:
        leads = self.read_leads()
        if 0 <= index < len(leads):
            leads[index] = new_lead
            self._save_all(leads)
            return True
        return False

    def delete_lead(self, index: int) -> bool:
        leads = self.read_leads()
        if 0 <= index < len(leads):
            leads.pop(index)
            self._save_all(leads)
            return True
        return False

    def export_csv(self) -> Optional[Path]:
        path_csv = self.data_dir / "leads.csv"
        leads = self.read_leads()

        if not leads:
            return None

        try:
            with path_csv.open("w", newline="", encoding="utf-8") as file:
                fieldnames = ["name", "company", "email", "stage", "create"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for lead in leads:
                    writer.writerow(lead.to_dict())
            return path_csv
        except PermissionError:
            return None