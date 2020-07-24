'''
Input:
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

Input:
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
Output:
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
'''

def arithmetic_arranger(problems, *need_ans):

    if len(problems) > 5:
        return "Error: Too many problems."
    
    rows = ['','','']
    if need_ans: rows.append('')
    
    for p in problems:
        p = (p.split(' '))
        width = len(max(p, key=len)) + 2
        num_1, operator, num_2 = p[0], p[1], p[2]
       
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
        if len(num_1) > 4 or len(num_2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not num_1.isnumeric() or not num_2.isnumeric():
            return "Error: Numbers must only contain digits."
        rows[0] += num_1.rjust(width) + ' '*4
        rows[1] += operator + ' ' + num_2.rjust(width - 2) + ' '*4
        rows[2] += '-' * (width) + ' ' * 4
        if need_ans:
            if operator == '+':
                rows[3] += str((int(num_1) + int(num_2))).rjust(width) + ' '*4
            elif operator == '-':
                rows[3] += str((int(num_1) - int(num_2))).rjust(width) + ' '*4

    return '\n'.join([x.rstrip() for x in rows]) 





print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))
print()




