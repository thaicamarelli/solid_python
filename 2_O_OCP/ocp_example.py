# Principio aberto fechado

class Programer:
    def make(self):
        print("Programmer creating code")

class Seller:
    def make(self):
        print("Seller selling the product")

class Company:
    def do_work(self,worker:any) -> None:
        # Posso ter uma logica antes do make
        worker.make()

programmer = Programer()
company = Company()
seller = Seller()
company.do_work(programmer)
company.do_work(seller)

# Errado
# class Company:
#     def do_work(self,worker:int) -> None:
#         if worker == 1:
#             print('Programmer creating code')
#         elif worker == 2:
#             print('Seller selling the product')
#         elif worker == 3:
#             print('Human Resources hiring new devs')
#         # se eu precisar colocar mais uma condição vou precisar alterar
#         elif worker == 4:
#             print('Frontend raising bigs for production')
#         else:
#             print('Error, no worker!')

# company = Company()
# company.do_work(4)