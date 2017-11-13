from django.db import models
from django.contrib.gis.utils import GeoIP
class Setor (models.Model):
    descricao = models.CharField('descricao', max_length=100)
    chefedesetor =models.ForeignKey(Funcionario,related_name='setor_funcionariochefe',null=True,blank=False)

class Funcionario(models.Model):
    nome = models.CharField('nome', max_length=100)
    cpf = models.CharField('cpf', max_length=11)
    is_admin = models.BooleanField(blank=True)
    idsetor =models.ForeignKey(Setor,related_name='funcionario_setor',null=True,blank=False)


class HorariosPonto(models.Model):
    descricao = models.CharField('nome', max_length=100)
    pontoentrada1 = models.DateTimeField('Horario Entrada', null=True, blank=True)
    pontosaida1 = models.DateTimeField('Horario Entrada', null=True, blank=True)
    pontoentrada2 = models.DateTimeField('Horario Entrada', null=True, blank=True)
    pontosaida2 = models.DateTimeField('Horario Entrada', null=True, blank=True)
    cargahorario = models.CharField('Carga Horaria', max_length=11)

class Ponto(models.Model):
    idFuncionario = models.ForeignKey(Funcionario,related_name='Ponto_funcionario',null=True,blank=False)
    pontoentrada1 = models.DateTimeField('Horario Entrada', null=True, blank=True)
    pontosaida1 = models.DateTimeField('Horario Entrada', null=True, blank=True)
    pontoentrada2 = models.DateTimeField('Horario Entrada', null=True, blank=True)
    pontosaida2 = models.DateTimeField('Horario Entrada', null=True, blank=True)
    id_chefesetor = models.ForeignKey(Setor,related_name='ponto_chefe_setor',null=True,blank=False)
    ip = models.CharField('ip', max_length=100)