# Django Authentication Template Project

A template with a custom user model built on top of the [AbstractBaseUser](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#specifying-a-custom-user-model). Integrates [allauth](https://django-allauth.readthedocs.io/) and [DRF](https://www.django-rest-framework.org/) providing `UserViewset`, `UserSerializer`, permission classes, admin classes, and following endpoints:

```
api/users/
api/users/<int:pk>
```

*Plus endpoints provided by allauth. See [installation instructions](https://django-allauth.readthedocs.io/en/latest/installation.html).*

The `CustomUser` model has an *email* identifying field and, by default, does not accept a username as described in [Advanced Usage](https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-user-models).

## When to use it

- You need a custom user. Then, go to *users/models.py* and customize the `CustomUser` model to fit your needs.
- You want to authenticate your users via email instead of a username.
- You don't need a username at all.
- You are happy with allauth.

## Tests

- **Model**: `CustomUser`, `CustomuserManager`
- **Forms**: `CustomSignupForm`

