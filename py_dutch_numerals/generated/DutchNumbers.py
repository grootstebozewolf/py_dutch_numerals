# Generated from DutchNumbers.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,194,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,54,8,1,1,2,1,
        2,1,3,1,3,1,3,3,3,61,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,74,8,3,1,4,1,4,3,4,78,8,4,1,4,1,4,3,4,82,8,4,1,4,1,4,3,4,
        86,8,4,3,4,88,8,4,1,5,1,5,1,5,3,5,93,8,5,1,6,3,6,96,8,6,1,6,1,6,
        3,6,100,8,6,1,6,3,6,103,8,6,1,7,3,7,106,8,7,1,7,1,7,3,7,110,8,7,
        1,7,3,7,113,8,7,1,8,3,8,116,8,8,1,8,1,8,3,8,120,8,8,1,8,3,8,123,
        8,8,1,9,3,9,126,8,9,1,9,1,9,3,9,130,8,9,1,9,3,9,133,8,9,1,10,3,10,
        136,8,10,1,10,1,10,3,10,140,8,10,1,10,3,10,143,8,10,1,11,3,11,146,
        8,11,1,11,1,11,3,11,150,8,11,1,11,3,11,153,8,11,1,12,3,12,156,8,
        12,1,12,1,12,3,12,160,8,12,1,12,3,12,163,8,12,1,13,1,13,1,13,3,13,
        168,8,13,1,14,1,14,3,14,172,8,14,1,15,1,15,3,15,176,8,15,1,16,1,
        16,3,16,180,8,16,1,17,1,17,3,17,184,8,17,1,18,1,18,3,18,188,8,18,
        1,19,1,19,3,19,192,8,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,0,2,1,0,1,9,1,0,20,27,229,0,40,1,0,0,
        0,2,53,1,0,0,0,4,55,1,0,0,0,6,73,1,0,0,0,8,77,1,0,0,0,10,92,1,0,
        0,0,12,95,1,0,0,0,14,105,1,0,0,0,16,115,1,0,0,0,18,125,1,0,0,0,20,
        135,1,0,0,0,22,145,1,0,0,0,24,155,1,0,0,0,26,167,1,0,0,0,28,171,
        1,0,0,0,30,175,1,0,0,0,32,179,1,0,0,0,34,183,1,0,0,0,36,187,1,0,
        0,0,38,191,1,0,0,0,40,41,3,2,1,0,41,42,5,0,0,1,42,1,1,0,0,0,43,54,
        3,4,2,0,44,54,3,6,3,0,45,54,3,8,4,0,46,54,3,12,6,0,47,54,3,14,7,
        0,48,54,3,16,8,0,49,54,3,18,9,0,50,54,3,20,10,0,51,54,3,22,11,0,
        52,54,3,24,12,0,53,43,1,0,0,0,53,44,1,0,0,0,53,45,1,0,0,0,53,46,
        1,0,0,0,53,47,1,0,0,0,53,48,1,0,0,0,53,49,1,0,0,0,53,50,1,0,0,0,
        53,51,1,0,0,0,53,52,1,0,0,0,54,3,1,0,0,0,55,56,7,0,0,0,56,5,1,0,
        0,0,57,58,3,4,2,0,58,59,5,36,0,0,59,61,1,0,0,0,60,57,1,0,0,0,60,
        61,1,0,0,0,61,62,1,0,0,0,62,74,7,1,0,0,63,74,5,10,0,0,64,74,5,11,
        0,0,65,74,5,12,0,0,66,74,5,13,0,0,67,74,5,14,0,0,68,74,5,15,0,0,
        69,74,5,16,0,0,70,74,5,17,0,0,71,74,5,18,0,0,72,74,5,19,0,0,73,60,
        1,0,0,0,73,63,1,0,0,0,73,64,1,0,0,0,73,65,1,0,0,0,73,66,1,0,0,0,
        73,67,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,0,73,70,1,0,0,0,73,71,1,
        0,0,0,73,72,1,0,0,0,74,7,1,0,0,0,75,78,3,4,2,0,76,78,3,6,3,0,77,
        75,1,0,0,0,77,76,1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,87,5,28,
        0,0,80,82,5,36,0,0,81,80,1,0,0,0,81,82,1,0,0,0,82,85,1,0,0,0,83,
        86,3,4,2,0,84,86,3,6,3,0,85,83,1,0,0,0,85,84,1,0,0,0,86,88,1,0,0,
        0,87,81,1,0,0,0,87,88,1,0,0,0,88,9,1,0,0,0,89,93,3,4,2,0,90,93,3,
        6,3,0,91,93,3,8,4,0,92,89,1,0,0,0,92,90,1,0,0,0,92,91,1,0,0,0,93,
        11,1,0,0,0,94,96,3,10,5,0,95,94,1,0,0,0,95,96,1,0,0,0,96,97,1,0,
        0,0,97,102,5,29,0,0,98,100,5,36,0,0,99,98,1,0,0,0,99,100,1,0,0,0,
        100,101,1,0,0,0,101,103,3,26,13,0,102,99,1,0,0,0,102,103,1,0,0,0,
        103,13,1,0,0,0,104,106,3,10,5,0,105,104,1,0,0,0,105,106,1,0,0,0,
        106,107,1,0,0,0,107,112,5,30,0,0,108,110,5,36,0,0,109,108,1,0,0,
        0,109,110,1,0,0,0,110,111,1,0,0,0,111,113,3,28,14,0,112,109,1,0,
        0,0,112,113,1,0,0,0,113,15,1,0,0,0,114,116,3,10,5,0,115,114,1,0,
        0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,122,5,31,0,0,118,120,5,36,
        0,0,119,118,1,0,0,0,119,120,1,0,0,0,120,121,1,0,0,0,121,123,3,30,
        15,0,122,119,1,0,0,0,122,123,1,0,0,0,123,17,1,0,0,0,124,126,3,10,
        5,0,125,124,1,0,0,0,125,126,1,0,0,0,126,127,1,0,0,0,127,132,5,32,
        0,0,128,130,5,36,0,0,129,128,1,0,0,0,129,130,1,0,0,0,130,131,1,0,
        0,0,131,133,3,32,16,0,132,129,1,0,0,0,132,133,1,0,0,0,133,19,1,0,
        0,0,134,136,3,10,5,0,135,134,1,0,0,0,135,136,1,0,0,0,136,137,1,0,
        0,0,137,142,5,33,0,0,138,140,5,36,0,0,139,138,1,0,0,0,139,140,1,
        0,0,0,140,141,1,0,0,0,141,143,3,34,17,0,142,139,1,0,0,0,142,143,
        1,0,0,0,143,21,1,0,0,0,144,146,3,10,5,0,145,144,1,0,0,0,145,146,
        1,0,0,0,146,147,1,0,0,0,147,152,5,34,0,0,148,150,5,36,0,0,149,148,
        1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,153,3,36,18,0,152,149,
        1,0,0,0,152,153,1,0,0,0,153,23,1,0,0,0,154,156,3,10,5,0,155,154,
        1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,162,5,35,0,0,158,160,
        5,36,0,0,159,158,1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,163,
        3,38,19,0,162,159,1,0,0,0,162,163,1,0,0,0,163,25,1,0,0,0,164,168,
        3,4,2,0,165,168,3,6,3,0,166,168,3,8,4,0,167,164,1,0,0,0,167,165,
        1,0,0,0,167,166,1,0,0,0,168,27,1,0,0,0,169,172,3,26,13,0,170,172,
        3,12,6,0,171,169,1,0,0,0,171,170,1,0,0,0,172,29,1,0,0,0,173,176,
        3,28,14,0,174,176,3,14,7,0,175,173,1,0,0,0,175,174,1,0,0,0,176,31,
        1,0,0,0,177,180,3,28,14,0,178,180,3,14,7,0,179,177,1,0,0,0,179,178,
        1,0,0,0,180,33,1,0,0,0,181,184,3,32,16,0,182,184,3,18,9,0,183,181,
        1,0,0,0,183,182,1,0,0,0,184,35,1,0,0,0,185,188,3,34,17,0,186,188,
        3,20,10,0,187,185,1,0,0,0,187,186,1,0,0,0,188,37,1,0,0,0,189,192,
        3,36,18,0,190,192,3,22,11,0,191,189,1,0,0,0,191,190,1,0,0,0,192,
        39,1,0,0,0,36,53,60,73,77,81,85,87,92,95,99,102,105,109,112,115,
        119,122,125,129,132,135,139,142,145,149,152,155,159,162,167,171,
        175,179,183,187,191
    ]

