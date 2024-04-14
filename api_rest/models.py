from django.db import models

class Profissional (models.Model):
    id_prof = models.AutoField (primary_key= True)
    nome_prof = models.CharField(max_length=100)
    profissao_prof = models.CharField(max_length=100)
    endereco_prof = models.CharField(max_length=200)
    telefone_prof = models.CharField(max_length=20)
    nomesocial_prof = models.CharField(max_length=100,  blank=True, null=True)
    
    def __str__(self):
        if self.nomesocial_prof: # essa condição vai verificar se o campo nome social foi preenchido. Se sim, irá retornar ele e não o nome. 
            return f'ID:{self.id_prof} | Nome: {self.nomesocial_prof} | Profissão: {self.profissao_prof}'
        else:      
            return f'ID:{self.id_prof} | Nome: {self.nome_prof} | Profissão: {self.profissao_prof}'
        
    
class Consulta (models.Model):
    id_consulta = models.AutoField (primary_key= True)
    data_consulta = models.DateTimeField()
    profissional_consulta = models.ForeignKey (Profissional, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Consulta com o Profissional: {self.profissional_consulta} no dia {self.data_consulta}'