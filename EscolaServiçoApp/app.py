from flask import Flask
from flask import request
from flask import jsonify
import logging

import sqlite3

app = Flask(__name__)

# Logging
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("escolaapp.log")
handler.setFormatter(formatter)
logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)

DATABASE_NAME = "ifpb.db"

# listar todas as escolas cadastradas
@app.route("/escolas", methods = ["GET"])
def getEscolas():
    logger.info("Listando escolas.")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_escola;
    """)
    escolas = []
    for linha in cursor.fetchall():
        escola = {
            "id" : linha[0],
            "nome" : linha[1],
            "logradouro" : linha[2],
            "cidade" : linha[3]
        }
        escolas.append(escola)
    conn.close()
    return jsonify(escolas)
    logger.info("Escolas listada com sucesso.")

# listar escola pelo id
@app.route("/escolas/<int:id>", methods = ["GET"])
def getEscolasId(id):
    logger.info("Listando escola.")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_escola where id_escola = ?;
    """, (id, ))

    linha = cursor.fetchone()
    escola = {
        "id" : linha[0],
        "nome" : linha[1],
        "logradouro" : linha[2],
        "cidade" : linha[3]
    }

    conn.close()
    return jsonify(escola)
    logger.info("Escola listada com sucesso.")

# cadastrar uma escola
@app.route("/escola", methods = ["POST"])
def setEscola():
    logger.info("Cadastrando escola.")
    escola = request.get_json()
    nome = escola["nome"]
    logradouro = escola["logradouro"]
    cidade = escola["cidade"]
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        insert into tb_escola(nome, logradouro, cidade)
        values(?,?,?);
    """, (nome, logradouro, cidade))
    conn.commit()
    conn.close()

    id = cursor.lastrowid
    escola["id"] = id

    return jsonify(escola)
    logger.info("Escola cadastrada com sucesso.")

# update esola
@app.route("/escola/<int:id>", methods=['PUT'])
def updateEscola(id):
    # Receber o JSON.
    escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']

    # Buscar a escola pelo "id".
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Executar a consulta de pesquisa.​​
    cursor.execute("""
        SELECT * FROM tb_escola WHERE id_escola ?;
    """, (id, ))

    data = cursor.fetchone()

    if data is not None:
        # Atualizar os dados caso a escola seja encontrada através do "id".
        cursor.execute("""
            UPDATE tb_escola
            SET nome=?, logradouro=?, cidade=?
            WHERE id_escola = ?;
        """, (nome, logradouro, cidade, id))
        conn.commit()
    else:
        logger.info("Inserindo.")
        # Inserir novo registro.
        cursor.execute("""
            INSERT INTO tb_escola(nome, logradouro, cidade)
            VALUES(?, ?, ?);
        """, (nome, logradouro, cidade))
        conn.commit()
        # Identificador do último registro inserido.
        id = cursor.lastrowid
        escola["id"] = id

    conn.close()

    #Retornar o JSON da escola atualizada.
    return jsonify(escola)


# listar alunos cadastrados
@app.route("/alunos", methods = ["GET"])
def getAlunos():
    logger.info("Listando alunos.")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_aluno;
    """)
    alunos = []
    for linha in cursor.fetchall():
        aluno = {
            "id" : linha[0],
            "nome" : linha[1],
            "matricula" : linha[2],
            "cpf" : linha[3],
            "nascimento" : linha[4]
        }
        alunos.append(aluno)
    conn.close()
    return jsonify(alunos)
    logger.info("Alunos listado com sucesso.")

# listar aluno pelo id
@app.route("/alunos/<int:id>", methods = ["GET"])
def getAlunosId(id):
    logger.info("Listando aluno.")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_aluno where id_aluno = ?;
    """, (id, ))

    linha = cursor.fetchone()
    aluno = {
        "id" : linha[0],
        "nome" : linha[1],
        "matricula" : linha[2],
        "cpf" : linha[3],
        "nascimento" : linha[4]
    }

    conn.close()
    return jsonify(aluno)
    logger.info("Aluno listado com sucesso.")

# cadastrar um aluno
@app.route("/aluno", methods = ["POST"])
def setAluno():
    logger.info("Cadastrando aluno..")
    aluno = request.get_json()
    nome = aluno["nome"]
    matricula = aluno["matricula"]
    cpf = aluno["cpf"]
    nascimento = aluno["nascimento"]
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_aluno(nome, matricula, cpf, nascimento)
        values(?,?,?,?);
    """, (nome, matricula, cpf, nascimento))
    conn.commit()
    conn.close()
    id = cursor.lastrowid
    aluno["id"] = id
    return jsonify(aluno)
    logger.info("Aluno Cadastrado com sucesso.")

