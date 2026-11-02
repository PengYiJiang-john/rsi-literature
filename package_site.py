#!/usr/bin/env python3
"""Create a self-contained GitHub upload archive after a successful local build."""
from pathlib import Path
import argparse
import subprocess
import sys
import zipfile

HERE=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=HERE/'rsi-literature-github.zip');a=p.parse_args()
    subprocess.run([sys.executable,str(HERE/'build_site.py')],check=True)
    subprocess.run([sys.executable,str(HERE/'validate_site.py')],check=True)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(a.output,'w',zipfile.ZIP_DEFLATED) as z:
        for folder in ['.github','assets','sources','dist']:
            for file in sorted((HERE/folder).rglob('*')):
                if file.is_file():z.write(file,file.relative_to(HERE))
        for name in ['README.md','.gitignore','build_site.py','validate_site.py','package_site.py','validation.json']:
            z.write(HERE/name,name)
    print(a.output)

if __name__=='__main__':main()
