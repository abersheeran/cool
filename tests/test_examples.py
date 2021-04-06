import os
import re
import sys
import subprocess
import tempfile
from pathlib import Path


def check_examples():
    from cool import F

    readme = Path(__file__).absolute().parent.parent / "README.md"
    sources = readme.read_text(encoding="utf8")
    current_cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as _:
        try:
            os.chdir(_)
            tmp = Path(_)
            for i, code in enumerate(
                re.findall(r"```python(?P<code>[\s\S]+?)```", sources)
            ):
                py_path = tmp / f"_{i}.py"
                py_path.write_text(code)
                print(f"Running. {i}")
                print(
                    code.splitlines()
                    | F(map, lambda line: " " * 4 + line)
                    | F("\n".join)
                )
                print("\nOutput:")
                subprocess.check_call(sys.executable + " " + str(py_path), shell=True)
                print()
        finally:
            os.chdir(current_cwd)


if __name__ == "__main__":
    check_examples()
