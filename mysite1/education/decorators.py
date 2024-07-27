from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def login_required1(function=None, redirect_field_name='next', login_url=None):
    actual_decorators = login_required(
        function,
        redirect_field_name=redirect_field_name,
        login_url=login_url
    )
    if function:
        return actual_decorators

    else:
        return actual_decorators
