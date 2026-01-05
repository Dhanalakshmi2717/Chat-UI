import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Chat UI with Document Upload")
root.geometry("900x500")
root.configure(bg="#0b0d17")


left = tk.Frame(root, width=220, bg="#141625")
left.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(
    left,
    text="Document Upload",
    bg="#141625",
    fg="white",
    font=("Arial", 13, "bold")
).pack(pady=20)

file_label = tk.Label(
    left,
    text="No file selected",
    bg="#141625",
    fg="#aaaaaa",
    wraplength=180
)
file_label.pack(pady=10)

def upload_file():
    file = filedialog.askopenfilename(
        filetypes=[("All Files", "*.*")]
    )
    if file:
        file_label.config(text=file)
        messagebox.showinfo("Uploaded", "File uploaded successfully!")

tk.Button(
    left,
    text="Upload File",
    command=upload_file,
    bg="#1f2235",
    fg="white",
    relief="flat",
    padx=15,
    pady=8
).pack(pady=10)


right = tk.Frame(root, bg="#0b0d17")
right.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

tk.Label(
    right,
    text="Chat Interface",
    bg="#0b0d17",
    fg="white",
    font=("Arial", 20, "bold")
).pack(pady=20)


chat_box = tk.Text(
    right,
    bg="#0b0d17",
    fg="white",
    font=("Arial", 12),
    relief="flat"
)
chat_box.pack(padx=30, pady=10, fill=tk.BOTH, expand=True)
chat_box.insert(tk.END, "Bot: Hello How can I help you?\n\n")
chat_box.config(state="disabled")

bottom = tk.Frame(right, bg="#0b0d17")
bottom.pack(fill=tk.X, pady=15)

msg_entry = tk.Entry(
    bottom,
    font=("Arial", 12),
    bg="#1a1c2c",
    fg="white",
    insertbackground="white",
    relief="flat"
)
msg_entry.pack(side=tk.LEFT, padx=30, fill=tk.X, expand=True, ipady=8)

def send_msg():
    msg = msg_entry.get()
    if msg.strip() == "":
        return
    chat_box.config(state="normal")
    chat_box.insert(tk.END, f"You: {msg}\n")
    chat_box.insert(tk.END, "Bot: Message received \n\n")
    chat_box.config(state="disabled")
    chat_box.see(tk.END)
    msg_entry.delete(0, tk.END)

welcome = tk.Label(
    text="Welcome to AI Chat Assistant\nStart a conversation by typing a message below",
    bg="#343541",
    fg="#bdbec2",
    font=("Arial", 12),
    justify="center"
)
welcome.pack(pady=80)

tk.Button(
    bottom,
    text="Send",
    command=send_msg,
    bg="#ff2d55",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="flat",
    padx=15,
    pady=6
).pack(side=tk.RIGHT, padx=30)

send_btn = tk.Button(
    bottom,
    text="Send",
    command=send_msg,
    bg="#40414f",
    fg="white",
    font=("Arial", 12),
    relief="flat",
    padx=20,
    pady=8
)
send_btn.pack(side=tk.RIGHT, padx=80)

root.mainloop()