# update aluno
@app.route("/aluno/<int:id>", methods=['PUT'])
def updateAluno(id):
    # Receber o JSON.
    aluno = request.get_json()
    nome = aluno['nome']
    matricula = aluno['matricula']
    cpf = aluno['cpf']
    nascimento = aluno['nascimento']

    # Buscar o aluno pelo "id".
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Executar a consulta de pesquisa.​​
    cursor.execute("""
        SELECT * FROM tb_aluno WHERE id_aluno = ?;
    """, (id, ))

    data = cursor.fetchone()

    if data is not None:
        # Atualizar os dados caso o aluno seja encontrado através do "id".
        cursor.execute("""
            UPDATE tb_aluno
            SET nome=?, matricula=?, cpf=?, nascimento=?
            WHERE id_aluno = ?;
        """, (nome, matricula, cpf, nascimento, id))
        conn.commit()
    else:
        logger.info("Inserindo")
        # Inserir novo registro.
        cursor.execute("""
            INSERT INTO tb_aluno(nome, matricula, cpf, nascimento)
            VALUES(?, ?, ?, ?);
        """, (nome, matricula, cpf, nascimento))
        conn.commit()
        # Identificador do último registro inserido.
        id = cursor.lastrowid
        aluno["id"] = id

    conn.close()

    #Retornar o JSON do aluno atualizado.
    return jsonify(aluno)


# listar todos os cursos
@app.route("/cursos", methods = ["GET"])
def getCursos():
    logger.info("Listando cursos.")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_curso;
    """)
    cursos = []
    for linha in cursor.fetchall():
        curso = {
            "id" : linha[0],
            "nome" : linha[1],
            "turno" : linha[2]
        }
        cursos.append(curso)
    conn.close()
    return jsonify(cursos)
    logger.info("Cursos listados com sucesso.")

# listar curso pelo id
@app.route("/cursos/<int:id>", methods = ["GET"])
def getCursosId(id):
    logger.info("Listando curso.")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_curso where id_curso = ?;
    """, (id, ))
    linha = cursor.fetchone()
    curso = {
        "id" : linha[0],
        "nome" : linha[1],
        "turno" : linha[2]
    }
    conn.close()
    return jsonify(curso)
    logger.info("Curso listado com sucesso.")

# cadastrar um curso
@app.route("/curso", methods = ["POST"])
def setCurso():
    logger.info("Cadastrando curso.")
    curso = request.get_json()
    nome = curso["nome"]
    turno = curso["turno"]
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_curso(nome, turno)
        values(?,?);
    """, (nome, turno))
    conn.commit()
    conn.close()
    id = cursor.lastrowid
    curso["id"] = id
    return jsonify(curso)
    logger.info("Curso cadastrado com sucesso.")

# update curso
@app.route("/curso/<int:id>", methods=['PUT'])
def updateCurso(id):
    # Receber o JSON.
    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']

    # Buscar o curso pelo "id".
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Executar a consulta de pesquisa.​​
    cursor.execute("""
        SELECT * FROM tb_curso WHERE id_curso = ?;
    """, (id, ))

    data = cursor.fetchone()

    if data is not None:
        # Atualizar os dados caso o curso seja encontrado através do "id".
        cursor.execute("""
            UPDATE tb_curso
            SET nome=?, turno=?
            WHERE id_curso = ?;
        """, (nome, turno, id))
        conn.commit()
    else:
        logger.info("Inserindo")
        # Inserir novo registro.
        cursor.execute("""
            INSERT INTO tb_curso(nome, turno)
            VALUES(?, ?);
        """, (nome, turno))
        conn.commit()
        # Identificador do último registro inserido.
        id = cursor.lastrowid
        aluno["id"] = id

    conn.close()

    #Retornar o JSON do curso atualizado.
    return jsonify(curso)

# listar todas as turmas
@app.route("/turmas", methods = ["GET"])
def getTurmas():
    logger.info("Listando turmas.")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_turma;
    """)
    turmas = []
    for linha in cursor.fetchall():
        turma = {
            "id" : linha[0],
            "nome" : linha[1],
            "curso" : linha[2]
        }
        turmas.append(turma)
    conn.close()
    return jsonify(turmas)
    logger.info("Turmas listadas com sucesso.")

