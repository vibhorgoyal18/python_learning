import xlrd
# student_report_cards = [
#     {
#         'name': "Ramu",
#         'roll_number': 1,
#         'marks_in_maths': 45,
#         'marks_in_science': 57,
#         'marks_in_english': 76,
#     },
#     {
#         'name': "Raj",
#         'roll_number': 2,
#         'marks_in_maths': 67,
#         'marks_in_science': 85,
#         'marks_in_english': 65,
#     }
# ]

workbook = xlrd.open_workbook('student_report_card.xlsx')
sheet = workbook.sheet_by_index(0)

student_report_cards = []
for row_number in sheet.nrows:
    if row_number == 0:
        continue

    student_report_card = {
        'roll_number': sheet.cell_value(row_number, 0),
        'name': sheet.cell_value(row_number, 1),
        'marks_in_maths': sheet.cell_value(row_number, 2),
        'marks_in_science': sheet.cell_value(row_number, 3),
        'marks_in_english': sheet.cell_value(row_number, 4),
    }

    student_report_cards.append(student_report_card)


# Provide grace marks to student
# 1. If student fails in one subject
# 2. Grace marks should be max 5
# 3. If marks are suppose 30. For that particular subject, display marks as '30 + 3'

# Student should fail if he is failed in one or more subjects
# 1. If fails in one subject and marks are less than 28
# 2. If fails in more than 1 subject
for student_report_card in student_report_cards:

    student_report_card['total_marks'] = student_report_card['marks_in_maths'] + \
        student_report_card['marks_in_science'] + \
        student_report_card['marks_in_english']
    student_report_card['result'] = 'Pass' if student_report_card['total_marks'] / \
        3 >= 33 else 'Fail'
    print('Roll No:     ' + str(student_report_card['roll_number']))
    print('Name:        ' + student_report_card['name'])
    print('Maths        ' + str(student_report_card['marks_in_maths']))
    print('Science:     ' + str(student_report_card['marks_in_science']))
    print('English:     ' + str(student_report_card['marks_in_english']))
    print('Total:       ' + str(student_report_card['total_marks']))
    print('Pass/Fail:   ' + student_report_card['result'])
    print('*****************************')
