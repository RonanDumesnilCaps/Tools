import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import vfx_tracker as tracker


class VFXTrackerApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("VFX Tracker")
        self.create_widgets()
        self.refresh_shots()

    def create_widgets(self):
        # List of shots
        self.shot_list = tk.Listbox(self.master, width=20)
        self.shot_list.grid(row=0, column=0, rowspan=4, sticky="ns")
        self.shot_list.bind("<<ListboxSelect>>", self.on_shot_select)

        tk.Button(self.master, text="Add Shot", command=self.add_shot).grid(row=4, column=0, sticky="ew")

        # Tasks table
        self.task_tree = ttk.Treeview(self.master, columns=("name", "status"), show="headings")
        self.task_tree.heading("name", text="Task")
        self.task_tree.heading("status", text="Status")
        self.task_tree.grid(row=0, column=1, columnspan=2, sticky="nsew")

        tk.Button(self.master, text="Add Task", command=self.add_task).grid(row=1, column=1, sticky="ew")
        tk.Button(self.master, text="Update Status", command=self.update_status).grid(row=1, column=2, sticky="ew")

        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.rowconfigure(0, weight=1)

    def refresh_shots(self):
        self.data = tracker.load_data()
        self.shot_list.delete(0, tk.END)
        for shot_id in self.data.get("shots", {}):
            self.shot_list.insert(tk.END, shot_id)
        self.task_tree.delete(*self.task_tree.get_children())

    def on_shot_select(self, event=None):
        selection = self.shot_list.curselection()
        self.task_tree.delete(*self.task_tree.get_children())
        if not selection:
            return
        shot_id = self.shot_list.get(selection[0])
        for idx, task in enumerate(self.data["shots"].get(shot_id, [])):
            self.task_tree.insert("", "end", iid=str(idx), values=(task["name"], task["status"]))

    def add_shot(self):
        shot_id = simpledialog.askstring("Add Shot", "Shot ID:")
        if shot_id:
            tracker.add_shot(shot_id)
            self.refresh_shots()

    def add_task(self):
        selection = self.shot_list.curselection()
        if not selection:
            messagebox.showinfo("Info", "Select a shot first")
            return
        shot_id = self.shot_list.get(selection[0])
        task_name = simpledialog.askstring("Add Task", "Task name:")
        if task_name:
            tracker.add_task(shot_id, task_name)
            self.refresh_shots()
            self.shot_list.selection_set(selection[0])
            self.on_shot_select()

    def update_status(self):
        selection_shot = self.shot_list.curselection()
        if not selection_shot:
            messagebox.showinfo("Info", "Select a shot first")
            return
        shot_id = self.shot_list.get(selection_shot[0])
        selection_task = self.task_tree.selection()
        if not selection_task:
            messagebox.showinfo("Info", "Select a task")
            return
        task_idx = int(selection_task[0])
        status = simpledialog.askstring("Update Status", "Status (todo, in_progress, done):")
        if status not in ["todo", "in_progress", "done"]:
            messagebox.showerror("Error", "Invalid status")
            return
        tracker.update_task(shot_id, task_idx, status)
        self.refresh_shots()
        self.shot_list.selection_set(selection_shot[0])
        self.on_shot_select()


if __name__ == "__main__":
    root = tk.Tk()
    app = VFXTrackerApp(root)
    root.mainloop()