# listar turma pelo id
@app.route("/turmas/<int:id>", methods = ["GET"])
def getTurmasId(id):
    logger.info("Listando turma.")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_turma where id_turma = ?;
    """, (id, ))
    linha = cursor.fetchone()
    turma = {
        "id" : linha[0],
        "nome" : linha[1],
        "curso" : linha[2]
    }
    conn.close()
    return jsonify(turma)
    logger.info("Turma listada com sucesso.")

# cadastrar uma turma
@app.route("/turma", methods = ["POST"])
def setTurma():
    logger.info("Cadastrando turma.")
    turma = request.get_json()
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    nome = turma["nome"]
    curso = turma["curso"]
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_turma(nome, curso)
        values(?,?);
    """, (nome, curso))
    conn.commit()
    conn.close()

    id = cursor.lastrowid
    turma["id"] = id

    return jsonify(turma)
    logger.info("Turma cadastrada com sucesso.")

# update turma
@app.route("/turma/<int:id>", methods=['PUT'])
def updateTurma(id):
    # Receber o JSON.
    turma = request.get_json()
    nome = curso['nome']
    curso = curso['curso']

    # Buscar a turma pelo "id".
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Executar a consulta de pesquisa.​​
    cursor.execute("""
        SELECT * FROM tb_turma WHERE id_turma = ?;
    """, (id, ))

    data = cursor.fetchone()

    if data is not None:
        # Atualizar os dados caso a turma seja encontrada através do "id".
        cursor.execute("""
            UPDATE tb_turma
            SET nome=?, curso=?
            WHERE id_turma = ?;
        """, (nome, curso, id))
        conn.commit()
    else:
        logger.info("Inserindo")
        # Inserir novo registro.
        cursor.execute("""
            INSERT INTO tb_turma(nome, curso)
            VALUES(?, ?);
        """, (nome, curso))
        conn.commit()
        # Identificador do último registro inserido.
        id = cursor.lastrowid
        aluno["id"] = id

    conn.close()

    #Retornar o JSON da turma atualizada.
    return jsonify(turma)

# listar todas as disciplinas
@app.route("/disciplinas", methods = ["GET"])
def getDisciplinas():
    logger.info("Listando disciplinas.")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_disciplina;
    """)
    disciplinas = []
    for linha in cursor.fetchall():
        disciplina = {
            "id" : linha[0],
            "nome" : linha[1]
        }
        disciplinas.append(disciplina)
    conn.close()
    return jsonify(disciplinas)
    logger.info("Disciplinas listadas com sucesso.")

# listar disciplina pelo id
@app.route("/disciplinas/<int:id>", methods = ["GET"])
def getDisciplinasId(id):
    logger.info("Listando disciplina.")
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_disciplina where id_disciplina = ?;
    """, (id, ))

    linha = cursor.fetchone()
    disciplina = {
        "id" : linha[0],
        "nome" : linha[1]
    }
    conn.close()
    return jsonify(disciplina)
    logger.info("Disciplina listada com sucesso.")

# cadastrar uma disciplina
@app.route("/disciplina", methods = ["POST"])
def setDisciplina():
    logger.info("Cadastrando disciplina.")
    disciplina = request.get_json()
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    nome = disciplina["nome"]
    cursor.execute("""
        insert into tb_disciplina(nome)
        values(?);
    """, (nome, ))
    conn.commit()
    conn.close()
    id = cursor.lastrowid
    disciplina["id"] = id
    return jsonify(disciplina)
    logger.info("Disciplina cadastrada com sucesso.")

# update disciplina
@app.route("/disciplina/<int:id>", methods=['PUT'])
def updateDisciplina(id):
    # Receber o JSON.
    disciplina = request.get_json()
    nome = disciplina['nome']

    # Buscar a turma pelo "id".
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Executar a consulta de pesquisa.​​
    cursor.execute("""
        SELECT * FROM tb_disciplina WHERE id_disciplina = ?;
    """, (id, ))

    data = cursor.fetchone()

    if data is not None:
        # Atualizar os dados caso a disciplina seja encontrada através do "id".
        cursor.execute("""
            UPDATE tb_disciplina
            SET nome=?
            WHERE id_disciplina = ?;
        """, (nome, id))
        conn.commit()
    else:
        logger.info("Inserindo")
        # Inserir novo registro.
        cursor.execute("""
            INSERT INTO tb_disciplina(nome)
            VALUES(?, ?);
        """, (nome))
        conn.commit()
        # Identificador do último registro inserido.
        id = cursor.lastrowid
        aluno["id"] = id

    conn.close()

    #Retornar o JSON da disciplina atualizada.
    return jsonify(turma)

def dict_factory(linha, cursor):
    dicionario = {}
    for idx, col in enumerate(cursor.description):
        dicionario[col[0]] = linha[idx]
    return dicionarionario

# Mensagem de erro para recurso não encontrado.
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if(__name__ == '__main__'):
app.run(host='0.0.0.0', debug=True, use_reloader=True)
