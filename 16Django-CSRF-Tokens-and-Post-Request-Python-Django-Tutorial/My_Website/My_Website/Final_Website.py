from django.shortcuts import render
from django.http import HttpResponse


def Webpage_Show(request):
    return render(request, "Main_Webpage.html")


def Contact_us(request):
    return render(request, "Contact_Us.html")


def About_Us(request):
    return render(request, "About_Us.html")


def Remove_Punctuations(text):
    punctuation_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
                        '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    analyzed_text = ""
    for charecter in text:
        for marks in punctuation_list:
            if charecter == marks:
                break
        else:
            analyzed_text += charecter
    return analyzed_text


def Word_Counter(text):
    Word_Counter = 1
    for char in text:
        if char == " ":
            Word_Counter += 1
        else:
            pass
    return Word_Counter


def Capitalize_First(text):
    analyzed_text = text.title()
    return analyzed_text


def Extra_Space_Remove(text):
    analyzed_text = ""
    index = 0
    for charecter in text:
        if text[index] == " " and text[index+1] == " ":
            pass
        else:
            analyzed_text += charecter
        index += 1
    print(index)
    return analyzed_text


def main(request):
    Word_Count = request.POST.get("Word_Counter")
    Capitalize_First_Charecter = request.POST.get("Capitalize_First_Charecter")
    Punctuations_Removal = request.POST.get("Remove Punctuations")
    User_Text = request.POST.get("Text_Entry")
    Remove_Extra_Spaces = request.POST.get("Remove Extra Spaces")
    if Capitalize_First_Charecter == "on":
        User_Text = Capitalize_First(User_Text)
    if Punctuations_Removal == "on":
        User_Text = Remove_Punctuations(User_Text)
    if Remove_Extra_Spaces == "on":
        User_Text = Extra_Space_Remove(User_Text)
    if Word_Count == "on":
        User_Text = f'''Your Given text is "{User_Text}" And Your Word Count Is {int(Word_Counter(User_Text))}'''

    parameters = {
        "Analyzed_Text": User_Text

    }
    return render(request, "Analyzed_Text.html", parameters)
