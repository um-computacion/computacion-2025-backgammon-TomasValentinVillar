# Automated Reports
## Coverage Report
```text
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
cli/__init__.py                         0      0   100%
core/__init__.py                        0      0   100%
core/backgammongame.py                117      3    97%   60, 94, 242
core/board.py                          98      1    99%   178
core/models/__init__.py                 0      0   100%
core/models/checker.py                  5      0   100%
core/models/dice.py                     8      0   100%
core/models/player.py                  15      0   100%
core/services/__init__.py               0      0   100%
core/services/dice_manager.py          36      2    94%   93, 102
core/services/move_calculator.py       64      5    92%   72, 99, 105, 127-128
core/validators/__init__.py             0      0   100%
core/validators/move_validator.py      23      6    74%   56-66
core/validators/rule_validator.py      39      7    82%   56, 76, 113-117
test/__init__.py                        0      0   100%
test/test_backgammongame.py           396      1    99%   639
test/test_board.py                    132      0   100%
test/test_checker.py                    9      0   100%
test/test_dice.py                      30      0   100%
test/test_dice_manager.py              41      1    98%   67
test/test_move_claculator.py           71      1    99%   102
test/test_move_validator.py            36      1    97%   61
test/test_player.py                    20      0   100%
test/test_rule_validator.py            52      1    98%   85
-----------------------------------------------------------------
TOTAL                                1192     29    98%

```
## Pylint Report
```text
************* Module computacion-2025-backgammon-TomasValentinVillar.core.backgammongame
core/backgammongame.py:20:0: R0902: Too many instance attributes (9/7) (too-many-instance-attributes)
core/backgammongame.py:25:4: R0913: Too many arguments (6/5) (too-many-arguments)
core/backgammongame.py:25:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
core/backgammongame.py:209:11: C1803: "self.__dice_manager__.obtener_dados_disponibles(...) == []" can be simplified to "not self.__dice_manager__.obtener_dados_disponibles(...)", if it is strictly a sequence, as an empty list is falsey (use-implicit-booleaness-not-comparison)
************* Module computacion-2025-backgammon-TomasValentinVillar.core.models.checker
core/models/checker.py:5:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module computacion-2025-backgammon-TomasValentinVillar.core.validators.rule_validator
core/validators/rule_validator.py:12:4: R0913: Too many arguments (6/5) (too-many-arguments)
core/validators/rule_validator.py:12:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
************* Module computacion-2025-backgammon-TomasValentinVillar.core.services.dice_manager
core/services/dice_manager.py:83:0: C0303: Trailing whitespace (trailing-whitespace)
************* Module computacion-2025-backgammon-TomasValentinVillar.core.services.move_calculator
core/services/move_calculator.py:109:4: R0913: Too many arguments (6/5) (too-many-arguments)
core/services/move_calculator.py:109:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
core/services/move_calculator.py:119:16: C0415: Import outside toplevel (core.models.dice.Dice) (import-outside-toplevel)
************* Module computacion-2025-backgammon-TomasValentinVillar.cli.cli
cli/cli.py:61:0: C0301: Line too long (109/100) (line-too-long)
cli/cli.py:63:0: C0301: Line too long (165/100) (line-too-long)
cli/cli.py:68:0: C0301: Line too long (166/100) (line-too-long)
cli/cli.py:76:0: C0301: Line too long (165/100) (line-too-long)
cli/cli.py:45:4: C0116: Missing function or method docstring (missing-function-docstring)
cli/cli.py:45:4: R0912: Too many branches (13/12) (too-many-branches)

-----------------------------------
Your code has been rated at 9.65/10


```
