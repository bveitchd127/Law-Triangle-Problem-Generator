import random, math

def sin(degrees):
    return math.sin(math.radians(degrees))

def cos(degrees):
    return math.cos(math.radians(degrees))

def asin(ratio):
    return math.degrees(math.asin(ratio))

def acos(ratio):
    return math.degrees(math.acos(ratio))

def sqrt(num):
    return math.sqrt(num)

def randrange(lower, upper):
    return random.random()*(upper - lower) + lower

def lawOfCosine(a, b, c):
    return acos((c**2 - a**2 - b**2) / (-2*a*b))

def getProblemThreeSides():
    sideA = random.randint(2,20)
    sideB = random.randint(2,20)
    sideC = random.randint(abs(sideA - sideB) + 1, sideA + sideB - 1)
    angleC = round(lawOfCosine(sideA, sideB, sideC),2)
    angleB = round(lawOfCosine(sideA, sideC, sideB),2)
    angleA = round(lawOfCosine(sideB, sideC, sideA),2)
    given = ((sideA, sideB, sideC), (None, None, None))
    solved = ((sideA, sideB, sideC), (angleA, angleB, angleC))
    return given, solved

def getProblemTwoSidesOneAngle():
    # two variants, either angle is between the sides or it is not
    if (random.randint(1,2) == 1):
        sideA  = random.randint(2,20)
        sideB  = random.randint(2,20)
        angleC = random.randint(20, 160)
        given = ((sideA, sideB, None), (None, None, angleC))

        sideC  = round( sqrt( sideA**2 + sideB**2 - 2*sideA*sideB*cos(angleC) ), 2)
        angleB = round( asin( sideB*sin(angleC) / sideC ), 2)
        angleA = round( 180 - angleB - angleC, 2)
    else:
        sideA = random.randint(6,30)
        sideB = random.randint(sideA//3+1,sideA)
        angleB = random.randint(15, math.floor( asin(sideB/sideA) -5))
        given = ((sideA, sideB, None), (None, angleB, None))
        
        angleA = round( asin( sideA*sin(angleB)/sideB ) , 2)
        
        angleC = round(180 - angleA - angleB,2)
        sideC = round((sideA**2 + sideB**2 - 2*sideA*sideB*cos(angleC))**0.5,2)

    solved = ((sideA, sideB, sideC), (angleA, angleB, angleC))
    return given, solved

def getProblemOneSideTwoAngles():
    # side is between or not
    # between
    if (random.randint(1,2) == 1):
        angleA = random.randint(20,110)
        angleB = random.randint(10, 180 - angleA - 10)
        sideC = random.randint(5,30)
        given = ((None, None, sideC), (angleA, angleB, None))

        angleC = 180 - angleA - angleB
        sideB = round(sideC*sin(angleB)/sin(angleC),2)
        sideA = round(sideC*sin(angleA)/sin(angleC),2)
    
    else:
        angleA = random.randint(20,110)
        angleB = random.randint(10, 180 - angleA - 10)
        sideA = random.randint(5,30)
        given = ((sideA, None, None), (angleA, angleB, None))

        sideB = round(sideA*sin(angleB)/sin(angleA),2)
        angleC = round(180 - angleA - angleB,2)
        sideC = round(sideA*sin(angleC)/sin(angleA))


    solved = ((sideA, sideB, sideC), (angleA, angleB, angleC))
    return given, solved
    
def makeTriangleProblem(problem):
    letterStart = random.randint(65, 65+26-3)
    letters = [chr(li) for li in range(letterStart, letterStart+3)]
    order   = [0,1,2]
    random.shuffle(order)
    sides  = problem[0][0]
    angles = problem[0][1]
    output = []
    possibleToBeAnswered = []
    for i in range(3):
        letter = letters[order[i]]
        side = sides[order[i]]
        if side:
            output.append( f"side {letter.lower()} is {side}" )
        else:
            possibleToBeAnswered.append((f"side {letter.lower()}", (0,order[i])))
        angle = angles[order[i]]
        if angle:
            output.append( f"∠{letter} is {angle}°" )
        else:
            possibleToBeAnswered.append((f"∠{letter}", (1,order[i])))

    triangleName = "△" + letters[0] + letters[1] + letters[2]
    toBeAnsweredTuple = random.choice(possibleToBeAnswered)
    toBeAnswered = toBeAnsweredTuple[0]
    answer = problem[1][toBeAnsweredTuple[1][0]][toBeAnsweredTuple[1][1]]
    # solving for angle
    if toBeAnsweredTuple[1][0] == 1:
        answers = [round(randrange(max(round(answer-45), 10), min(round(answer + 45), 170)),2) for i in range(3)]
        answers.append(answer)
        random.shuffle(answers)
        correctAnswer = answers.index(answer)
    else:
        answers = [round(randrange(1, round(answer*2)),2) for i in range(3)]
        answers.append(answer)
        random.shuffle(answers)
        correctAnswer = answers.index(answer)

    return f"In {triangleName}, {output[0]}, {output[1]}, and {output[2]}. Solve for {toBeAnswered}", (answers, answer, correctAnswer)
# A = 65

def getNewAnswerSums(problem):
    total = 0
    # add angles
    for i in range(3):
        given = problem[0][1][i]
        solut = problem[1][1][i]
        if given != solut:
            total += solut
    
    # add sides
    for i in range(3):
        given = problem[0][0][i]
        solut = problem[1][0][i]
        if given != solut:
            total += solut
    
    return total



problemGenerators = [getProblemThreeSides, getProblemTwoSidesOneAngle, getProblemOneSideTwoAngles]

for i in range(100):
    problem = random.choice(problemGenerators)()
    formatted = makeTriangleProblem(problem)
    print(formatted[0], formatted[1][0][0], formatted[1][0][1], formatted[1][0][2], formatted[1][0][3], 300, formatted[1][2]+1, sep="|")
    
