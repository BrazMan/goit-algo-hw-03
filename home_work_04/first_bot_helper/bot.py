def parse_input(user_input: str) -> str:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contacts(args, contacts):
    name, phone = args
    name = name.lower()
    contacts[name] = phone
    name = name.capitalize()
    return (f"Контакт {name} з номером {phone} додано.")

def change_contact(args, contacts):
    name, phone = args
    name = name.lower()
    if name in contacts:
        contacts[name] = phone
        name = name.capitalize()
        return f"Контакт {name} оновлено новим номером {phone}."
    else:
        return f"Контакт {name} не знайдено."

def search_contact(args, contacts):
    name = args[0]
    name = name.lower()
    if name in contacts:
        name = name.capitalize()
        return f"Контакт {name}: номер телефону {contacts[name]}."
    else:
        return f"Контакт {name} не знайдено."

def main():
    print("Вас вітає помічник бот!")
    contacts = {}
    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)
        match command:
            case "exit":
                print("Вихід з програми. До побачення!")
                break
            case 'hello':
                print("Привіт! Як я можу вам допомогти?")
            case 'help':
                print("Доступні команди: hello, help, exit, add, change, phone, list")
            case 'add':
                print(add_contacts(args, contacts))
            case 'change':
                print(change_contact(args, contacts))
            case 'phone':
                print(search_contact(args, contacts))
            case 'list':
                if contacts:
                    for name, phone in contacts.items():
                        name = name.capitalize()
                        print(f"{name}: {phone}")
                else:
                    print("Список контактів порожній.")
            case _:
                print("Невідома команда. Введіть 'help' для списку доступних команд.")


if __name__ == "__main__":
    main()