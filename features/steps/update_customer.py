from behave import when, then


@when(u'"{name}" with ID "{customerId}" changes their surname to "{new_name}"')
def update_surname(context, customer_id, new_name):
        response = context.web_client.put(
            f'/customers/{customer_id}',
            json={'new_name': new_name})

        assert response.status_code == 200, response.status_code


@then(u'Account "{customer_id}" now has name "{name}"')
def check_surname(context, customer_id, name):
    (first_name, surname) = name.split(' ', 2)
    response = context.web_client.get(f'/customers/{customer_id}')
    customer = response.get_json()
    assert customer['surname'] == surname
