Function Main
    Declare String Nama
    Declare Real NIM
    Declare Real UTS, UAS, RERATA
    
    Output "Masukan Nama :"
    Input Nama
    Output "Masukan NIM :"
    Input NIM
    Output "Masukan Nilai UTS :"
    Input UTS
    Output "masukan nilai UAS"
    Input UAS
    Assign Rerata = (UTS+UAS)/2
    Output "Nama anda :" &Nama
    Output "NIM anda :" &NIM
    Output "Nilai Rata-rata anda :" &Rerata
    If 100 >= Rerata and Rerata >= 80
        Output "Anda mendapatkan nilai A"
    False:
        If 80 > Rerata and Rerata >= 70
            Output "Anda mendapatkan nilai B"
        False:
            If 70 >= Rerata and Rerata >= 60
                Output "Anda mendapatkan nilai C"
            False:
                If 60 > Rerata and Rerata >= 40
                    Output "Anda mendapatkan nilai D"
                False:
                    Output "Anda mendapatkan nilai E"
                End
            End
        End
    End
End
