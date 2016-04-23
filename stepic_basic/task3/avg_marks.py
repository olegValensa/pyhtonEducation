def avg_student_mark(marks):
    student_sum = 0
    for mark in marks:
        student_sum += int(mark)
    return str(student_sum / 3) + '\n'

def avg_discipline(marks):
    math_total += int(marks[0])
    physics_total += int(marks[1])
    lang_total += int(marks[2])
    math_total += 1
    physics_total += 1
    lang_total += 1



with open("files/dataset_3363_4.txt") as f:
    math_total = math_count = 0
    physics_total = physics_count = 0
    lang_total = lang_count = 0
    o = open('files/out.txt', 'w')
    for line in f:
        student_sum = 0
        student = line.strip().split(';')
        o.write(avg_student_mark(student[1:]))
        math_total += int(student[1])
        physics_total += int(student[2])
        lang_total += int(student[3])
        math_count += 1
        physics_count += 1
        lang_count += 1
    o.write(str(math_total / math_count) + ' ' + str(physics_total / physics_count) + ' ' + str(lang_total / lang_count))
    o.close()




