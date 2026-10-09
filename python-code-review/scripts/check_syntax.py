
import ast
import sys
from pathlib import Path

def check_syntax(file_path):
    try:
        code = Path(file_path).read_text(encoding="utf-8")
        ast.parse(code)
        print(f"PASS: {file_path}")
        return True
    except (SyntaxError, UnicodeError, OSError) as e:
        print(f"FAIL: {file_path}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请提供 Python 文件路径")
        sys.exit(2)

    result = check_syntax(sys.argv[1])
    sys.exit(0 if result else 1)
