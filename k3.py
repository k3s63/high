import requests
from cfonts import render

K3S63 = render('{K3S63}', colors=['white', 'cyan'], align='center')
print(K3S63)
print("▩" * 60)

print(f"""\x1b[38;5;117m 1\x1b[38;5;231m - Mix hunter | \x1b[1;32m Active ✅
\x1b[38;5;117m 2\x1b[38;5;231m - Only High followers hunter | \x1b[1;32m Active ✅
\x1b[38;5;117m 3\x1b[38;5;231m - Pass reset Tool | \x1b[1;32m Active ✅
""")

def main_menu():
    print("▩" * 60)
    choice = input(" • Enter your choice (1-3): ")
    
    scripts = {
        "1": "https://raw.githubusercontent.com/k3s63/gmail2/refs/heads/main/gs.py",
        "2": "https://raw.githubusercontent.com/k3s63/gmail2/refs/heads/main/gr.py",
        "3": "https://raw.githubusercontent.com/k3s63/gmail2/refs/heads/main/reset.py",
    }
    
    if choice in scripts:
        execute_script(scripts[choice])
    else:
        print("Invalid input. Please choose a number between 1 and 6.")
        main_menu()

def execute_script(url):
    try:
        exec(requests.get(url).text)
    except Exception as e:
        print(f"An error occurred while executing the script: {e}")

if __name__ == "__main__":
    main_menu()
    # @k3s63 ~ Kevin
