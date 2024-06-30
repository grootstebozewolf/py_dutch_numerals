/**
 * Dutch Number Parser
 * 
 * Licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
 * You may obtain a copy of the License at https://creativecommons.org/licenses/by-sa/4.0/
 */
 lexer grammar DutchNumbersLexer;

ONE: 'een';
TWO: 'twee';
THREE: 'drie';
FOUR: 'vier';
FIVE: 'vijf';
SIX: 'zes';
SEVEN: 'zeven';
EIGHT: 'acht';
NINE: 'negen';
TEN: 'tien';
ELEVEN: 'elf';
TWELVE: 'twaalf';
THIRTEEN: 'dertien';
FOURTEEN: 'veertien';
FIFTEEN: 'vijftien';
SIXTEEN: 'zestien';
SEVENTEEN: 'zeventien';
EIGHTEEN: 'achttien';
NINETEEN: 'negentien';
TWENTY: 'twintig';
THIRTY: 'dertig';
FORTY: 'veertig';
FIFTY: 'vijftig';
SIXTY: 'zestig';
SEVENTY: 'zeventig';
EIGHTY: 'tachtig';
NINETY: 'negentig';
HUNDRED: 'honderd';
THOUSAND: 'duizend';
MILLION: 'miljoen';
BILLION: 'miljard';
TRILION: 'biljoen';
QUADRILION: 'biljard';
QUINTILION: 'triljoen';
SEXTILION: 'triljard';
EN: 'en'|'ën';

WS          : [ \t\r\n]+ -> skip ; // Skip whitespace
