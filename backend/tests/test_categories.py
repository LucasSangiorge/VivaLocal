def test_criar_categoria(client):
    resposta = client.post("/categories/", json={
        "name": "Restaurante",
        "slug": "restaurante",
    })
    assert resposta.status_code == 200
    dado = resposta.json()
    assert dado["name"] == "Restaurante"
    assert dado["slug"] == "restaurante"
    assert "id" in dado


def test_listar_categorias(client):
    client.post("/categories/", json={"name": "Bar", "slug": "bar"})
    client.post("/categories/", json={"name": "Trilha", "slug": "trilha"})

    resposta = client.get("/categories/")
    assert resposta.status_code == 200
    dados = resposta.json()
    assert len(dados) == 2


def test_criar_categoria_sem_nome_falha(client):
    resposta = client.post("/categories/", json={"slug": "sem-nome"})
    assert resposta.status_code == 422