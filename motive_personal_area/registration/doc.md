# Логин POST domen.com/api/auth/login/

Вид заголовка для доступа ко всем остальным частям сайта, где нужна аутентификация
Authorizations | token <user_token>


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

# OTP логин POST domen.com/api/auth/otp-login/

````python
# POST
{
    "login": "str",
    "otp": "str (0000)"
}

# Response
{
    "detail": "str",
    "token": "str"
}
# status 200


# Если отп не валиден. 
{
    "detail": "Incorrect otp"
}
# status 400
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

