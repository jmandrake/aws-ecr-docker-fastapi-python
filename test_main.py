from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Wikipedia API end point. Usage: /search or /wiki or /phrase"
    }


def test_get_phrase():
    response = client.get("/phrase/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "barack hussein obama ii",
            "bə-rahk hoo-sayn oh-bah-mə",
            "august",
            "american politician",
            "44th president",
        ]
    }


def test_get_wiki():
    response = client.get("/wiki/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "result": "Barack Hussein Obama II ( (listen) bə-RAHK hoo-SAYN oh-BAH-mə; born August 4, 1961) is an American politician who served as the 44th president of the United States from 2009 to 2017."
    }


def test_get_search():
    response = client.get("/search/Barack Obama")
    assert response.status_code == 200
    response_dict = dict(response.json())
    assert "Barack Obama" in response_dict["result"]
    # assert response.json() == {'result': ['Barack Obama', 'Barack Obama Sr.', 'Family of Barack Obama', 'Presidency of Barack Obama', 'Early life and career of Barack Obama', 'First inauguration of Barack Obama', 'Cabinet of Barack Obama', 'Barack Obama citizenship conspiracy theories', 'Speeches of Barack Obama', 'Barack Obama 2008 presidential campaign']}
