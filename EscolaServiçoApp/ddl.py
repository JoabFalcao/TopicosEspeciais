import sqlite3

conn = sqlite3.connect("ifpb.db")

cursor = conn.cursor()

cursor.execute("""
    create table tb_escola(
        id_escola integer auto_increment primary key,
        nome varchar(45),
        logradouro varchar(70),
        cidade varchar(45)
    );
""")

cursor.execute("""
    create table tb_aluno(
        id_aluno integer auto_increment primary key,
        nome varchar(45),
        matricula varchar(12),
        cpf varchar(11),
        nascimento date
    );
""")

cursor.execute("""
    create table tb_curso(
        id_curso integer  auto_incrementprimary key,
        nome varchar(45),
        turno varchar(10)
    );
""")

cursor.execute("""
    create table tb_turma(
        id_turma integer auto_increment primary key,
        nome varchar(45),
        curso varchar(45)
    );
""")

cursor.execute("""
    create table tb_disciplina(
        id_disciplina integer auto_increment primary key,
        nome varchar(45)
    );
""")

print ("Tabelas criadas com sucesso!")

cursor.close()
