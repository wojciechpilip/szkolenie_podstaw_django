def operacje(request, operacja, liczba1, liczba2):
    if operacja == "add":
        liczba = liczba1 + liczba2
    elif operacja == "sub":
        liczba = liczba1 - liczba2
    elif operacja == "div":
        liczba = liczba1 / liczba2

    return HttpResponse(f"Wynik {liczba}")