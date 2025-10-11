# Automated Reports
## Coverage Report
```text
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
cli/__init__.py                         0      0   100%
core/__init__.py                        0      0   100%
core/backgammongame.py                117      3    97%   52, 75, 201
core/board.py                          98      4    96%   112, 134-137
core/models/__init__.py                 0      0   100%
core/models/checker.py                  5      0   100%
core/models/dice.py                     8      0   100%
core/models/player.py                  15      0   100%
core/services/__init__.py               0      0   100%
core/services/dice_manager.py          36      2    94%   89, 98
core/services/move_calculator.py       64      5    92%   69, 96, 102, 124-125
core/test_checker.py                    9      0   100%
core/test_dice_manager.py              41      1    98%   67
core/test_move_claculator.py           71      1    99%   102
core/test_move_validator.py            36      1    97%   61
core/test_player.py                    20      0   100%
core/test_rule_validator.py            52      1    98%   85
core/validators/__init__.py             0      0   100%
core/validators/move_validator.py      23      6    74%   53-63
core/validators/rule_validator.py      39      7    82%   54, 74, 112-116
-----------------------------------------------------------------
TOTAL                                 634     31    95%

```
## Pylint Report
```text
************* Module main.py
main.py:1:0: F0001: No module named main.py (fatal)
************* Module test.py
test.py:1:0: F0001: No module named test.py (fatal)

```
