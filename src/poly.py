class Polynomial:
    def __init__(self, deg_to_coef):
        '''
        Chaves - Graus
        Valores - Coeficientes 
        '''
        self.deg_to_coef = deg_to_coef

    def derivative(self):
        '''
        Multiplicar o coeficiente pelo grau correspondente
        Diminuir uma unidade no grau do expoente

        Tratar do grau 0 especialmente

        Retorna um outro polinômio 
        '''
        der_deg_to_coef = {}

        for deg in self.deg_to_coef:
            new_deg = deg - 1 
            new_coef = self.deg_to_coef[deg] * deg 
            if deg > 0:
                der_deg_to_coef[new_deg] = new_coef
        
        return Polynomial(der_deg_to_coef)
    


