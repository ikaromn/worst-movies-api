from pytest import fixture


@fixture
def prize_ranges_result():
    return {
        "max":[
            {
                "followingWin":2015,
                "interval":13,
                "previousWin":2002,
                "producer":"Matthew Vaughn"
            },
            {
                "followingWin":1994,
                "interval":9,
                "previousWin":1985,
                "producer":"Buzz Feitshans"
            },
            {
                "followingWin":1990,
                "interval":6,
                "previousWin":1984,
                "producer":"Bo Derek"
            },
            {
                "followingWin":1991,
                "interval":1,
                "previousWin":1990,
                "producer":"Joel Silver"
            }
        ],
        "min":[
            {
                "followingWin":1991,
                "interval":1,
                "previousWin":1990,
                "producer":"Joel Silver"
            },
            {
                "followingWin":1990,
                "interval":6,
                "previousWin":1984,
                "producer":"Bo Derek"
            },
            {
                "followingWin":1994,
                "interval":9,
                "previousWin":1985,
                "producer":"Buzz Feitshans"
            },
            {
                "followingWin":2015,
                "interval":13,
                "previousWin":2002,
                "producer":"Matthew Vaughn"
            }
        ]
    }