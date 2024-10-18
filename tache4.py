def get_user_guess(entry):
    return int(entry.get())

def display_message(label, message):
    label.config(text=message)