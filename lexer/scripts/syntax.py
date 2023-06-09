i = 0
current_token = None
flag = 0


def Foo(tokens):
    def getToken_Huzaifa():
        global flag, current_token, i
        if not flag:
            if i < len(tokens):
                current_token = tokens[i]
                i += 1  # Increment i by 1
            else:
                current_token = "INVALID"
            return current_token
        else:
            flag = 0
            return current_token

    def unGetToken():
        global flag
        flag = 1

    def While_Huzaifa():
        Huzaifa_Token = getToken_Huzaifa()
        if Huzaifa_Token[0] == "WHILE":
            Huzaifa_Token = getToken_Huzaifa()
            if Huzaifa_Token[0] == 'LEFT_ROUND_BRACKET':
                if Comparison():
                    Huzaifa_Token = getToken_Huzaifa()
                    if Huzaifa_Token[0] == 'RIGHT_ROUND_BRACKET':
                        Huzaifa_Token = getToken_Huzaifa()
                        if Huzaifa_Token[0] == 'LEFT_CURLY_BRACKET':
                            if StatementList_Huzaifa():
                                Huzaifa_Token = getToken_Huzaifa()
                                if Huzaifa_Token[0] == 'RIGHT_CURLY_BRACKET':
                                    return True
        return False

    def Do_While_Huzaifa():
        Huzaifa_Token = getToken_Huzaifa()
        if Huzaifa_Token[0] == 'DO':
            Huzaifa_Token = getToken_Huzaifa()
            if Huzaifa_Token[0] == 'LEFT_CURLY_BRACKET':
                if Assignment_Huzaifa():
                    Huzaifa_Token = getToken_Huzaifa()
                    if Huzaifa_Token[0] == 'RIGHT_CURLY_BRACKET':
                        Huzaifa_Token = getToken_Huzaifa()
                        if Huzaifa_Token[0] == 'WHILE':
                            Huzaifa_Token = getToken_Huzaifa()
                            if Huzaifa_Token[0] == 'LEFT_ROUND_BRACKET':
                                if Comparison():
                                    Huzaifa_Token = getToken_Huzaifa()
                                    if Huzaifa_Token[0] == 'RIGHT_ROUND_BRACKET':
                                        Huzaifa_Token = getToken_Huzaifa()
                                        if Huzaifa_Token[0] == 'SEMICOLON':
                                            return True
        return False

    def If_Huzaifa():
        Huzaifa_Token = getToken_Huzaifa()
        if Huzaifa_Token[0] == 'IF':
            Huzaifa_Token = getToken_Huzaifa()
            if Huzaifa_Token[0] == 'LEFT_ROUND_BRACKET':
                if Comparison():
                    Huzaifa_Token = getToken_Huzaifa()
                    if Huzaifa_Token[0] == 'RIGHT_ROUND_BRACKET':
                        Huzaifa_Token = getToken_Huzaifa()
                        if Huzaifa_Token[0] == 'LEFT_CURLY_BRACKET':
                            if StatementList_Huzaifa():
                                Huzaifa_Token = getToken_Huzaifa()
                                if Huzaifa_Token[0] == 'RIGHT_CURLY_BRACKET':
                                    return True
        return False

    def If_Else_Huzaifa():
        Huzaifa_Token = getToken_Huzaifa()
        if Huzaifa_Token[0] == 'IF':
            Huzaifa_Token = getToken_Huzaifa()
            if Huzaifa_Token[0] == 'LEFT_ROUND_BRACKET':
                if Comparison():
                    Huzaifa_Token = getToken_Huzaifa()
                    if Huzaifa_Token[0] == 'RIGHT_ROUND_BRACKET':
                        Huzaifa_Token = getToken_Huzaifa()
                        if Huzaifa_Token[0] == 'LEFT_CURLY_BRACKET':
                            if Assignment_Huzaifa():
                                Huzaifa_Token = getToken_Huzaifa()
                                if Huzaifa_Token[0] == 'RIGHT_CURLY_BRACKET':
                                    Huzaifa_Token = getToken_Huzaifa()
                                    if Huzaifa_Token[0] == 'ELSE':
                                        Huzaifa_Token = getToken_Huzaifa()
                                        if Huzaifa_Token[0] == 'LEFT_CURLY_BRACKET':
                                            if StatementList_Huzaifa():
                                                Huzaifa_Token = getToken_Huzaifa()
                                                if Huzaifa_Token[0] == 'RIGHT_CURLY_BRACKET':
                                                    return True
                                    unGetToken()
                                    return True
            if StatementList_Huzaifa():
                return True
        if Huzaifa_Token[0] == 'ELSE':
            Huzaifa_Token = getToken_Huzaifa()
            if Huzaifa_Token[0] == 'LEFT_CURLY_BRACKET':
                if StatementList_Huzaifa():
                    Huzaifa_Token = getToken_Huzaifa()
                    if Huzaifa_Token[0] == 'RIGHT_CURLY_BRACKET':
                        return True
        return False

    def Comparison():
        if not F_Huzaifa():
            return False
        Huzaifa_Token = getToken_Huzaifa()
        if Huzaifa_Token[0] in ['LESS_THAN_EQUAL', 'EQUAL_TO', 'GREATER_THAN_EQUAL', 'NOT_EQUAL']:
            if F_Huzaifa():
                return True
        unGetToken()  # Add this line to "unget" the token if comparison fails
        return False

    def Program_Huzaifa():
        # Huzaifa_Token = getToken_Huzaifa()
        # if Huzaifa_Token[0] != 'BEGIN':
        #   return False
        if not StatementList_Huzaifa():
            return False
        # Huzaifa_Token = getToken_Huzaifa()
        # if Huzaifa_Token[0] != 'END':
        #   return False
        return True

    def StatementList_Huzaifa():
        if Statement_Huzaifa():
            while True:
                if i != len(tokens):
                    Huzaifa_Token = getToken_Huzaifa()
                # print("Current Token:", Huzaifa_Token)  # Debug print statement
                    if Huzaifa_Token[0] in ['IF', 'DO', 'WHILE', 'ELSE']:
                        unGetToken()
                        if not Statement_Huzaifa():
                            return False
                    else:
                        unGetToken()
                        break
                else:
                    break
            return True
        # unGetToken()  # Add this line to "unget" the token if statement list is empty
        return False

    def Statement_Huzaifa():
        if Assignment_Huzaifa():
            return True
        unGetToken()
        if If_Huzaifa():
            return True
        unGetToken()
        if If_Else_Huzaifa():
            return True
        unGetToken()
        if While_Huzaifa():
            return True
        unGetToken()
        if Do_While_Huzaifa():
            return True
        return False

    def Assignment_Huzaifa():
        Huzaifa_Token = getToken_Huzaifa()
        if Huzaifa_Token[0] != 'IDENTIFIER':
            unGetToken()
            return False
        Huzaifa_Token = getToken_Huzaifa()
        if Huzaifa_Token[0] != 'ASSIGN':
            unGetToken()
            return False
        if not OR_Huzaifa():
            unGetToken()
            return False
        Huzaifa_Token = getToken_Huzaifa()
        if Huzaifa_Token[0] != 'SEMICOLON':
            unGetToken()
            return False
        return True

    def OR_Huzaifa():
        if not AND_Huzaifa():
            return False
        Huzaifa_Token = getToken_Huzaifa()
        while Huzaifa_Token[0] == 'OR':
            if not AND_Huzaifa():
                return False
            Huzaifa_Token = getToken_Huzaifa()
        unGetToken()
        return True

    def AND_Huzaifa():
        if not Bouble_Equal_Operators_Huzaifa():
            return False
        Huzaifa_Token = getToken_Huzaifa()
        while Huzaifa_Token[0] == 'AND':
            if not Bouble_Equal_Operators_Huzaifa():
                return False
            Huzaifa_Token = getToken_Huzaifa()
        unGetToken()
        return True

    def Bouble_Equal_Operators_Huzaifa():
        if not Greater_Lesser_Equal_Operators_Huzaifa():
            return False
        Huzaifa_Token = getToken_Huzaifa()
        while Huzaifa_Token[0] in ['EQUAL_TO', 'NOT_EQUAL']:
            if not Greater_Lesser_Equal_Operators_Huzaifa():
                return False
            Huzaifa_Token = getToken_Huzaifa()
        unGetToken()
        return True

    def Greater_Lesser_Equal_Operators_Huzaifa():
        if not E_Huzaifa():
            return False
        Huzaifa_Token = getToken_Huzaifa()
        while Huzaifa_Token[0] in ['LESS_THAN_EQUAL', 'GREATER_THAN_EQUAL']:
            if not E_Huzaifa():
                return False
            Huzaifa_Token = getToken_Huzaifa()
        unGetToken()
        return True

    def E_Huzaifa():
        if not T_Huzaifa():
            return False
        Huzaifa_Token = getToken_Huzaifa()
        while Huzaifa_Token[0] in ['PLUS', 'MINUS']:
            if not T_Huzaifa():
                return False
            Huzaifa_Token = getToken_Huzaifa()
        unGetToken()
        return True

    def T_Huzaifa():
        if not F_Huzaifa():
            return False
        Huzaifa_Token = getToken_Huzaifa()
        while Huzaifa_Token[0] in ['MULTIPLY', 'DIVIDE', 'MODULUS']:
            if not F_Huzaifa():
                return False
            Huzaifa_Token = getToken_Huzaifa()
        unGetToken()
        return True

    def F_Huzaifa():
        Huzaifa_Token = getToken_Huzaifa()
        if Huzaifa_Token[0] == 'IDENTIFIER' or Huzaifa_Token[0] == 'NUMBER':
            return True
        elif Huzaifa_Token[0] == 'LEFT_ROUND_BRACKET':
            if OR_Huzaifa():
                Huzaifa_Token = getToken_Huzaifa()
                if Huzaifa_Token[0] == 'RIGHT_ROUND_BRACKET':
                    return True
        unGetToken()
        return False

    if Program_Huzaifa():
        return True
    else:
        return False
