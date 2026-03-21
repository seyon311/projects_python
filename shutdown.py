import os

input("Press Enter to shutdown YOUR computer, It'll ask you to confirm, if you want to cancel just type N and press Enter")
confirmation = input("Are you sure? (Y/N), WARNING: This will shutdown your computer immediately without any confirmation. Make sure to save all your work before proceeding.")
if confirmation.lower() == "y":
    os.system("shutdown /s /t 0")