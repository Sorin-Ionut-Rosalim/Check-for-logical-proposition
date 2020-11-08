def check(p):
    opened_paranteces = 0
    maxp = -1
    maxo = -1
    operator_needed = 0
    case = 0
    for i in range(len(p)):
        
        if case == 0:
            if p[i] == "(":
                print(f"Step ", i, ": we found a (, we expect next a (, ! or an atomic proposition")
                opened_paranteces += 1
                operator_needed += 1
                maxp += 1
                case = 1
            elif p[i].isalpha():
                print(f"Step ", i, ": we found a atomic proposition,we expect nothing in next position")
                case = 6
            else:
                print("Expected ( in position", i, "but got", p[i], "instead X")
                return False
        elif case == 1:
            if p[i].isalpha():
                print(f"Step ", i, ": we found a atomic proposition,we expect next an &, |, >, < or an =")
                case = 2 
            elif p[i] == "(":
                print(f"Step ", i, ": we found a (, we expect next a (, ! or an atomic proposition")
                opened_paranteces += 1
                operator_needed += 1
                maxp += 1
                case = 1
            elif p[i] == "!":
                print(f"Step ", i, ": we found a !, we expect next a ( or an atomic proposition")
                case == 3
                maxo += 1
                operator_needed -= 1
            else:
                print("Expected (, ! or an atomic proposition in position", i, "but got", p[i], "instead")
                return False
        elif case == 2:
            if p[i] in ["&", "|", ">", "<", "="]:
                print(f"Step ", i, ": we found a ", p[i],", we expect next a ( or an atomic proposition")
                operator_needed -= 1
                maxo += 1
                case = 3
            elif p[i] == ')':
                print(f"Step ", i, ": we found a ), we expect next a ) or  an &, |, >, <, =")
                opened_paranteces -= 1
                case = 5
            else:
                print("Expected binary operator in position", i, "but got", p[i], "instead")
                return False
        elif case == 3:
            if p[i].isalpha():
                print(f"Step ", i, ": we found a atomic proposition,we expect next an &, |, >, < or an =")
                case = 4
            elif p[i] == '(':
                print(f"Step ", i, ": we found a (, we expect next a (, ! or an atomic proposition")
                opened_paranteces += 1
                operator_needed += 1
                maxp += 1
                case = 1
            else:
                print("Expected a ( or an atomic sentence in position", i, "but got", p[i], "instead")
                return False
        elif case == 4:
            if p[i] == ')':
                print(f"Step ", i, ": we found a ), we expect next a ) or  an &, |, >, <, =")
                opened_paranteces -= 1
                case = 5
            else:
                print("Expected a ) or an atomic sentence in position", i, "but got", p[i], "instead")
                return False
        elif case == 5:
            if p[i] in ['&', '|', '=', '<', '>']:
                print(f"Step {i}: we found a ", p[i],", we expect next a ( or an atomic proposition")
                operator_needed -= 1
                maxo += 1
                case = 3
            elif p[i] == ')':
                print(f"Step ", i, ": we found a ), we expect next a ) or an &, |, >, <, =")
                case = 5
                opened_paranteces -= 1
            else:
                print("Expected ) or a binary operator in position", i, "but got", p[i], "instead")
                return False
        elif case == 6:
            if p[i]:
                print("Expected nothing in position", i, "but got", p[i])
                return False
    if maxp == maxo:
        if operator_needed == 0 and opened_paranteces == 0:
            print("END of the proposition. The proposition is correct.")
    else:
        if maxp - maxo == 1:
            print(maxp - maxo," extra set of paranteses")
            return False
        else:
            print(maxp - maxo," extra sets of paranteses")
            return False





print(" ! is the symbol for not\n","| is the symbol for or\n",
      "& is the symbol for and\n","> is the symbol for implies\n",
      "< is the symbol for is implied by\n",
      "= is the symbol for if and only if\n",
      "Any upper case letter is an atomic proposition")
p = input(" Plese input a string of symbols:\n")
print("\n")
for i in range(len(p)):
    print(p[i], end ="  ")
print("\n")
for i in range(len(p)): 
    print(i, end ="  ") 
print("\n")
check(p)