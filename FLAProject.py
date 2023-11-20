import tkinter as tk

def is_ambiguous(cfg):
    def derive_strings(productions, non_terminal, max_length):
        if max_length == 0:
            return set()

        derived_strings = set()

        for production in productions:
            current_string = ""
            for symbol in production:
                if symbol in cfg:
                    # Recursively derive strings for non-terminals
                    derived_strings |= derive_strings(cfg[symbol], symbol, max_length - 1)
                else:
                    current_string += symbol

            derived_strings.add(current_string)

        return derived_strings

    start_symbol = list(cfg.keys())[0]
    max_length = 10  # Adjust the maximum length as needed

    # Derive strings for the start symbol
    strings1 = derive_strings(cfg[start_symbol], start_symbol, max_length)

    # Derive strings for the start symbol after adding a new production
    new_production = 'X'  # A new non-terminal
    cfg[start_symbol].append(new_production)
    strings2 = derive_strings(cfg[start_symbol], start_symbol, max_length)
    del cfg[start_symbol][-1]  # Remove the added production

    # If there are common strings in both sets, the grammar is ambiguous
    return bool(strings1 & strings2)

def check_ambiguity():
    if is_ambiguous(cfg):
        result_label.config(text="Ambiguous")
    else:
        result_label.config(text="Not Ambiguous")

# Example CFG
# cfg = {
#     'S': ['AB', 'BC', 'a', 'b', 'c'],
#     'A': ['aA', ''],
#     'B': ['bB', ''],
#     'C': ['cC', ''],
# }

# Example non-ambiguous CFG
cfg = {
    'S': ['AB', 'a', 'b'],
    'A': ['aA', ''],
    'B': ['bB', 'c', ''],
}

# Create the main window
root = tk.Tk()
root.title("CFG Ambiguity Checker")

# Create a label for the result
result_label = tk.Label(root, text="")
result_label.pack()

# Create a button to check ambiguity
check_button = tk.Button(root, text="Check Ambiguity", command=check_ambiguity)
check_button.pack()

# Start the main event loop
root.mainloop()
