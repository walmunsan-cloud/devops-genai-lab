from app import formatar_recibo

def test_recibo():
    assert formatar_recibo(25.5) == "Total: R$ 25.50"
