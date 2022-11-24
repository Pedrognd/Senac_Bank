"""
    FEITO POR:
    CAIO JONATHAN
    LARISSA BATISTA
    LIDYANE ALVES
    LUCAS MENDONÇA
    PEDRO GABRIEL
    RYAN VINÍCIUS
    
"""
from ast import Break
import Function as fn
from User import user

class CA:
    def __init__(self,cod,tit,sen,slc,stt):
        self.AccountNumber = cod
        self.Username = tit
        self.Password = sen
        self.CheckingBalance = slc
        self.StatusLog = stt

class SA(CA):
    def __init__(self,cod='',tit='',sen=0,slc=0,stt=False):
        super().__init__(cod,tit,sen,slc,stt)
        self.SavingsBalance = 0

    # CADASTRO DE CONTA #
    def CAD(self):
        
        fn.cls()
        fn.ajustar()
        print('|' + f'{"Cadastro de Conta":^48}' + '|')
        fn.ajustar()
        
        # GERAR CÓDIGO DA CONTA #
        UserID = fn.GerCod()
        
        # NOME DO TITULAR #
        UserTIT = str(input('Digite seu Nome: ').title())
       
        # SENHA DO USUÁRIO #
        while True:
            try:
                UserSEN = int(input('Digite sua senha (4 dígitos númericos): '))
                if len(str(UserSEN)) != 4:
                    print('Sua senha não tem 4 dígitos!')
                else:
                    break
            except ValueError:
                print('Sua senha só pode conter números!')
        
        fn.ajustar()
        print('|' + f'{"Atenção!":^48}' + '|')
        print('|' + f'{"É necessário realizar um primeiro depósito":^48}' + '|')
        fn.ajustar()

        # DEPÓSITO INICIAL #
        while True:
            try:
                UserSLC = float(input('Faca um depósito inicial: '))
                if UserSLC <= 0:
                    print('Para depositar, insira um valor maior que zero.')
                else:
                    break
            except ValueError:
                print('Valor inválido')
        
        # SALVAR CONTA #
        NewUser = {
            "username": UserTIT,
            "password": UserSEN,
            "checkingBalance": UserSLC,
            "savingsBalance": 0
        }

        user[str(UserID)] = NewUser
        self.StatusLog = True
        self.ACC(str(UserID),UserSEN)
        
    # ACESSAR CONTA CADASTRADA #
    def ACC(self,User_ID='', User_SEN=0):
        tentativa = 0 
        while True:   
            if self.StatusLog == False:
                fn.cls()
                fn.ajustar()
                print('|' + f'{"Acessar Conta":^48}' + '|')
                fn.ajustar()
                User_ID = input('Insira o código da sua conta: ')
                User_SEN = int(input('Insira sua senha: '))
                
            if User_ID in user and User_SEN == user[User_ID].get('password'):
                self.StatusLog = True

                self.AccountNumber = User_ID

                self.Username = user[User_ID].get('username')
                self.Password = user[User_ID].get('password')
                self.CheckingBalance = user[User_ID].get('checkingBalance')
                self.SavingsBalance = user[User_ID].get('savingsBalance')
                break


            if self.StatusLog == False:
                print('Usuario ou a senha esta incorreta!')
                tentativa += 1
                fn.espera(2)
                if tentativa == 3:
                    fn.cls()
                    fn.ajustar()
                    print('|' + f'{"Atenção":^48}')
                    fn.ajustar()

                    print('|' + f'{"Numero de tentativas ultrapassada!":^48}' + '|')
                    print('|' + f'{"A sua conta será bloqueada":^48}' + '|')
                    print('|' + f'{"Entre em conta com a sua agencia":^48}' + '|')
                    print('|' + f'{"Fone: 0800 012 9874":^48}' + '|') # Numero ficticio #

                    fn.ajustar()
                    tentativa = 0
                    fn.espera(5)
                    MainMenu()

            else:
                fn.ajustar()
                if self.StatusLog == True:
                    pass
                else:
                    print('Você está logado')

                fn.espera(3)
                
                fn.cls()

                def escc():
                    fn.ajustar()
                    print('|' + f'{"Selecione uma das Operações":^48}' + '|')
                    fn.ajustar()
                    
                    print('|' + f'{"[1] - Mostrar Dados":<48}' + '|')
                    print('|' + f'{"[2] - Depósito":<48}' + '|')
                    print('|' + f'{"[3] - Saque":<48}' + '|')
                    print('|' + f'{"[4] - Aplicação":<48}' + '|')
                    print('|' + f'{"[5] - Resgate":<48}' + '|')
                    print('|' + f'{"[0] - Sair":<48}' + '|')

                    fn.ajustar()
                
                    esc = int(input())

                    if esc == 1:
                        aa.MTD()
                    elif esc == 2:
                        aa.DEP()
                    elif esc == 3:
                        aa.SAQ()
                    elif esc == 4:
                        aa.APL()
                    elif esc == 5:
                        aa.RES()
                    elif esc == 0:
                        self.StatusLog = False
                        MainMenu()
                    else:
                        fn.cls()
                        print('Escolha uma das operações')
                        escc()
                escc()

    def MTD(self):
        
            fn.cls()
            fn.ajustar()
            print('|' + f'{"Mostrar Dados":^48}' + '|')
            fn.ajustar()
            dados = self.__dict__

            for attr in dados:
                print(f'{attr}: {getattr(self, attr)}')
            fn.ajustar()

            test = int(input('Deseja voltar?\n\n[1] - Sim\n[2] - Encerrar Sessão\n'))
            if test == 1:
                fn.cls()
                aa.ACC()
            elif test == 2:
                self.logado = False
                fn.cls()
                MainMenu()
            else:
                fn.cls()
                print("Operação Invalida")
                aa.MTD()

    def DEP(self):
        fn.cls()
        fn.ajustar()
        print('|' + f'{"Depóstito":^48}' + '|')
        fn.ajustar()
        vD = float(input('Insira um valor para depósito: '))
        if vD < 10:
            print('Você não pode realizar o depósito com esse valor!')

        else:
            self.CheckingBalance += vD
            print('Seu depósito foi realizado com sucesso!')
        fn.espera(3)
        aa.ACC()

    def SAQ(self):
        fn.cls()
        fn.ajustar()
        print('|' + f'{"Saque":^48}' + '|')
        fn.ajustar()
        vS = float(input('Insira um valor para o saque: '))
        if vS > self.getCheckingBalance():
            print('Saldo insuficiente. Seu saldo é R$', self.getCheckingBalance())
        else:
            saldoAtual = self.getCheckingBalance()
            saldoAtual -= vS
            self.setCheckingBalance(saldoAtual)  
            print('O saque foi realizado com sucesso!')

    def APL(self):
        fn.cls()
        fn.ajustar()
        print('|' + f'{"Aplicação Poupança":^48}' + '|')
        fn.ajustar()
        vA = float(input('Insira um valor para aplicação: '))
        self.CheckingBalance -= vA
        self.SavingsBalance += vA
        print('Sua aplicação foi feita com sucesso!')
        fn.espera(3)
        aa.ACC()

    def RES(self):
        fn.cls()
        fn.ajustar()
        print('|' + f'{"Resgate Poupança":^48}' + '|')
        fn.ajustar()
        vR = float(input('Insira um valor para resgate: '))
        self.SavingsBalanceSLC -= vR
        print('Seu resgate foi efetuado com sucesso!')
        fn.espera(3)
        aa.ACC()

def MainMenu():
    fn.cls()
    try:
        fn.cls()
        fn.ajustar()
        print('|' + f'{"Bem vindo ao Senac Bank":^48}' + '|')
        fn.ajustar()
        print('|' + f'{"[1] - Acessar Conta":^48}' + '|')
        print('|' + f'{"[2] - Cadastra Conta":^48}' + '|')
        print('|' + f'{"[0] - Encerrar Sessão":^48}' + '|')
        fn.ajustar()
        esc = int(input())
        
        if esc == 1:
            aa.ACC()
        elif esc == 2:
            aa.CAD()
        elif esc == 0:
            Break
        else:
            print('Escolha uma operação valida')
            fn.espera(3)
            MainMenu()
    except ValueError:
        print('Apenas numeros')
        MainMenu()

aa = SA()
MainMenu()
