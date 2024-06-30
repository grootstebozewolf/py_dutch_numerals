/**
 * Dutch Number Parser
 * 
 * Licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
 * You may obtain a copy of the License at https://creativecommons.org/licenses/by-sa/4.0/
 */
 parser grammar DutchNumbers;

options { tokenVocab=DutchNumbersLexer; }

number
    : whole_number EOF
    ;

whole_number
    : ones
    | tens
    | hundreds
    | thousands
    | millions
    | billions
    | triljons
    | quadrilions
    | quintilions
    | sextilions
    ;

ones
    : ONE
    | TWO
    | THREE
    | FOUR
    | FIVE
    | SIX
    | SEVEN
    | EIGHT
    | NINE
    ;

tens
    : (ones EN)? (TWENTY | THIRTY | FORTY | FIFTY | SIXTY | SEVENTY | EIGHTY | NINETY)
    | TEN
    | ELEVEN
    | TWELVE
    | THIRTEEN
    | FOURTEEN
    | FIFTEEN
    | SIXTEEN
    | SEVENTEEN
    | EIGHTEEN
    | NINETEEN
    ;

hundreds
    : (ones|tens)? HUNDRED (EN? (ones|tens))?
    ;

prefixes
    : ones|tens|hundreds
    ;

thousands
    : prefixes? THOUSAND (EN? thousands_suffixes)?
    ;

millions
    : prefixes? MILLION (EN? millions_suffixes)?
    ;

billions
    : prefixes? BILLION (EN? billions_suffixes)?
    ;

triljons
    : prefixes? TRILION (EN? triljons_suffixes)?
    ;

quadrilions
    : prefixes? QUADRILION (EN? quadrilions_suffixes)?
    ;

quintilions
    : prefixes? QUINTILION (EN? quintilions_suffixes)?
    ;

sextilions
    : prefixes? SEXTILION (EN? sextilions_suffixes)?
    ;

thousands_suffixes
    : ones|tens|hundreds
    ;

millions_suffixes
    : thousands_suffixes | thousands
    ;

billions_suffixes
    : millions_suffixes | millions
    ;

triljons_suffixes
    : millions_suffixes | millions
    ;
    
quadrilions_suffixes
    : triljons_suffixes | triljons
    ;

quintilions_suffixes
    : quadrilions_suffixes | quadrilions
    ;
    
sextilions_suffixes
    : quintilions_suffixes | quintilions
    ;