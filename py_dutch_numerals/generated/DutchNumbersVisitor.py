# Generated from DutchNumbers.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DutchNumbers import DutchNumbers
else:
    from DutchNumbers import DutchNumbers

# This class defines a complete generic visitor for a parse tree produced by DutchNumbers.

class DutchNumbersVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DutchNumbers#number.
    def visitNumber(self, ctx:DutchNumbers.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#whole_number.
    def visitWhole_number(self, ctx:DutchNumbers.Whole_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#ones.
    def visitOnes(self, ctx:DutchNumbers.OnesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#tens.
    def visitTens(self, ctx:DutchNumbers.TensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#hundreds.
    def visitHundreds(self, ctx:DutchNumbers.HundredsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#prefixes.
    def visitPrefixes(self, ctx:DutchNumbers.PrefixesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#thousands.
    def visitThousands(self, ctx:DutchNumbers.ThousandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#millions.
    def visitMillions(self, ctx:DutchNumbers.MillionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#billions.
    def visitBillions(self, ctx:DutchNumbers.BillionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#triljons.
    def visitTriljons(self, ctx:DutchNumbers.TriljonsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#quadrilions.
    def visitQuadrilions(self, ctx:DutchNumbers.QuadrilionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#quintilions.
    def visitQuintilions(self, ctx:DutchNumbers.QuintilionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#sextilions.
    def visitSextilions(self, ctx:DutchNumbers.SextilionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#thousands_suffixes.
    def visitThousands_suffixes(self, ctx:DutchNumbers.Thousands_suffixesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#millions_suffixes.
    def visitMillions_suffixes(self, ctx:DutchNumbers.Millions_suffixesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#billions_suffixes.
    def visitBillions_suffixes(self, ctx:DutchNumbers.Billions_suffixesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#triljons_suffixes.
    def visitTriljons_suffixes(self, ctx:DutchNumbers.Triljons_suffixesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#quadrilions_suffixes.
    def visitQuadrilions_suffixes(self, ctx:DutchNumbers.Quadrilions_suffixesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#quintilions_suffixes.
    def visitQuintilions_suffixes(self, ctx:DutchNumbers.Quintilions_suffixesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DutchNumbers#sextilions_suffixes.
    def visitSextilions_suffixes(self, ctx:DutchNumbers.Sextilions_suffixesContext):
        return self.visitChildren(ctx)



del DutchNumbers