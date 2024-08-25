import tkinter as tk
from tkinter import filedialog, messagebox

import deeplabcut
from threading import Thread
import os


class FileProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Pose Inferencer")

        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.frame.pack_propagate(True)

        self.input_label = tk.Label(root, text="Select File Or Folder to Process:")
        self.input_label.pack(pady=5, padx=5)

        self.input_path = tk.Entry(root, width=50)
        self.input_path.pack(pady=5, padx=5)

        self.input_button = tk.Button(
            root, text="Browse File", command=self.browse_file
        )
        self.input_button.pack(pady=5, padx=5)

        self.input_button = tk.Button(
            root, text="Browse Folder", command=self.browse_folder
        )
        self.input_button.pack(pady=5, padx=5)

        # Output Directory Selection
        self.output_label = tk.Label(root, text="Select Output Directory:")
        self.output_label.pack(pady=5, padx=5)

        self.output_path = tk.Entry(root, width=50)
        self.output_path.pack(pady=5, padx=5)

        self.output_button = tk.Button(
            root, text="Browse Output Directory", command=self.browse_output
        )
        self.output_button.pack(pady=5, padx=5)

        # Process Button
        self.process_button = tk.Button(
            root, text="Process Data", command=self.process_data
        )
        self.process_button.pack(pady=20)

    def browse_folder(self):
        file_or_folder = filedialog.askdirectory(title="Select Folder or File")

        if file_or_folder:
            self.input_path.delete(0, tk.END)
            self.input_path.insert(0, file_or_folder)

    def browse_file(self):

        file_or_folder = filedialog.askopenfilename(title="Select File")

        if file_or_folder:
            self.input_path.delete(0, tk.END)
            self.input_path.insert(0, file_or_folder)

    def browse_output(self):
        output_dir = filedialog.askdirectory(title="Select Output Directory")

        if output_dir:
            self.output_path.delete(0, tk.END)
            self.output_path.insert(0, output_dir)

    def process_data(self):
        input_path = self.input_path.get()
        output_path = self.output_path.get()

        if not input_path or not output_path:
            messagebox.showwarning(
                "Input Error", "Please select both input and output paths."
            )
            return

        # This allows inferencing to be done in the background and allow the messagebox to be responsive
        t = Thread(target=inference_videos, args=(input_path, output_path))
        t.start()

        messagebox.showinfo(
            "Inferencing Started",
            "Inferencing has started, this may take multiple minutes.",
        )


def inference_videos(input_path: str, output_path: str):

    if os.path.isdir(input_path):
        videos = [
            os.path.join(dirpath, f)
            for (dirpath, dirnames, filenames) in os.walk(input_path)
            for f in filenames
        ]
    elif os.path.isfile(input_path):
        videos = input_path
    else:
        return "Error, incorrect input path"

    deeplabcut.video_inference_superanimal(
        videos,
        "superanimal_quadruped_hrnetw32",
        dest_folder=output_path,
        plot_trajectories=True,
    )
    messagebox.showinfo(
        "Inferencing Completed",
        "Inferencing has been completed, check the output files for your results.",
    )


def main():
    root = tk.Tk()
    app = FileProcessorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
