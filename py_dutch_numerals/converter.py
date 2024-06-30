from .logger import Logger
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from .generated.DutchNumbersVisitor import DutchNumbersVisitor
from .generated.DutchNumbers import DutchNumbers
from .generated.DutchNumbersLexer import DutchNumbersLexer

class TelVisitor(DutchNumbersVisitor):
    def defaultResult(self):
        return 0

    def visitNumber(self, ctx:DutchNumbers.NumberContext):
        return self.visit(ctx.whole_number())

    def visitWhole_number(self, ctx:DutchNumbers.Whole_numberContext):
        if ctx.ones(): return self.visit(ctx.ones())
        if ctx.tens(): return self.visit(ctx.tens())
        if ctx.hundreds(): return self.visit(ctx.hundreds())
        if ctx.thousands(): return self.visit(ctx.thousands())
        if ctx.millions(): return self.visit(ctx.millions())
        if ctx.billions(): return self.visit(ctx.billions())
        if ctx.triljons(): return self.visit(ctx.triljons())
        if ctx.quadrilions(): return self.visit(ctx.quadrilions())
        if ctx.quintilions(): return self.visit(ctx.quintilions())
        if ctx.sextilions(): return self.visit(ctx.sextilions())
        return 0

    def visitOnes(self, ctx:DutchNumbers.OnesContext):
        return self.getValueFromTerminal(ctx.getChild(0)) or 0

    def visitTens(self, ctx:DutchNumbers.TensContext):
        result = 0
        ones = 0
        tens = 0
    
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                value = self.getValueFromTerminal(child)
                if value is not None:
                    if value >= 20:
                        tens = value
                    elif value < 10:
                        ones = value
                    else:
                        result = value
            elif isinstance(child, DutchNumbers.OnesContext):
                ones = self.visit(child)
    
        if result == 0:
            result = tens + ones
    
        return result

    def visitHundreds(self, ctx:DutchNumbers.HundredsContext):
        result = 0
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                value = self.getValueFromTerminal(child)
                if value is not None:
                    result = value if result == 0 else result * value
            else:
                result += self.visit(child)
        return result

    def visitThousands(self, ctx:DutchNumbers.ThousandsContext):
        result = 0
        multiplier = 1
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                value = self.getValueFromTerminal(child)
                if value == 1000:
                    result = (1 if result == 0 else result) * value
                elif value is not None:
                    multiplier *= value
            else:
                result += self.visit(child)
        return result * multiplier

    def visitMillions(self, ctx:DutchNumbers.MillionsContext):
        result = 0
        multiplier = 1
        
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                value = self.getValueFromTerminal(child)
                if value == 1000000:
                    result = (1 if result == 0 else result) * value
                elif value is not None:
                    multiplier *= value
            else:
                child_value = self.visit(child)
                if result == 0:
                    result = child_value
                else:
                    result += child_value
        
        return result * multiplier

    def visitBillions(self, ctx:DutchNumbers.BillionsContext):
        result = 0
        multiplier = 1
        
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                value = self.getValueFromTerminal(child)
                if value == 1000000000:
                    result = (1 if result == 0 else result) * value
                elif value is not None:
                    multiplier *= value
            else:
                child_value = self.visit(child)
                if result == 0:
                    result = child_value
                else:
                    result += child_value
        
        return result * multiplier

    def visitTriljons(self, ctx:DutchNumbers.TriljonsContext):
        result = 1000000000000
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                value = self.getValueFromTerminal(child)
                if value is not None and value != 1000000000000:
                    result *= value
            else:
                result += self.visit(child)
        return result

    def visitQuadrilions(self, ctx:DutchNumbers.QuadrilionsContext):
        result = 1000000000000000
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                value = self.getValueFromTerminal(child)
                if value is not None and value != 1000000000000000:
                    result *= value
            else:
                result += self.visit(child)
        return result

    def visitQuintilions(self, ctx:DutchNumbers.QuintilionsContext):
        result = 1000000000000000000
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                value = self.getValueFromTerminal(child)
                if value is not None and value != 1000000000000000000:
                    result *= value
            else:
                result += self.visit(child)
        return result

    def visitSextilions(self, ctx:DutchNumbers.SextilionsContext):
        result = 1000000000000000000000
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                value = self.getValueFromTerminal(child)
                if value is not None and value != 1000000000000000000000:
                    result *= value
            else:
                result += self.visit(child)
        return result

    def getValueFromTerminal(self, node):
        type = node.symbol.type
        if DutchNumbersLexer.ONE <= type <= DutchNumbersLexer.SEXTILION:
            values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                      20, 30, 40, 50, 60, 70, 80, 90, 100, 1000, 1000000, 1000000000,
                      1000000000000, 1000000000000000, 1000000000000000000, 1000000000000000000000]
            return values[type - DutchNumbersLexer.ONE]
        return None
class Tel:
    _logger: Logger = None

    @classmethod
    def set_logger(cls, logger: Logger):
        cls._logger = logger

    @classmethod
    def parse(cls, text: str) -> int:
        if cls._logger is None:
            raise ValueError("Logger not set. Call Tel.set_logger() before parsing.")

        try:
            input_stream = InputStream(text)
            lexer = DutchNumbersLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = DutchNumbers(stream)
            
            # Add an error listener to catch lexer and parser errors
            error_listener = SyntaxErrorListener()
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)

            tree = parser.number()

            if error_listener.errors:
                raise ValueError("Invalid number context")

            visitor = TelVisitor()
            result = visitor.visit(tree)

            cls._logger.log_info(f"Successfully parsed input: {text} to {result}")
            return result
        except Exception as e:
            error_message = f"Error parsing input: {str(e)}"
            cls._logger.log_error(error_message)
            raise ValueError(error_message)

tel = Tel.parse

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")