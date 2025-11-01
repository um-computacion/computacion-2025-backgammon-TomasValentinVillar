# Automated Reports
## Coverage Report
```text
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
cli/__init__.py                         0      0   100%
cli/cli.py                             87      6    93%   81-83, 99, 117-118
core/__init__.py                        0      0   100%
core/backgammongame.py                127      4    97%   77-79, 100, 264
core/board.py                          98      1    99%   178
core/models/__init__.py                 0      0   100%
core/models/checker.py                  5      0   100%
core/models/dice.py                     8      0   100%
core/models/player.py                  15      0   100%
core/services/__init__.py               0      0   100%
core/services/dice_manager.py          26      2    92%   71, 89
core/services/move_calculator.py       64     12    81%   58, 67, 86, 123-124, 127-139
core/validators/__init__.py             0      0   100%
core/validators/move_validator.py      23      6    74%   56-66
core/validators/rule_validator.py      60      7    88%   65-67, 100-102, 110
pygame_ui/__init__.py                   0      0   100%
pygame_ui/board_adapter.py             15      0   100%
test/__init__.py                        0      0   100%
-----------------------------------------------------------------
TOTAL                                 528     38    93%

```
## Pylint Report
```text
************* Module core.backgammongame
core/backgammongame.py:257:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammongame.py:265:27: C0303: Trailing whitespace (trailing-whitespace)
************* Module core.models.checker
core/models/checker.py:5:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.services.move_calculator
core/services/move_calculator.py:106:4: R0913: Too many arguments (6/5) (too-many-arguments)
core/services/move_calculator.py:106:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
************* Module cli.cli
cli/cli.py:68:0: C0301: Line too long (109/100) (line-too-long)
cli/cli.py:70:0: C0301: Line too long (165/100) (line-too-long)
cli/cli.py:74:0: C0301: Line too long (112/100) (line-too-long)
cli/cli.py:76:0: C0301: Line too long (166/100) (line-too-long)
cli/cli.py:85:0: C0301: Line too long (165/100) (line-too-long)
cli/cli.py:90:0: C0301: Line too long (112/100) (line-too-long)
cli/cli.py:46:4: R0912: Too many branches (15/12) (too-many-branches)
cli/cli.py:46:4: R0915: Too many statements (58/50) (too-many-statements)
************* Module pygame_ui.pygameui
pygame_ui/pygameui.py:265:0: C0301: Line too long (110/100) (line-too-long)
pygame_ui/pygameui.py:297:0: C0301: Line too long (103/100) (line-too-long)
pygame_ui/pygameui.py:323:0: C0301: Line too long (105/100) (line-too-long)
pygame_ui/pygameui.py:327:0: C0301: Line too long (101/100) (line-too-long)
pygame_ui/pygameui.py:329:0: C0301: Line too long (104/100) (line-too-long)
pygame_ui/pygameui.py:360:0: C0301: Line too long (111/100) (line-too-long)
pygame_ui/pygameui.py:741:0: C0301: Line too long (103/100) (line-too-long)
pygame_ui/pygameui.py:781:0: C0301: Line too long (103/100) (line-too-long)
pygame_ui/pygameui.py:799:70: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/pygameui.py:19:0: R0914: Too many local variables (17/15) (too-many-locals)
pygame_ui/pygameui.py:60:29: E1101: Module 'pygame' has no 'QUIT' member (no-member)
pygame_ui/pygameui.py:63:29: E1101: Module 'pygame' has no 'KEYDOWN' member (no-member)
pygame_ui/pygameui.py:64:32: E1101: Module 'pygame' has no 'K_UP' member (no-member)
pygame_ui/pygameui.py:66:34: E1101: Module 'pygame' has no 'K_DOWN' member (no-member)
pygame_ui/pygameui.py:68:34: E1101: Module 'pygame' has no 'K_RETURN' member (no-member)
pygame_ui/pygameui.py:72:34: E1101: Module 'pygame' has no 'K_ESCAPE' member (no-member)
pygame_ui/pygameui.py:39:8: W0612: Unused variable 'colores' (unused-variable)
pygame_ui/pygameui.py:78:0: R0914: Too many local variables (18/15) (too-many-locals)
pygame_ui/pygameui.py:136:29: E1101: Module 'pygame' has no 'QUIT' member (no-member)
pygame_ui/pygameui.py:139:29: E1101: Module 'pygame' has no 'KEYDOWN' member (no-member)
pygame_ui/pygameui.py:140:32: E1101: Module 'pygame' has no 'K_ESCAPE' member (no-member)
pygame_ui/pygameui.py:143:32: E1101: Module 'pygame' has no 'K_RETURN' member (no-member)
pygame_ui/pygameui.py:155:34: E1101: Module 'pygame' has no 'K_BACKSPACE' member (no-member)
pygame_ui/pygameui.py:78:0: R0912: Too many branches (15/12) (too-many-branches)
pygame_ui/pygameui.py:88:4: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
pygame_ui/pygameui.py:166:0: R0914: Too many local variables (38/15) (too-many-locals)
pygame_ui/pygameui.py:194:4: E1101: Module 'pygame' has no 'init' member (no-member)
pygame_ui/pygameui.py:208:12: E1101: Module 'pygame' has no 'quit' member (no-member)
pygame_ui/pygameui.py:245:29: E1101: Module 'pygame' has no 'QUIT' member (no-member)
pygame_ui/pygameui.py:246:20: E1101: Module 'pygame' has no 'quit' member (no-member)
pygame_ui/pygameui.py:249:31: E1101: Module 'pygame' has no 'KEYDOWN' member (no-member)
pygame_ui/pygameui.py:250:33: E1101: Module 'pygame' has no 'K_ESCAPE' member (no-member)
pygame_ui/pygameui.py:250:50: E1101: Module 'pygame' has no 'K_q' member (no-member)
pygame_ui/pygameui.py:253:34: E1101: Module 'pygame' has no 'K_r' member (no-member)
pygame_ui/pygameui.py:257:34: E1101: Module 'pygame' has no 'K_SPACE' member (no-member)
pygame_ui/pygameui.py:204:4: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
pygame_ui/pygameui.py:272:31: E1101: Module 'pygame' has no 'MOUSEBUTTONDOWN' member (no-member)
pygame_ui/pygameui.py:204:4: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
pygame_ui/pygameui.py:312:42: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
pygame_ui/pygameui.py:204:4: R1702: Too many nested blocks (11/5) (too-many-nested-blocks)
pygame_ui/pygameui.py:204:4: R1702: Too many nested blocks (9/5) (too-many-nested-blocks)
pygame_ui/pygameui.py:166:0: R0912: Too many branches (47/12) (too-many-branches)
pygame_ui/pygameui.py:166:0: R0915: Too many statements (162/50) (too-many-statements)
pygame_ui/pygameui.py:450:0: R0914: Too many local variables (25/15) (too-many-locals)
pygame_ui/pygameui.py:450:0: R0912: Too many branches (13/12) (too-many-branches)
pygame_ui/pygameui.py:450:0: R0915: Too many statements (53/50) (too-many-statements)
pygame_ui/pygameui.py:592:41: W0613: Unused argument 'font' (unused-argument)
pygame_ui/pygameui.py:684:0: R0914: Too many local variables (21/15) (too-many-locals)
pygame_ui/pygameui.py:684:40: W0613: Unused argument 'font' (unused-argument)
pygame_ui/pygameui.py:703:4: W0612: Unused variable 'margin' (unused-variable)
************* Module pygame_ui.board_adapter
pygame_ui/board_adapter.py:7:0: R0903: Too few public methods (1/2) (too-few-public-methods)

-----------------------------------
Your code has been rated at 8.44/10


```
