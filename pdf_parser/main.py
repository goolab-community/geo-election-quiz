import models
import PyPDF2
import re
import json


pdf_file = "./mokhelistestebi2024.pdf"


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i, page in enumerate(reader.pages):
            # Skip address pages
            if i > 5:
                text += page.extract_text()
    return text


def specal_cases(qurrent_text, previous_text):
    if qurrent_text.count("\uf0a7") == 4 and qurrent_text.startswith("\uf0a7"):
        return True
    if qurrent_text.count("\uf0a7") == 4 and qurrent_text.strip().startswith("\uf0a7"):
        return True
    if qurrent_text.count("\uf0a7") < 4 and not qurrent_text.strip().split(".")[0].isdigit():
        return True
    return False


def separ_funct(items, item, separator):
    tests = item.split(separator)
    items.append(tests[0])
    items.append(separator + tests[1])


def split_text(text):
    items = []
    for i, t in enumerate(text.split("\n \n")):
        matches = re.findall(r'\d+\.', t.strip())
        matches_answer = re.findall(r"\(\b\d+\.", t.strip())
        if 870 < i < 885:
            print("+++++++++++++++++++++++")
            print(i)
            print(t)
            print("Matched", matches)
            print("Matched answer", matches_answer)
            print(i > 0, (not (matches and matches[0].strip(".").isdigit())), "or",
                  (matches_answer and (not (matches and len(matches) > 1))), t.count("\uf0a7") < 4)
            print(i > 0, t.count("\uf0a7") == 4, t.strip().startswith("\uf0a7"))
            print("+++++++++++++++++++++++")
        if i == 128:
            tests = t.split("53")
            items.append(tests[0])
            items.append("53" + tests[1])
        elif i == 174:
            tests = t.split("\nსაოლქო")
            items.append(tests[0])
            items.append("\nსაოლქო" + tests[1])
        elif i == 198:
            tests = t.split("საარჩევნო  უბნები  (მუხლი  23)")
            items.append(tests[0])
            items.append("საარჩევნო  უბნები  (მუხლი  23)" + tests[1])
        elif i == 208:
            separ = "საუბნო  საარჩევნო  კომისიის  წევრთა  არჩევა /დანიშვნა  (მუხლი  25)"
            tests = t.split(separ)
            items.append(tests[0])
            items.append(separ + tests[1])
        elif i == 211:
            separ = "საუბნო  საარჩევნო  კომისიის  ხელმძღვანელ  პირთა  არჩევა  (მუხლი  251)"
            separ_funct(items, t, separ)
        elif i == 312:
            separ_funct(items, t, "მხარდამჭერთა  სიები  (მუხლი  37)")
        elif i == 327:
            separ_funct(items, t, "ადგილობრივი  და საერთაშორისო  დამკვირვებლები  (მუხლი  39)")
        elif i == 333:
            separ_funct(items, t, "დამკვირვებელ  ორგანიზაციათა  რეგისტრაცია  (მუხლი  40)")
        elif i == 341:
            separ_funct(items, t, "დამკვირვებლის  უფლებები  (მუხლი  41)")
        elif i == 382:
            separ_funct(items, t, "არჩევნებისათვის /რეფერენდუმისათვის  საჭირო  ფულადი  სახსრები  (მუხლი  53)")
        elif i == 385:
            separ_funct(items, t, "კენჭისყრის  შენობის  მოწყობა  (მუხლი  58)")
        elif i == 400:
            separ_funct(items, t, "კენჭისყრის  დრო  და ადგილი  (მუხლი  60)")
        elif i == 405:
            separ_funct(items, t, "საარჩევნო  უბნის  გახსნა (მუხლი  61)")
        elif i == 656:
            sep1 = "პასიური  საარჩევნო  უფლება  (მუხლი  96)"
            sep2 = "საქართველოს  პრეზიდენტობის  კანდიდატის  წარდგენის  უფლება  (მუხლი  97)"
            tests = t.split(sep1)
            items.append(tests[0])
            tests2 = tests[1].split(sep2)
            items.append(sep1 + tests2[0])
            items.append(sep2 + tests2[1])
        elif i == 665:
            separ_funct(items, t, "საარჩევნო  კოლეგია  (მუხლი  1031)")
        elif i == 680:
            separ_funct(items, t, "საქართველოს  პარლამენტის  არჩევნების  დანიშვნა  (მუხლი  108)")
        elif i == 449:
            separ_funct(items, t, "345. ")
        elif i == 701:
            separ_funct(items, t, "პარტიული  სიის  საარჩევნო  რეგისტრაცია  (მუხლი  117)")
        elif i == 711:
            sep1 = "ხმების  დათვლა  საუბნო  საარჩევნო  კომისიაში  (მუხლი  123)"
            sep2 = "კენჭისყრის  შედეგების  შეჯამება  საოლქო  საარჩევნო  კომისიაში  (მუხლი  124)"
            tests = t.split(sep1)
            items.append(tests[0])
            tests2 = tests[1].split(sep2)
            items.append(sep1 + tests2[0])
            items.append(sep2 + tests2[1])
        elif i == 741:
            sep1 = "საარჩევნო  ოლქები  (მუხლი  137)"
            sep2 = "საარჩევნო  სისტემა  (მუხლი  138)"
            tests = t.split(sep1)
            items.append(tests[0])
            tests2 = tests[1].split(sep2)
            items.append(sep1 + tests2[0])
            items.append(sep2 + tests2[1])
        elif i == 746:
            separ_funct(items, t, "საკრებულოს  არჩევნებში  მონაწილეობის  უფლება  და მაჟორიტარ  კანდიდატთა  წარდგენა")
        elif i == 754:
            separ_funct(items, t, "მაჟორიტარული  საარჩევნო  სისტემის  საფუძველზე  ჩატარებული  საკრებულოს  არჩევნების")
        elif i == 732:
            items.append(t.strip())
        elif i == 756:
            splited = t.split("საკრებულოს  არჩევნების  შედეგების  შეჯამება  საოლქო  საარჩევნო  კომისიაში  (მუხლი  150)")
            items[-1] += "\n" + splited[0].strip()
            items.append("საკრებულოს  არჩევნების  შედეგების  შეჯამება  საოლქო  საარჩევნო  კომისიაში  (მუხლი  150)" +
                         splited[1])
        elif i == 846:
            splited = t.split("28. ელექტრონული  საშუალებების  გამოყენებით  კენჭისყრის  ჩატარებისას , საარჩევნო  ბიულეტენის")
            items[-1] += "\n" + splited[0].strip()
            items.append("28. ელექტრონული  საშუალებების  გამოყენებით  კენჭისყრის  ჩატარებისას , საარჩევნო  ბიულეტენის"+
                         splited[1])
        elif i == 783:
            separ_funct(items, t, "რეფერენდუმის  დანიშვნა  (მუხლი  174)")
        elif i == 796:
            separ_funct(items, t, "664. რეფერენდუმი  შეიძლება  მოეწყოს :")
        elif i == 806:
            separ_funct(items, t, "რეფერენდუმის  მოწყობის  თაობაზე  მოთხოვნის  გამოთხოვა  (მუხლი  180)")
        elif i == 880:
            items[-1] += "\n" + t.strip()
        elif i == 733:
            items[-1] += "\n" + t.strip()
        elif i == 578:
            items[-1] += "\n" + t.strip()
        elif i == 525:
            items[-1] += "\n" + t.strip()
        elif i == 408:
            items[-1] += "\n" + t.strip()
        elif i == 413:
            items[-1] += "\n" + t.strip()
        elif i == 291:
            items[-1] += "\n" + t.strip()
        elif i == 143:
            items[-1] += "\n" + t.strip()
        elif (i > 0 and
                ((not (matches and matches[0].strip(".").isdigit())) or
                    (matches_answer and (not (matches and len(matches) > 1)))) and
                t.count("\uf0a7") < 4):
            items[-1] += "\n" + t.strip()
        elif (i > 0 and t.count("\uf0a7") == 4 and t.strip().startswith("\uf0a7")) and i != 66:
            items[-1] += "\n" + t.strip()
        else:
            if len(t.strip()) > 10:
                items.append(t.strip())
    return items


