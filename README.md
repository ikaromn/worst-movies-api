# Worst Movies Api

API Responsible for evaluating films nominated as the worst movie at the Golden Raspberry Awards

## Requirements

Install [python](https://www.python.org/downloads/)

## Installation

```
pip install poetry
poetry install
```

## Run API
```
python run.py
```

## Endpoint
`GET http://127.0.0.1/prize-ranges/`

Response:
```
{
    "min": [
        {
            "producer": "Producer 1",
            "interval": 1,
            "previousWin": 2008,
            "followingWin": 2009
        }
        ],
    "max": [
        {
            "producer": "Producer 1",
            "interval": 99,
            "previousWin": 1900,
            "followingWin": 1999
        }
    ]
}
```


## Tests

```
pytest .
```