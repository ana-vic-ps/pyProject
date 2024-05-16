from agenda.Tarefa import Tarefa
from agenda.Agenda import Agenda


def menu():
    print("\nAgenda de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Exibir tarefas")
    print("4. Sair")


def definindo_prioridade_tarefa():
    prioridade_tarefa = ['URGENTE', 'ALTA', 'MEDIA', 'BAIXA']
    print("\nSelecione a prioridade da tarefa: ")
    for idx, prioridade in enumerate(prioridade_tarefa, 1):
        print(f'{idx}. {prioridade}')
    while True:
        opcao = input("Escolha uma opção (1-4): ")
        if opcao in ['1', '2', '3', '4']:
            return prioridade_tarefa[int(opcao) - 1]
        else:
            print("Opção inválida. Tente novamente.")

def definindo_estado_tarefa():
    estado_tarefa = ['NÃO INICIADA', 'EM PROGESSO', 'EM PAUSA', 'CONCLUÍDA',]
    print("\nSelecione o estada da tarefa: ")
    for index, estado in enumerate(estado_tarefa, 1):
        print(f'{index}. {estado}')
    while True: 
        opcao = input ('Escolha uma opção (1-4): ')
        if opcao in ['1', '2', '3', '4']:
            return estado_tarefa[int(opcao) - 1]
        else:
            print("Opção inválida. Tente novamente.")


def main():

    agenda = Agenda()
    agenda.carregar_agenda("agenda_tarefas.txt")
    
    while True:
        
        menu()
        opcao = input('O que deseja realizar? ')

        if opcao == '1':
            
            nome = input('Digite o nome da tarefa: ')
            data_inicio = input('Digite a data de inicio da tarefa: ')
            data_termino = input('Digite a data de termino da tarefa: ')
            prioridade = definindo_prioridade_tarefa()
            estado_tarefa = definindo_estado_tarefa()
            nova_tarefa = Tarefa(nome, data_inicio, data_termino, prioridade, estado_tarefa)
            agenda.adicionar_tarefa(nova_tarefa)
            
            
        elif opcao == '2':
            nome = input('Digite o nome da tarefa a ser removida: ')
            tarefa_a_remover = None
            for tarefa in agenda.tarefas:
                if tarefa.nome == nome:
                    tarefa_a_remover = tarefa
                    break
            if tarefa_a_remover:
                agenda.remover_tarefa(tarefa_a_remover)
            else:
                print("Tarefa não encontrada.")
                
        elif opcao == '3':
            agenda.exibir_tarefas()
            
        elif opcao == '4':
            break
        
        else:
            print("Opção inválida. Tente novamente.")
                

if __name__ == "__main__":
    main()