class DutchNumbers ( Parser ):

    grammarFileName = "DutchNumbers.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'een'", "'twee'", "'drie'", "'vier'", 
                     "'vijf'", "'zes'", "'zeven'", "'acht'", "'negen'", 
                     "'tien'", "'elf'", "'twaalf'", "'dertien'", "'veertien'", 
                     "'vijftien'", "'zestien'", "'zeventien'", "'achttien'", 
                     "'negentien'", "'twintig'", "'dertig'", "'veertig'", 
                     "'vijftig'", "'zestig'", "'zeventig'", "'tachtig'", 
                     "'negentig'", "'honderd'", "'duizend'", "'miljoen'", 
                     "'miljard'", "'biljoen'", "'biljard'", "'triljoen'", 
                     "'triljard'" ]

    symbolicNames = [ "<INVALID>", "ONE", "TWO", "THREE", "FOUR", "FIVE", 
                      "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN", 
                      "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", 
                      "SEVENTEEN", "EIGHTEEN", "NINETEEN", "TWENTY", "THIRTY", 
                      "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY", 
                      "HUNDRED", "THOUSAND", "MILLION", "BILLION", "TRILION", 
                      "QUADRILION", "QUINTILION", "SEXTILION", "EN", "WS" ]

    RULE_number = 0
    RULE_whole_number = 1
    RULE_ones = 2
    RULE_tens = 3
    RULE_hundreds = 4
    RULE_prefixes = 5
    RULE_thousands = 6
    RULE_millions = 7
    RULE_billions = 8
    RULE_triljons = 9
    RULE_quadrilions = 10
    RULE_quintilions = 11
    RULE_sextilions = 12
    RULE_thousands_suffixes = 13
    RULE_millions_suffixes = 14
    RULE_billions_suffixes = 15
    RULE_triljons_suffixes = 16
    RULE_quadrilions_suffixes = 17
    RULE_quintilions_suffixes = 18
    RULE_sextilions_suffixes = 19

    ruleNames =  [ "number", "whole_number", "ones", "tens", "hundreds", 
                   "prefixes", "thousands", "millions", "billions", "triljons", 
                   "quadrilions", "quintilions", "sextilions", "thousands_suffixes", 
                   "millions_suffixes", "billions_suffixes", "triljons_suffixes", 
                   "quadrilions_suffixes", "quintilions_suffixes", "sextilions_suffixes" ]

    EOF = Token.EOF
    ONE=1
    TWO=2
    THREE=3
    FOUR=4
    FIVE=5
    SIX=6
    SEVEN=7
    EIGHT=8
    NINE=9
    TEN=10
    ELEVEN=11
    TWELVE=12
    THIRTEEN=13
    FOURTEEN=14
    FIFTEEN=15
    SIXTEEN=16
    SEVENTEEN=17
    EIGHTEEN=18
    NINETEEN=19
    TWENTY=20
    THIRTY=21
    FORTY=22
    FIFTY=23
    SIXTY=24
    SEVENTY=25
    EIGHTY=26
    NINETY=27
    HUNDRED=28
    THOUSAND=29
    MILLION=30
    BILLION=31
    TRILION=32
    QUADRILION=33
    QUINTILION=34
    SEXTILION=35
    EN=36
    WS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def whole_number(self):
            return self.getTypedRuleContext(DutchNumbers.Whole_numberContext,0)


        def EOF(self):
            return self.getToken(DutchNumbers.EOF, 0)

        def getRuleIndex(self):
            return DutchNumbers.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = DutchNumbers.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.whole_number()
            self.state = 41
            self.match(DutchNumbers.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Whole_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ones(self):
            return self.getTypedRuleContext(DutchNumbers.OnesContext,0)


        def tens(self):
            return self.getTypedRuleContext(DutchNumbers.TensContext,0)


        def hundreds(self):
            return self.getTypedRuleContext(DutchNumbers.HundredsContext,0)


        def thousands(self):
            return self.getTypedRuleContext(DutchNumbers.ThousandsContext,0)


        def millions(self):
            return self.getTypedRuleContext(DutchNumbers.MillionsContext,0)


        def billions(self):
            return self.getTypedRuleContext(DutchNumbers.BillionsContext,0)


        def triljons(self):
            return self.getTypedRuleContext(DutchNumbers.TriljonsContext,0)


        def quadrilions(self):
            return self.getTypedRuleContext(DutchNumbers.QuadrilionsContext,0)


        def quintilions(self):
            return self.getTypedRuleContext(DutchNumbers.QuintilionsContext,0)


        def sextilions(self):
            return self.getTypedRuleContext(DutchNumbers.SextilionsContext,0)


        def getRuleIndex(self):
            return DutchNumbers.RULE_whole_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhole_number" ):
                listener.enterWhole_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhole_number" ):
                listener.exitWhole_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhole_number" ):
                return visitor.visitWhole_number(self)
            else:
                return visitor.visitChildren(self)




    def whole_number(self):

        localctx = DutchNumbers.Whole_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_whole_number)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.ones()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.tens()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.hundreds()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.thousands()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.millions()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.billions()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 49
                self.triljons()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 50
                self.quadrilions()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 51
                self.quintilions()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 52
                self.sextilions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OnesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ONE(self):
            return self.getToken(DutchNumbers.ONE, 0)

        def TWO(self):
            return self.getToken(DutchNumbers.TWO, 0)

        def THREE(self):
            return self.getToken(DutchNumbers.THREE, 0)

        def FOUR(self):
            return self.getToken(DutchNumbers.FOUR, 0)

        def FIVE(self):
            return self.getToken(DutchNumbers.FIVE, 0)

        def SIX(self):
            return self.getToken(DutchNumbers.SIX, 0)

        def SEVEN(self):
            return self.getToken(DutchNumbers.SEVEN, 0)

        def EIGHT(self):
            return self.getToken(DutchNumbers.EIGHT, 0)

        def NINE(self):
            return self.getToken(DutchNumbers.NINE, 0)

        def getRuleIndex(self):
            return DutchNumbers.RULE_ones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOnes" ):
                listener.enterOnes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOnes" ):
                listener.exitOnes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOnes" ):
                return visitor.visitOnes(self)
            else:
                return visitor.visitChildren(self)




    def ones(self):

        localctx = DutchNumbers.OnesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1022) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TensContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TWENTY(self):
            return self.getToken(DutchNumbers.TWENTY, 0)

        def THIRTY(self):
            return self.getToken(DutchNumbers.THIRTY, 0)

        def FORTY(self):
            return self.getToken(DutchNumbers.FORTY, 0)

        def FIFTY(self):
            return self.getToken(DutchNumbers.FIFTY, 0)

        def SIXTY(self):
            return self.getToken(DutchNumbers.SIXTY, 0)

        def SEVENTY(self):
            return self.getToken(DutchNumbers.SEVENTY, 0)

        def EIGHTY(self):
            return self.getToken(DutchNumbers.EIGHTY, 0)

        def NINETY(self):
            return self.getToken(DutchNumbers.NINETY, 0)

        def ones(self):
            return self.getTypedRuleContext(DutchNumbers.OnesContext,0)


        def EN(self):
            return self.getToken(DutchNumbers.EN, 0)

        def TEN(self):
            return self.getToken(DutchNumbers.TEN, 0)

        def ELEVEN(self):
            return self.getToken(DutchNumbers.ELEVEN, 0)

        def TWELVE(self):
            return self.getToken(DutchNumbers.TWELVE, 0)

        def THIRTEEN(self):
            return self.getToken(DutchNumbers.THIRTEEN, 0)

        def FOURTEEN(self):
            return self.getToken(DutchNumbers.FOURTEEN, 0)

        def FIFTEEN(self):
            return self.getToken(DutchNumbers.FIFTEEN, 0)

        def SIXTEEN(self):
            return self.getToken(DutchNumbers.SIXTEEN, 0)

        def SEVENTEEN(self):
            return self.getToken(DutchNumbers.SEVENTEEN, 0)

        def EIGHTEEN(self):
            return self.getToken(DutchNumbers.EIGHTEEN, 0)

        def NINETEEN(self):
            return self.getToken(DutchNumbers.NINETEEN, 0)

        def getRuleIndex(self):
            return DutchNumbers.RULE_tens

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTens" ):
                listener.enterTens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTens" ):
                listener.exitTens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTens" ):
                return visitor.visitTens(self)
            else:
                return visitor.visitChildren(self)




    def tens(self):

        localctx = DutchNumbers.TensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tens)
        self._la = 0 # Token type
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21, 22, 23, 24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1022) != 0):
                    self.state = 57
                    self.ones()
                    self.state = 58
                    self.match(DutchNumbers.EN)


                self.state = 62
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 267386880) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(DutchNumbers.TEN)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(DutchNumbers.ELEVEN)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.match(DutchNumbers.TWELVE)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.match(DutchNumbers.THIRTEEN)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self.match(DutchNumbers.FOURTEEN)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 7)
                self.state = 68
                self.match(DutchNumbers.FIFTEEN)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 8)
                self.state = 69
                self.match(DutchNumbers.SIXTEEN)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 9)
                self.state = 70
                self.match(DutchNumbers.SEVENTEEN)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 10)
                self.state = 71
                self.match(DutchNumbers.EIGHTEEN)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 11)
                self.state = 72
                self.match(DutchNumbers.NINETEEN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HundredsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HUNDRED(self):
            return self.getToken(DutchNumbers.HUNDRED, 0)

        def ones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DutchNumbers.OnesContext)
            else:
                return self.getTypedRuleContext(DutchNumbers.OnesContext,i)


        def tens(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DutchNumbers.TensContext)
            else:
                return self.getTypedRuleContext(DutchNumbers.TensContext,i)


        def EN(self):
            return self.getToken(DutchNumbers.EN, 0)

        def getRuleIndex(self):
            return DutchNumbers.RULE_hundreds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHundreds" ):
                listener.enterHundreds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHundreds" ):
                listener.exitHundreds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHundreds" ):
                return visitor.visitHundreds(self)
            else:
                return visitor.visitChildren(self)




    def hundreds(self):

        localctx = DutchNumbers.HundredsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_hundreds)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 75
                self.ones()

            elif la_ == 2:
                self.state = 76
                self.tens()


            self.state = 79
            self.match(DutchNumbers.HUNDRED)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68987912190) != 0):
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 80
                    self.match(DutchNumbers.EN)


                self.state = 85
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 83
                    self.ones()
                    pass

                elif la_ == 2:
                    self.state = 84
                    self.tens()
                    pass




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrefixesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ones(self):
            return self.getTypedRuleContext(DutchNumbers.OnesContext,0)


        def tens(self):
            return self.getTypedRuleContext(DutchNumbers.TensContext,0)


        def hundreds(self):
            return self.getTypedRuleContext(DutchNumbers.HundredsContext,0)


        def getRuleIndex(self):
            return DutchNumbers.RULE_prefixes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefixes" ):
                listener.enterPrefixes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefixes" ):
                listener.exitPrefixes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefixes" ):
                return visitor.visitPrefixes(self)
            else:
                return visitor.visitChildren(self)




    def prefixes(self):

        localctx = DutchNumbers.PrefixesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_prefixes)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.ones()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.tens()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.hundreds()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThousandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THOUSAND(self):
            return self.getToken(DutchNumbers.THOUSAND, 0)

        def prefixes(self):
            return self.getTypedRuleContext(DutchNumbers.PrefixesContext,0)


        def thousands_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Thousands_suffixesContext,0)


        def EN(self):
            return self.getToken(DutchNumbers.EN, 0)

        def getRuleIndex(self):
            return DutchNumbers.RULE_thousands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThousands" ):
                listener.enterThousands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThousands" ):
                listener.exitThousands(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThousands" ):
                return visitor.visitThousands(self)
            else:
                return visitor.visitChildren(self)




    def thousands(self):

        localctx = DutchNumbers.ThousandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_thousands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536870910) != 0):
                self.state = 94
                self.prefixes()


            self.state = 97
            self.match(DutchNumbers.THOUSAND)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 69256347646) != 0):
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 98
                    self.match(DutchNumbers.EN)


                self.state = 101
                self.thousands_suffixes()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MillionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MILLION(self):
            return self.getToken(DutchNumbers.MILLION, 0)

        def prefixes(self):
            return self.getTypedRuleContext(DutchNumbers.PrefixesContext,0)


        def millions_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Millions_suffixesContext,0)


        def EN(self):
            return self.getToken(DutchNumbers.EN, 0)

        def getRuleIndex(self):
            return DutchNumbers.RULE_millions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMillions" ):
                listener.enterMillions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMillions" ):
                listener.exitMillions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMillions" ):
                return visitor.visitMillions(self)
            else:
                return visitor.visitChildren(self)




    def millions(self):

        localctx = DutchNumbers.MillionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_millions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536870910) != 0):
                self.state = 104
                self.prefixes()


            self.state = 107
            self.match(DutchNumbers.MILLION)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 69793218558) != 0):
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 108
                    self.match(DutchNumbers.EN)


                self.state = 111
                self.millions_suffixes()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BillionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BILLION(self):
            return self.getToken(DutchNumbers.BILLION, 0)

        def prefixes(self):
            return self.getTypedRuleContext(DutchNumbers.PrefixesContext,0)


        def billions_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Billions_suffixesContext,0)


        def EN(self):
            return self.getToken(DutchNumbers.EN, 0)

        def getRuleIndex(self):
            return DutchNumbers.RULE_billions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBillions" ):
                listener.enterBillions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBillions" ):
                listener.exitBillions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBillions" ):
                return visitor.visitBillions(self)
            else:
                return visitor.visitChildren(self)




    def billions(self):

        localctx = DutchNumbers.BillionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_billions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536870910) != 0):
                self.state = 114
                self.prefixes()


            self.state = 117
            self.match(DutchNumbers.BILLION)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 70866960382) != 0):
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 118
                    self.match(DutchNumbers.EN)


                self.state = 121
                self.billions_suffixes()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TriljonsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRILION(self):
            return self.getToken(DutchNumbers.TRILION, 0)

        def prefixes(self):
            return self.getTypedRuleContext(DutchNumbers.PrefixesContext,0)


        def triljons_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Triljons_suffixesContext,0)


        def EN(self):
            return self.getToken(DutchNumbers.EN, 0)

        def getRuleIndex(self):
            return DutchNumbers.RULE_triljons

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTriljons" ):
                listener.enterTriljons(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTriljons" ):
                listener.exitTriljons(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTriljons" ):
                return visitor.visitTriljons(self)
            else:
                return visitor.visitChildren(self)




    def triljons(self):

        localctx = DutchNumbers.TriljonsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_triljons)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536870910) != 0):
                self.state = 124
                self.prefixes()


            self.state = 127
            self.match(DutchNumbers.TRILION)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 70866960382) != 0):
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 128
                    self.match(DutchNumbers.EN)


                self.state = 131
                self.triljons_suffixes()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuadrilionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUADRILION(self):
            return self.getToken(DutchNumbers.QUADRILION, 0)

        def prefixes(self):
            return self.getTypedRuleContext(DutchNumbers.PrefixesContext,0)


        def quadrilions_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Quadrilions_suffixesContext,0)


        def EN(self):
            return self.getToken(DutchNumbers.EN, 0)

        def getRuleIndex(self):
            return DutchNumbers.RULE_quadrilions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuadrilions" ):
                listener.enterQuadrilions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuadrilions" ):
                listener.exitQuadrilions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuadrilions" ):
                return visitor.visitQuadrilions(self)
            else:
                return visitor.visitChildren(self)




    def quadrilions(self):

        localctx = DutchNumbers.QuadrilionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_quadrilions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536870910) != 0):
                self.state = 134
                self.prefixes()


            self.state = 137
            self.match(DutchNumbers.QUADRILION)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 75161927678) != 0):
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 138
                    self.match(DutchNumbers.EN)


                self.state = 141
                self.quadrilions_suffixes()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuintilionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUINTILION(self):
            return self.getToken(DutchNumbers.QUINTILION, 0)

        def prefixes(self):
            return self.getTypedRuleContext(DutchNumbers.PrefixesContext,0)


        def quintilions_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Quintilions_suffixesContext,0)


        def EN(self):
            return self.getToken(DutchNumbers.EN, 0)

        def getRuleIndex(self):
            return DutchNumbers.RULE_quintilions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuintilions" ):
                listener.enterQuintilions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuintilions" ):
                listener.exitQuintilions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuintilions" ):
                return visitor.visitQuintilions(self)
            else:
                return visitor.visitChildren(self)




    def quintilions(self):

        localctx = DutchNumbers.QuintilionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_quintilions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536870910) != 0):
                self.state = 144
                self.prefixes()


            self.state = 147
            self.match(DutchNumbers.QUINTILION)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 83751862270) != 0):
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 148
                    self.match(DutchNumbers.EN)


                self.state = 151
                self.quintilions_suffixes()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SextilionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEXTILION(self):
            return self.getToken(DutchNumbers.SEXTILION, 0)

        def prefixes(self):
            return self.getTypedRuleContext(DutchNumbers.PrefixesContext,0)


        def sextilions_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Sextilions_suffixesContext,0)


        def EN(self):
            return self.getToken(DutchNumbers.EN, 0)

        def getRuleIndex(self):
            return DutchNumbers.RULE_sextilions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSextilions" ):
                listener.enterSextilions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSextilions" ):
                listener.exitSextilions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSextilions" ):
                return visitor.visitSextilions(self)
            else:
                return visitor.visitChildren(self)




    def sextilions(self):

        localctx = DutchNumbers.SextilionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sextilions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536870910) != 0):
                self.state = 154
                self.prefixes()


            self.state = 157
            self.match(DutchNumbers.SEXTILION)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 100931731454) != 0):
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 158
                    self.match(DutchNumbers.EN)


                self.state = 161
                self.sextilions_suffixes()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Thousands_suffixesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ones(self):
            return self.getTypedRuleContext(DutchNumbers.OnesContext,0)


        def tens(self):
            return self.getTypedRuleContext(DutchNumbers.TensContext,0)


        def hundreds(self):
            return self.getTypedRuleContext(DutchNumbers.HundredsContext,0)


        def getRuleIndex(self):
            return DutchNumbers.RULE_thousands_suffixes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThousands_suffixes" ):
                listener.enterThousands_suffixes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThousands_suffixes" ):
                listener.exitThousands_suffixes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThousands_suffixes" ):
                return visitor.visitThousands_suffixes(self)
            else:
                return visitor.visitChildren(self)




    def thousands_suffixes(self):

        localctx = DutchNumbers.Thousands_suffixesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_thousands_suffixes)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.ones()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.tens()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.hundreds()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Millions_suffixesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def thousands_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Thousands_suffixesContext,0)


        def thousands(self):
            return self.getTypedRuleContext(DutchNumbers.ThousandsContext,0)


        def getRuleIndex(self):
            return DutchNumbers.RULE_millions_suffixes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMillions_suffixes" ):
                listener.enterMillions_suffixes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMillions_suffixes" ):
                listener.exitMillions_suffixes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMillions_suffixes" ):
                return visitor.visitMillions_suffixes(self)
            else:
                return visitor.visitChildren(self)




    def millions_suffixes(self):

        localctx = DutchNumbers.Millions_suffixesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_millions_suffixes)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.thousands_suffixes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.thousands()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Billions_suffixesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def millions_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Millions_suffixesContext,0)


        def millions(self):
            return self.getTypedRuleContext(DutchNumbers.MillionsContext,0)


        def getRuleIndex(self):
            return DutchNumbers.RULE_billions_suffixes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBillions_suffixes" ):
                listener.enterBillions_suffixes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBillions_suffixes" ):
                listener.exitBillions_suffixes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBillions_suffixes" ):
                return visitor.visitBillions_suffixes(self)
            else:
                return visitor.visitChildren(self)




    def billions_suffixes(self):

        localctx = DutchNumbers.Billions_suffixesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_billions_suffixes)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.millions_suffixes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.millions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Triljons_suffixesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def millions_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Millions_suffixesContext,0)


        def millions(self):
            return self.getTypedRuleContext(DutchNumbers.MillionsContext,0)


        def getRuleIndex(self):
            return DutchNumbers.RULE_triljons_suffixes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTriljons_suffixes" ):
                listener.enterTriljons_suffixes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTriljons_suffixes" ):
                listener.exitTriljons_suffixes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTriljons_suffixes" ):
                return visitor.visitTriljons_suffixes(self)
            else:
                return visitor.visitChildren(self)




    def triljons_suffixes(self):

        localctx = DutchNumbers.Triljons_suffixesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_triljons_suffixes)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.millions_suffixes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.millions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Quadrilions_suffixesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def triljons_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Triljons_suffixesContext,0)


        def triljons(self):
            return self.getTypedRuleContext(DutchNumbers.TriljonsContext,0)


        def getRuleIndex(self):
            return DutchNumbers.RULE_quadrilions_suffixes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuadrilions_suffixes" ):
                listener.enterQuadrilions_suffixes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuadrilions_suffixes" ):
                listener.exitQuadrilions_suffixes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuadrilions_suffixes" ):
                return visitor.visitQuadrilions_suffixes(self)
            else:
                return visitor.visitChildren(self)




    def quadrilions_suffixes(self):

        localctx = DutchNumbers.Quadrilions_suffixesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_quadrilions_suffixes)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.triljons_suffixes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.triljons()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Quintilions_suffixesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quadrilions_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Quadrilions_suffixesContext,0)


        def quadrilions(self):
            return self.getTypedRuleContext(DutchNumbers.QuadrilionsContext,0)


        def getRuleIndex(self):
            return DutchNumbers.RULE_quintilions_suffixes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuintilions_suffixes" ):
                listener.enterQuintilions_suffixes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuintilions_suffixes" ):
                listener.exitQuintilions_suffixes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuintilions_suffixes" ):
                return visitor.visitQuintilions_suffixes(self)
            else:
                return visitor.visitChildren(self)




    def quintilions_suffixes(self):

        localctx = DutchNumbers.Quintilions_suffixesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_quintilions_suffixes)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.quadrilions_suffixes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.quadrilions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sextilions_suffixesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quintilions_suffixes(self):
            return self.getTypedRuleContext(DutchNumbers.Quintilions_suffixesContext,0)


        def quintilions(self):
            return self.getTypedRuleContext(DutchNumbers.QuintilionsContext,0)


        def getRuleIndex(self):
            return DutchNumbers.RULE_sextilions_suffixes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSextilions_suffixes" ):
                listener.enterSextilions_suffixes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSextilions_suffixes" ):
                listener.exitSextilions_suffixes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSextilions_suffixes" ):
                return visitor.visitSextilions_suffixes(self)
            else:
                return visitor.visitChildren(self)




    def sextilions_suffixes(self):

        localctx = DutchNumbers.Sextilions_suffixesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_sextilions_suffixes)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.quintilions_suffixes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.quintilions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





