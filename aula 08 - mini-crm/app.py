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


def list_leads():
    leads = control.read_leads()

    if not leads:
        print("Nenhum lead encontrado.")
        return

    print("\n#  | Nome                 | Empresa           | Email                | Estágio")
    print("-" * 75)
    for i, lead in enumerate(leads):
        print(
            f"{i:02d} | {lead.get('name', ''):<20} | {lead.get('company', ''):<17} | {lead.get('email', ''):<20} | {lead.get('stage', ''):<10}")


def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta vazia.")
        return

    leads_found = control.query_leads(query)
    if not leads_found:
        print("Nenhum resultado encontrado.")
        return

    print("\n#  | Nome                 | Empresa           | Email                | Estágio")
    print("-" * 75)
    for i, lead in enumerate(leads_found):
        print(
            f"{i:02d} | {lead.get('name', ''):<20} | {lead.get('company', ''):<17} | {lead.get('email', ''):<20} | {lead.get('stage', ''):<10}")


def update_lead():
    list_leads()
    leads = control.read_leads()
    if not leads:
        return

    try:
        index = int(input("\nDigite o # do lead que deseja atualizar: "))
        if index < 0 or index >= len(leads):
            print("Índice inválido!")
            return
    except ValueError:
        print("Digite um número válido!")
        return

    lead_atual = leads[index]
    print(f"\nAtualizando lead: {lead_atual.get('name')}")
    print("(Pressione Enter sem digitar nada para manter o valor atual)")

    name = input(f"Novo Nome [{lead_atual.get('name')}]: ").strip() or lead_atual.get('name')
    company = input(f"Nova Empresa [{lead_atual.get('company')}]: ").strip() or lead_atual.get('company')
    email = input(f"Novo Email [{lead_atual.get('email')}]: ").strip() or lead_atual.get('email')
    stage = input(f"Novo Estágio [{lead_atual.get('stage')}]: ").strip() or lead_atual.get('stage')

    updated_lead = model_lead(name, company, email, stage)
    # Preserva a data de criação original do lead
    updated_lead['create'] = lead_atual.get('create')

    if control.update_lead(index, updated_lead):
        print("Lead atualizado com sucesso!")
    else:
        print("Erro ao atualizar o lead.")


def delete_lead():
    list_leads()
    leads = control.read_leads()
    if not leads:
        return

    try:
        index = int(input("\nDigite o # do lead que deseja DELETAR: "))
    except ValueError:
        print("Digite um número válido!")
        return

    if 0 <= index < len(leads):
        confirm = input(f"Tem certeza que deseja deletar '{leads[index].get('name')}'? (s/n): ").strip().lower()
        if confirm == 's':
            if control.delete_lead(index):
                print("Lead removido com sucesso!")
            else:
                print("Erro ao remover o lead.")
        else:
            print("Operação cancelada.")
    else:
        print("Índice inválido!")


def export_leads():
    path_csv = control.export_csv()
    if path_csv is None:
        print("Não foi possível exportar os leads para CSV.")
    else:
        print(f"CSV exportado com sucesso para: {path_csv}")


def main():
    while True:
        print("\n--- Mini CRM (CRUD Completo) ---")
        print("[1] Adicionar lead (Create)")
        print("[2] Listar leads (Read)")
        print("[3] Buscar (Read)")
        print("[4] Atualizar lead (Update)")
        print("[5] Deletar lead (Delete)")
        print("[6] Exportar para CSV")
        print("[0] Sair")

        cpt = input("Escolha uma opção: ").strip()
        if cpt == "1":
            add_lead()
        elif cpt == "2":
            list_leads()
        elif cpt == "3":
            search_leads()
        elif cpt == "4":
            update_lead()
        elif cpt == "5":
            delete_lead()
        elif cpt == "6":
            export_leads()
        elif cpt == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()