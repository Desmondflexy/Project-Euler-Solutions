# Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
# Output: true
#
# Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
# Output: false

def TreeConstructor(strArr: list) -> bool:
    newStrArr = []
    for i in strArr:
        a = int(i.split(',')[0][1:])
        b = int(i.split(',')[1][:-1])
        newStrArr.append((a, b))

    strArr = newStrArr
    children = []
    parents = []
    for i in strArr:
        children.append(i[0])
        parents.append(i[1])

    def oneRoot():
        'Checks if tree has one root node'
        roots = []
        for i in parents:
            if i not in children:
                roots.append(i)
        return len(set(roots)) == 1

    def oneParent():
        'Checks if every child node has only one parent'
        return all(children.count(i) == 1 for i in children)

    def atLeastTwoChildren():
        'Checks if every parent has at least two children'
        return all(parents.count(i) <= 2 for i in parents)

    if not oneRoot():
        # print('not one root')
        strArr = False

    elif not oneParent():
        # print('not one parent')
        strArr = False

    elif not atLeastTwoChildren():
        # print('more than two children')
        strArr = False

    else:
        strArr = True

    return strArr

print(TreeConstructor(["(1,2)", "(2,4)", "(7,2)"]))
