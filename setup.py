from cx_Freeze import setup, Executable
import sys
import os

setup(
    name = "votre_programme",
    version = "1",
    description = "Votre programme",
    executables = [Executable("test.py")],
)