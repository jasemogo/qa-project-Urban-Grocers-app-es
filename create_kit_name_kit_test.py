import sender_stand_request
import data


# function that change the values of name in the kit body
def get_kit_body(name):
    # Copia el cuerpo del diccionario de la solicitud
    current_body = data.kit_body.copy()
    # Cambia el valor name al del introducido en el parametro
    current_body["name"] = name
    return current_body

def get_new_user_token():
    # crear ususario
    user_response = sender_stand_request.post_new_user(data.user_body)

    # Verficar que usuario se creo y que el authToken no esta vacio
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    #resultado de la solicitud de recepcion de datos de la tabla "user_model"
    users_table_response = sender_stand_request.get_users_table()
    #string del usuario que debe estar en al respuesta
    str_user = data.user_body["firstName"] + "," + data.user_body["phone"] + "," \
               + data.user_body["address"] + ",,," + user_response.json()["authToken"]
    #comprobar si el usuario eiste y no hay duplicados en la tabla
    assert users_table_response.text.count(str_user) == 1

    return user_response.json()["authToken"]


# funcion de prueba positiva en el que regresa 201
def positive_assert(kit_body_name):
    # obtiene el token del nuevo usuario creado
    new_user_token = get_new_user_token()
    # obtiene y copia el headers de data
    kit_headers = data.headers.copy()
    # Agrega al header el parametro de Authorization y el token del usuario
    kit_headers["Authorization"] = "Bearer " + new_user_token

    # Obtiene el cuerpo de la solicitud con el nombre indicado en el parametro
    kit_body = get_kit_body(kit_body_name)

    kit_response = sender_stand_request.post_new_kit(kit_body, kit_headers)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body_name):
    # obtiene el token del nuevo usuario creado
    new_user_token = get_new_user_token()
    # obtiene y copia el headers de data
    kit_headers = data.headers.copy()
    # Agrega al header el parametro de Authorization y el token del usuario
    kit_headers["Authorization"] = "Bearer " + new_user_token

    kit_body = get_kit_body(kit_body_name)

    kit_response = sender_stand_request.post_new_kit(kit_body, kit_headers)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

def negative_assert_code_400_no_name(kit_body):
    # obtiene el token del nuevo usuario creado
    new_user_token = get_new_user_token()
    # obtiene y copia el headers de data
    kit_headers = data.headers.copy()
    # Agrega al header el parametro de Authorization y el token del usuario
    kit_headers["Authorization"] = "Bearer " + new_user_token

    kit_response = sender_stand_request.post_new_kit(kit_body, kit_headers)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

# Prueba 1 Kit Creado con exito. Parametro name contiene 1 caracter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

# Prueba 2 Kit Creado con exito. Parametro name contiene 511 caracteres
def test_create_kit_511_letter_in_name_get_success_response():
    # Asignar el nombre a 512 caracteres
    name = "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabc" \
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"

    positive_assert(name)

# Prueba 3 Kit Error. Parametro name contiene 0 caracter
def test_create_kit_no_letter_in_name_get_error_response():
    negative_assert_code_400("")

# Prueba 4 Kit Error. Parametro name contiene 512 caracter
def test_create_kit_512_letter_in_name_get_error_response():
    # Asignar el nombre a 512 caracteres
    name = "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabc" \
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"

    negative_assert_code_400(name)

# Prueba 5 Kit Creado con exito. Parametro name contiene caracteres especiales
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert('"№%@",')

# Prueba 6 Kit Creado con exito. Parametro name contiene espacio
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" A Aaa ")

# Prueba 7 Kit Creado con exito. Parametro name contiene numeros
def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")

# Prueba 8 Kit Error. Parametro name no se pasa en la solicitud
def test_create_kit_name_parameter_not_in_body_get_error_response():
    # Copia el cuerpo de solicitud de data.py
    kit_body = data.kit_body.copy()
    # Remueve el parametro "name" del cuerpo de la solicitud
    kit_body.pop("name")

    negative_assert_code_400_no_name(kit_body)


# Prueba 9 Kit Error. Parametro name tipo diferente (numero)
def test_create_kit_has_number_type_in_parameter_name_get_error_response():
    negative_assert_code_400(123)
