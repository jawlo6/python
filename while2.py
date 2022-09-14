prompt = "\npowiedz mi coś o sobie a wyświetlę to na ekranie: "
prompt += "\nNapisz 'koniec' aby zakończyć działanie programu."
message = ""
while message != 'koniec':
    message = input( prompt )
    print( message )