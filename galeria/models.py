
from django.db import models


class Abertura(models.Model):
    id_abertura = models.AutoField(primary_key=True)
    nome = models.TextField(blank=False, null=True)  # This field type is a guess.
    movimento = models.TextField(blank=False, null=True)  # This field type is a guess.
    descricao = models.TextField(blank=False, null=True)

    class Meta:
        managed = False
        db_table = 'abertura'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Jogador(models.Model):
    id_jogador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False, null=True)
    data_nascimento = models.DateField(blank=False, null=True)
    pais = models.CharField(max_length=25, blank=False, null=True)
    elo = models.TextField(blank=False, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'jogador'


class Movimento(models.Model):
    id_movimento = models.AutoField(primary_key=True)
    id_partida = models.ForeignKey('Partida', models.DO_NOTHING, db_column='id_partida', blank=True, null=True)
    id_jogador = models.ForeignKey(Jogador, models.DO_NOTHING, db_column='id_jogador', blank=True, null=True)
    numero_jogada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimento'


class Partida(models.Model):
    id_partida = models.AutoField(primary_key=True)
    id_jogador_brancas = models.ForeignKey(Jogador, models.DO_NOTHING, db_column='id_jogador_brancas', blank=True, null=True)
    id_jogador_pretas = models.ForeignKey(Jogador, models.DO_NOTHING, db_column='id_jogador_pretas', related_name='partida_id_jogador_pretas_set', blank=True, null=True)
    id_abertura = models.ForeignKey(Abertura, models.DO_NOTHING, db_column='id_abertura', blank=True, null=True)
    data_partida = models.DateField(blank=True, null=True)
    duracao = models.DateTimeField(blank=True, null=True)
    resultado = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partida'


class Torneio(models.Model):
    nome_torneio = models.TextField(blank=True, null=True)  # This field type is a guess.
    localizacao = models.TextField(blank=True, null=True)  # This field type is a guess.
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    id_torneio = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'torneio'
