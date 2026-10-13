from model import Lead
from control import CRMController


class CRMCLI:

    def __init__(self):
        self.controller = CRMController()

    def add_lead(self):
        name = input("Nome: ").strip()
        email = input("Email: ").strip()
        company = input("Empresa: ").strip()
        stage = input("Estágio de Vendas: ").strip()

        lead = Lead(name=name, company=company, email=email, stage=stage)

        if not lead.is_valid():
            print("Nome e/ou email válido são obrigatórios.")
            return

        print("\nLead gerado:", lead)
        self.controller.create_lead(lead)
        print("Lead salvo com sucesso!")

    def _display_leads(self, leads: list[Lead]):
        print(
            "\n#  | Nome                 | Empresa           | Email                | Estágio"
        )
        print("-" * 75)
        for i, lead in enumerate(leads):
            print(
                f"{i:02d} | {lead.name:<20} | {lead.company:<17} | {lead.email:<20} | {lead.stage:<10}"
            )

    def list_leads(self):
        leads = self.controller.read_leads()
        if not leads:
            print("Nenhum lead encontrado.")
            return
        self._display_leads(leads)

    def search_leads(self):
        query = input("Buscar por: ").strip()
        if not query:
            print("Consulta vazia.")
            return

        leads_found = self.controller.query_leads(query)
        if not leads_found:
            print("Nenhum resultado encontrado.")
            return

        self._display_leads(leads_found)

    def update_lead(self):
        leads = self.controller.read_leads()
        if not leads:
            print("Nenhum lead encontrado.")
            return

        self.list_leads()

        try:
            index = int(input("\nDigite o # do lead que deseja atualizar: "))
            if index < 0 or index >= len(leads):
                print("Índice inválido!")
                return
        except ValueError:
            print("Digite um número válido!")
            return

        lead_atual = leads[index]
        print(f"\nAtualizando lead: {lead_atual.name}")
        print("(Pressione Enter sem digitar nada para manter o valor atual)")

        name = input(
            f"Novo Nome [{lead_atual.name}]: ").strip() or lead_atual.name
        company = input(f"Nova Empresa [{lead_atual.company}]: ").strip(
        ) or lead_atual.company
        email = input(
            f"Novo Email [{lead_atual.email}]: ").strip() or lead_atual.email
        stage = input(f"Novo Estágio [{lead_atual.stage}]: ").strip(
        ) or lead_atual.stage

        updated_lead = Lead(name=name,
                            company=company,
                            email=email,
                            stage=stage,
                            created_at=lead_atual.created_at)

        if self.controller.update_lead(index, updated_lead):
            print("Lead atualizado com sucesso!")
        else:
            print("Erro ao atualizar o lead.")

    def delete_lead(self):
        leads = self.controller.read_leads()
        if not leads:
            print("Nenhum lead encontrado.")
            return

        self.list_leads()

        try:
            index = int(input("\nDigite o # do lead que deseja DELETAR: "))
        except ValueError:
            print("Digite um número válido!")
            return

        if 0 <= index < len(leads):
            confirm = input(
                f"Tem certeza que deseja deletar '{leads[index].name}'? (s/n): "
            ).strip().lower()
            if confirm == "s":
                if self.controller.delete_lead(index):
                    print("Lead removido com sucesso!")
                else:
                    print("Erro ao remover o lead.")
            else:
                print("Operação cancelada.")
        else:
            print("Índice inválido!")

    def export_leads(self):
        path_csv = self.controller.export_csv()
        if path_csv is None:
            print("Não foi possível exportar os leads para CSV.")
        else:
            print(f"CSV exportado com sucesso para: {path_csv}")

    def run(self):
        while True:
            print("\n--- Mini CRM (CRUD POO) ---")
            print("[1] Adicionar lead (Create)")
            print("[2] Listar leads (Read)")
            print("[3] Buscar (Read)")
            print("[4] Atualizar lead (Update)")
            print("[5] Deletar lead (Delete)")
            print("[6] Exportar para CSV")
            print("[0] Sair")

            cpt = input("Escolha uma opção: ").strip()
            if cpt == "1":
                self.add_lead()
            elif cpt == "2":
                self.list_leads()
            elif cpt == "3":
                self.search_leads()
            elif cpt == "4":
                self.update_lead()
            elif cpt == "5":
                self.delete_lead()
            elif cpt == "6":
                self.export_leads()
            elif cpt == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")


if __name__ == "__main__":
    app = CRMCLI()
    app.run()