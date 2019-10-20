
## Full info GET domen.com/api/info/full/

Получение сразу всей информации

```python
{
    "balance": {
        "money": int,
        "minutes": int,
        "sms": int,
        "traffic": int
    },
    "base": {
        "number": "str",
        "full_name": "str",
        "first_name": "str",
        "last_name": "str",
        "middle_name": "str"
    },
    "tariff": {
        "name": "str",
        "price": int,
        "description": "str",
        "minutes": int,
        "sms": int,
        "traffic": int
    }
}
```

## Full info GET domen.com/api/info/base/

```python
{
        "number": "str",
        "full_name": "str",
        "first_name": "str",
        "last_name": "str",
        "middle_name": "str"
}
```