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
        
    def getCheckingBalance(self):
        return self.__CheckingBalance

    def setCheckingBalance(self):
        return self.__CheckingBalance

    def getSavingsBalance(self):
        return self.__SavingsBalance

    def setSavingsBalance(self):
        return self.__SavingsBalance


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
        
        fn.ajustar()
        print('Deposito efetuado com sucesso!')
        print('Conta criada com sucesso')
        
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
        
        if self.StatusLog == False:
            fn.cls()
            fn.ajustar()
            print('|' + f'{"Acessar Conta":^48}' + '|')
            fn.ajustar()
            User_ID = input('Insira o código da sua conta: ')
            User_SEN = int(input('Insira sua senha: '))

        # VERIFICAÇÃO DE LOGIN #    
        if User_ID in user and User_SEN == user[User_ID].get('password'):
            self.StatusLog = True

            self.AccountNumber = User_ID

            self.Username = user[User_ID].get('username')
            self.Password = user[User_ID].get('password')
            self.CheckingBalance = user[User_ID].get('checkingBalance')
            self.SavingsBalance = user[User_ID].get('savingsBalance')


        if self.StatusLog == False:
            print('Usuario nao existe, ou a senha esta incorreta!')
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
                
                # CHAMANDO FUNÇÕES #
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

    # FUNÇÃO DE MOSTRAR DADOS #
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
                self.StatusLog = False
                fn.cls()
                MainMenu()
            else:
                fn.cls()
                print("Operação Invalida")
                aa.MTD()

    # FUNÇÃO DE DEPOSITO #
    def DEP(self):
        fn.cls()
        fn.ajustar()
        print('|' + f'{"Depóstito":^48}' + '|')
        fn.ajustar()
        while True:
            try:
                vD = float(input('Insira um valor para depósito: R$ '))
                if vD < 10:
                    print('Valor minimo de R$ 10,00 !')

                else:
                    SLCant = self.CheckingBalance
                    self.CheckingBalance += vD
                    print('Seu depósito foi realizado com sucesso!')
                    print('Saldo antes do deposito: R$ ',SLCant)
                    print('Saldo depois do deposito: R$ ',self.CheckingBalance)
                fn.espera(3)
                aa.ACC()
                break
            except ValueError:
                print('Insira um valor valido!')

    # FUNÇÃO DE SAQUE #
    def SAQ(self):
        fn.cls()
        fn.ajustar()
        print('|' + f'{"Saque":^48}' + '|')
        fn.ajustar()
        try:
            print('Valor disponivel para saque: R$ ',self.CheckingBalance)
            vS = float(input('Insira um valor para o saque: R$ '))
            if vS > self.getCheckingBalance():
                print('Saldo insuficiente. Seu saldo é R$', self.getCheckingBalance())
            else:
                saldoAtual = self.getCheckingBalance()
                saldoAtual -= vS
                self.setCheckingBalance(saldoAtual)  
                print('O saque foi realizado com sucesso!')
        except AttributeError:
            print('Erro')
            aa.ACC()
    # FUNÇÃO DE APLICAÇÃO #
    def APL(self):
        fn.cls()
        fn.ajustar()
        print('|' + f'{"Aplicação Poupança":^48}' + '|')
        fn.ajustar()
        print('Valor disponivel para aplicação: R$ ',self.CheckingBalance)
        vA = float(input('Insira um valor para aplicação: R$ '))
        self.CheckingBalance -= vA
        self.SavingsBalance += vA
        print('Sua aplicação foi feita com sucesso!')
        print('Saldo conta corrente: R$ ',self.CheckingBalance)
        print('Saldo conta poupança: R$ ',self.SavingsBalance)
        fn.espera(3)
        aa.ACC()

    # FUNÇÃO DE RESGATE #
    def RES(self):
        fn.cls()
        fn.ajustar()
        print('|' + f'{"Resgate Poupança":^48}' + '|')
        fn.ajustar()
        try:
            print('Valor disponivel para resgate: R$ ',self.SavingsBalance)
            vR = float(input('Insira um valor para resgate: R$ '))
            self.SavingsBalanceSLC -= vR
            print('Seu resgate foi efetuado com sucesso!')
            print('Saldo conta corrente: R$ ',self.CheckingBalance)
            print('Saldo conta poupança: R$ ',self.SavingsBalance)
            fn.espera(3)
            aa.ACC()
        except AttributeError:
            print('Erro')
            aa.ACC()

# FUNÇÃO DE "TELA" PRINCIPAL #
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
