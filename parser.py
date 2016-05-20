# -*- coding: utf-8 -*-
import lxml.html as html
import requests
import os


def create_files(dict_problem):
    path = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists('solutions'):
        os.makedirs('solutions')
    for x in dict_problem:
        number_problrm = [int(s) for s in x.split("_") if s.isdigit()][0]
        name_f = str((number_problrm // 20) * 20) + "-" + str((number_problrm // 20) * 20+20)
        if not os.path.exists('solutions/'+name_f):
            os.makedirs('solutions/'+name_f)
        if not os.path.exists(path+"\\solutions\\"+name_f+"\\"+x+"_"+dict_problem[x]['name']+".py"):
            file = open(path+"\\solutions\\"+name_f+"\\"+x+"_"+dict_problem[x]['name']+".py", 'w',encoding='utf-8')
            file.write('"""'+dict_problem[x]['description']+'"""')
            file.write('\nfrom decorators_k import writeResult\n')
            file.write('import sys\nsys.path.insert(0, "..")\n\n')

            file.write('\n@writeResult\n')
            file.write('def solution(x = None):')
            file.write('\n    pass\n')
            file.write('\n')
            file.write('solution()\n')
            file.close()
            print("Good!",x+"_"+dict_problem[x]['name']+".py")


def parse_euler_problem(start=0,stop=-1):
    main_domain_stat = 'https://projecteuler.net/'
    problem_dict = {}
    problem_counter = start
    while True:
        response = requests.get("{domain}{att}{index}".format(domain = main_domain_stat, att = "problem=", index = problem_counter))
        parsed_body = html.fromstring(response.text)
        not_found = parsed_body.xpath("//div[@id='content']/div[@id='message']")
        if not_found or problem_counter == stop:
            break
        name_task = str(parsed_body.xpath('//h2/text()')[0]).replace(" ", "_").lower().strip()
        number_task = str(parsed_body.xpath('//h3/text()')[0]).replace(" ", "_").lower().strip()
        task_descriprion = str(parsed_body.xpath("//div[@role='problem']")[0].text_content()).strip()
        print("Courrent problem:", problem_counter)

        if number_task not in problem_dict:
            problem_dict[number_task] = dict(name=name_task, description=task_descriprion)
        problem_counter += 1
    print("GREAT!!!")
    return problem_dict


create_files(parse_euler_problem(int(input("Start: ")), int(input("Stop: "))))







