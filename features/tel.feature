#language: nl

Functionaliteit: Nederlandse Getallen Parser
  Als een gebruiker van de py_dutch_numerals bibliotheek
  Wil ik Nederlandse geschreven getallen omzetten naar integers
  Zodat ik kan werken met numerieke waarden

  Abstract Scenario: Converteer eenvoudige Nederlandse getallen naar integers
    Gegeven ik heb het Nederlandse getal "<nederlands_getal>"
    Als ik het converteer naar een integer
    Dan moet het resultaat <verwacht_resultaat> zijn

    Voorbeelden:
      | nederlands_getal | verwacht_resultaat |
      | een              | 1                  |
      | twee             | 2                  |
      | drie             | 3                  |

  Abstract Scenario: Converteer 'tien'-getallen naar integers
    Gegeven ik heb het Nederlandse getal "<nederlands_getal>"
    Als ik het converteer naar een integer
    Dan moet het resultaat <verwacht_resultaat> zijn

  Voorbeelden:
      | nederlands_getal | verwacht_resultaat |
      | tien             | 10                 |
      | elf              | 11                 |
      | twaalf           | 12                 |

  Abstract Scenario: Converteer tientallen naar integers
    Gegeven ik heb het Nederlandse getal "<nederlands_getal>"
    Als ik het converteer naar een integer
    Dan moet het resultaat <verwacht_resultaat> zijn

    Voorbeelden:
      | nederlands_getal | verwacht_resultaat |
      | twintig          | 20                 |
      | dertig           | 30                 |
      | veertig          | 40                 |

  Abstract Scenario: Converteer samengestelde getallen naar integers
    Gegeven ik heb het Nederlandse getal "<nederlands_getal>"
    Als ik het converteer naar een integer
    Dan moet het resultaat <verwacht_resultaat> zijn

    Voorbeelden:
      | nederlands_getal | verwacht_resultaat |
      | eenentwintig     | 21                 |
      | tweeëndertig     | 32                 |
      | drieenvijftig    | 53                 |

  Abstract Scenario: Converteer honderdtallen naar integers
    Gegeven ik heb het Nederlandse getal "<nederlands_getal>"
    Als ik het converteer naar een integer
    Dan moet het resultaat <verwacht_resultaat> zijn

    Voorbeelden:
      | nederlands_getal  | verwacht_resultaat |
      | honderd           | 100                |
      | honderd en een    | 101                |
      | tweehonderd       | 200                |

  Abstract Scenario: Converteer duizendtallen naar integers
    Gegeven ik heb het Nederlandse getal "<nederlands_getal>"
    Als ik het converteer naar een integer
    Dan moet het resultaat <verwacht_resultaat> zijn

    Voorbeelden:
      | nederlands_getal                | verwacht_resultaat |
      | tweeduizend tweeëntwintig        | 2022               |
      | tweeduizend en tweeëntwintig     | 2022               |
      | elfhonderdeneen                  | 1101               |
      | duizend en een                   | 1001               |
      | duizend                          | 1000               |

  Abstract Scenario: Converteer miljoenen naar integers
    Gegeven ik heb het Nederlandse getal "<nederlands_getal>"
    Als ik het converteer naar een integer
    Dan moet het resultaat <verwacht_resultaat> zijn

    Voorbeelden:
      | nederlands_getal                                                   | verwacht_resultaat |
      | zeventien miljoen drieënvijftigduizend negenhonderdtachtig         | 17053980           |
      | miljoen                                                            | 1000000            |
      | twee miljoen                                                       | 2000000            |

  Abstract Scenario: Converteer miljarden naar integers
    Gegeven ik heb het Nederlandse getal "<nederlands_getal>"
    Als ik het converteer naar een integer
    Dan moet het resultaat <verwacht_resultaat> zijn

    Voorbeelden:
      | nederlands_getal | verwacht_resultaat |
      | twee miljard     | 2000000000         |
      | miljard          | 1000000000         |
      | miljard een      | 1000000001         |

  Abstract Scenario: Converteer complexe getallen naar integers
    Gegeven ik heb het Nederlandse getal "<nederlands_getal>"
    Als ik het converteer naar een integer
    Dan moet het resultaat <verwacht_resultaat> zijn

    Voorbeelden:
      | nederlands_getal                               | verwacht_resultaat |
      | drieduizend en vijfhonderdzevenenzeventig      | 3577               |
      | vijfendertighonderdenzevenenzeventig           | 3577               |

  Scenario: Ongeldige invoer leidt tot een fout
    Gegeven ik heb het Nederlandse getal "ongeldig"
    Als ik het probeer te converteren naar een integer
    Dan moet er een fout optreden met de melding "Error parsing input: Invalid number context"
