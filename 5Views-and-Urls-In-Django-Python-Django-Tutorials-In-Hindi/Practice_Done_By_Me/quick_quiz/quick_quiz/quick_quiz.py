from django import http


def Function_To_Read_Text_From_A_Document(Defaul_Argument):
    with open("quick_quiz\\Text_Document.txt") as read:
        hello = read.readline()

        return http.HttpResponse(hello)