def differentiate_headers_and_versions(text):
    items = []
    for i, t in enumerate(split_text(text)):
        header = t.split("\uf0a7")[0]
        if len(header.strip()) > 7:
            items.append((header, t.split(header)[1]))
    return items


def separate_questions(text):
    items = differentiate_headers_and_versions(text)
    questions = []
    for i, t in enumerate(items):
        header = t[0]
        qstr = t[1]
        questions.append([i, header, [n.strip() for n in qstr.split("\uf0a7")[1:]]])
    return questions


# ----------------------------------------------------------------
def find_sections(text):
    items = separate_questions(text)
    tests = []
    for i, header, questions in items:
        result = re.split(r'\n\d+\.', header)
        header = result[0]
        section = result[1] if len(result) > 1 else ""
        tests.append([i, section, header, questions])
    return tests


def mark_correct_answers(text):
    # items = find_sections(text)
    items = separate_questions(text)
    items1 = []
    pattern = r'\(\s*\d+.*[/n]?.*\)'  # r'\(.*?\)'
    for item in items:
        for i, n in enumerate(item[2]):
            if item[0] == 256:
                pattern = r'\(.*\s*\d+.*[/n]?.*\)'
            match = re.findall(pattern, n)
            if item[0] == 196 and i == 1:
                item.append(i)
                item[2][i] = n.strip("(27.3 , \n62.3)")
                item.append("(27.3 , \n62.3)")
            elif item[0] == 631 and i == 2:
                item.append(i)
                item[2][i] = n.split("117.4")[0]
                item.append("117.4")
            elif match:
                item.append(i)
                item[2][i] = re.sub(pattern, '', n).strip()
                item.append(match[0].strip())
        items1.append(item)
    return items1


def extract_tests(text):
    tests = []

    for params in mark_correct_answers(text):
        for p in params:
            print(p)
        print()
        print()
        i, header, versions, correct_answer, reference_number = params
        test = models.Test(header, i)
        # test.section_text = section
        test.correct_answer = correct_answer
        test.reference_number = reference_number
        test.versions = versions
        tests.append(test)
    return tests


if __name__ == "__main__":
    text = extract_text_from_pdf(pdf_file)
    # remove first line
    text = text[1:]
    tests = extract_tests(text)
    tests_dict = models.build_tests(tests)
    with open("tests.js", "w") as file:
        data = str(tests_dict)
        data = data.replace("\n", """
                                    """)
        file.write(data)
    print("Done")
