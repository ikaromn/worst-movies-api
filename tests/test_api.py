from app import create_app


def test_prize_ranges(prize_ranges_result):
    """
    Test the endpoint that calculates the interval between 2 prizes won by a producer
    """
    app = create_app().test_client()
    rv = app.get("/prize-ranges/")
    result = rv.get_json()
    assert prize_ranges_result == result
