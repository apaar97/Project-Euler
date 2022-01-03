#   Number letter counts

'''
    Sum of letter counts for numbers 1-1000

    Numbers 1-9 :
        one     =   3
        two     =   3
        three   =   5
        four    =   4
        five    =   4
        six     =   3
        seven   =   5
        eight   =   5
        nine    =   4
                            =   36
    Numbers 11-19 :
        ten         =   3
        eleven      =   6
        twelve      =   6
        thirteen    =   8
        fourteen    =   8
        fifteen     =   7
        sixteen     =   7
        seventeen   =   9
        eighteen    =   8
        nineteen    =   8
                            =   70
    Numbers 20-99 :
        ( thirty nine )
        Prefix :
        twenty      =   6
        thirty      =   6
        forty       =   5
        fifty       =   5
        sixty       =   5
        seventy     =   7
        eighty      =   6
        ninety      =   6
                            =   46
                                        =   10*46 + 8*36 =  748
            =>  Total 1-99  =  748 + 70 + 36
                            =  854

    Numbers 100-999 :
        ( three hundred and ninety nine)
        hundred     =   7
        and         =   3
                        =   (36 + 9*7)  +   (99*(36 + 9*(7+3)) + 9*854)
                        =   20259
    Number : 1000
        one thousand    =   3 + 8
                        =   11

    TOTAL   =   854 + 20259 + 11
            =   21124
'''
