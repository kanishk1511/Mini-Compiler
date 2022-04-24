import fun

while True:
    text = input('fun > ')
    result, error = fun.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
