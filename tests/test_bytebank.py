from Codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    @mark.calculo_idade
    def test_quando_idade_recebe_13_03_200_deve_retornar_22(self):
        # Given - Contexto
        entrada = '13/03/2000'
        esperado = 23
        # When - Ação
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()
        
        assert resultado == esperado #then - desfecho  
    
    @mark.retornar_sobrenome    
    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_apenas_caravalho(self):
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'
        
        lucas = Funcionario(entrada, '11/11/2002', 1000)
        resultado = lucas.sobrenome()
        
        assert resultado == esperado
    
    @mark.descrescimo_salario
    def test_decrescimo_salario_quando_recebe_100000_deve_retornar_90000(self):
        entrada = 100000
        entrada_nome = 'Paulo Bragança'
        resultado = 90000
        
        funcionario_teste = Funcionario(entrada_nome, "11/11/1111", entrada)
        funcionario_teste.descrescimo_salario()
        resposta = funcionario_teste.salario
        
        assert  resposta == resultado
      
    @mark.calcular_bonus  
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        resultado = 100
        
        funcionario_teste = Funcionario("Paulo", "11/11/1111", entrada)
        resposta  = funcionario_teste.calcular_bonus()
        
        assert  resposta == resultado
        
    @mark.calcular_bonus    
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000
            
            funcionario_teste = Funcionario("Paulo", "11/11/1111", entrada)
            resposta  = funcionario_teste.calcular_bonus()
            
            assert  resposta
