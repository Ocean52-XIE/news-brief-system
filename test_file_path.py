#!/usr/bin/env python3
import os

print(f"1. __file__: {__file__}")
print(f"2. abspath(__file__): {os.path.abspath(__file__)}")
print(f"3. dirname(abspath(__file__)): {os.path.dirname(os.path.abspath(__file__))}")
print(f"4. 当前目录: {os.getcwd()}")

# 切换目录
os.chdir("/tmp")
print(f"\n5. 切换后当前目录: {os.getcwd()}")
print(f"6. __file__: {__file__}")
print(f"7. abspath(__file__): {os.path.abspath(__file__)}")
print(f"8. dirname(abspath(__file__)): {os.path.dirname(os.path.abspath(__file__))}")