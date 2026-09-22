from model import model_lead
import control


def add_lead():
    name = input("Nome: ").strip()
    email = input("Email: ").strip()
    company = input("Empresa: ").strip()
    stage = input("Estágio de Vendas: ").strip()

    if not name or not email or "@" not in email:
        print("Nome e/ou email válido são obrigatórios.")
        return

    lead = model_lead(name, company, email, stage)
    print("\nLead gerado:", lead)

    control.create_lead(lead)
    print("Lead salvo com sucesso!")


def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta vazia")
        return

    leads_found = control.query_leads(query)
    if not leads_found:
        print("Nenhum resultado encontrado.")
        return

    print("\n#  | Nome                 | Empresa           | Email")
    print("-" * 60)
    for i, lead in enumerate(leads_found):
        print(f"{i:02d} | {lead['name']:<20} | {lead['company']:<17} | {lead['email']:<20}")


def export_leads():
    path_csv = control.export_csv()
    if path_csv is None:
        print("Não foi possível exportar os leads para CSV.")
    else:
        print(f"CSV exportado para {path_csv}")


def list_leads():
    leads = control.read_leads()

    if not leads:
        print("Nenhum lead ainda.")
        return

    print("\n#  | Nome                 | Empresa           | Email")
    print("-" * 60)
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead['name']:<20} | {lead['company']:<17} | {lead['email']:<20}")


def main():
    while True:
        print("\n--- Mini CRM ---")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome, email, empresa)")
        print("[4] Exportar para CSV")
        print("[0] Sair")

        cpt = input("Escolha uma opção: ").strip()
        if cpt == "1":
            add_lead()
        elif cpt == "2":
            list_leads()
        elif cpt == "3":
            search_leads()
        elif cpt == "4":
            export_leads()
        elif cpt == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()