#Логин 

Вид заголовка для доступа ко всем остальным частям сайта, гд


````python
# POST
{
    "login": "str",
    "password": "str"
}

# Response
{
    "detail": "str",
    "token": "str"
}
# status 200

# Если не 200 -> что-то не так

````

# Change password POST domen.com/api/auth/change-password/

```python
{
# POST
{
    "otp": "str (0000)",
    "password" "str (new password)",
}

# Response 200
{}

# Во всех остальных случаях не 200
```