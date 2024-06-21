import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageTileViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Tile Viewer")

        self.image = None
        self.tiles = []
        self.tile_width = tk.IntVar(value=128)
        self.tile_height = tk.IntVar(value=256)
        self.tileset_name = ""

        # Create a frame to contain all widgets
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Left side: Image grid and scrollbar
        self.left_frame = tk.Frame(self.main_frame)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.left_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.left_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW)

        # Right side: Text box and buttons
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(self.right_frame, text="Tile Width:").pack()
        self.width_entry = tk.Entry(self.right_frame, textvariable=self.tile_width)
        self.width_entry.pack()

        tk.Label(self.right_frame, text="Tile Height:").pack()
        self.height_entry = tk.Entry(self.right_frame, textvariable=self.tile_height)
        self.height_entry.pack()

        self.load_button = tk.Button(self.right_frame, text="Load Image", command=self.load_image)
        self.load_button.pack()

        # Text box for displaying clicked tiles
        self.text_box = tk.Text(self.right_frame, height=10, width=40)
        self.text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the text box
        self.text_scrollbar = tk.Scrollbar(self.right_frame, command=self.text_box.yview)
        self.text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_box.config(yscrollcommand=self.text_scrollbar.set)

        # Button to create the list
        self.create_list_button = tk.Button(self.right_frame, text="Create List", command=self.create_list)
        self.create_list_button.pack()

        # Button to clear the text output
        self.clear_list_button = tk.Button(self.right_frame, text="Clear List", command=self.clear_list)
        self.clear_list_button.pack()

        # Button to clear the temporary list and unhighlight images
        self.clear_temp_list_button = tk.Button(self.right_frame, text="Clear Temp List", command=self.clear_temp_list)
        self.clear_temp_list_button.pack()

        # List to store clicked tile indices
        self.clicked_tiles = []

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.bmp")])
        if file_path:
            self.image = Image.open(file_path)
            self.tileset_name = os.path.splitext(os.path.basename(file_path))[0]
            
            # Clear existing tiles
            self.tiles.clear()
            self.clicked_tiles.clear()
            
            # Clear existing widgets from the frame
            for widget in self.frame.winfo_children():
                widget.destroy()
            
            self.split_image()

    def split_image(self):
        width, height = self.image.size
        tile_width = self.tile_width.get()
        tile_height = self.tile_height.get()
        rows = height // tile_height
        cols = width // tile_width

        self.tiles.clear()  # Clear tiles list before splitting again

        for y in range(rows):
            for x in range(cols):
                tile = self.image.crop((x * tile_width, y * tile_height,
                                        (x + 1) * tile_width, (y + 1) * tile_height))
                self.tiles.append(tile)

        self.display_tiles()
        self.canvas.update_idletasks()  # Update the canvas
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Update scrollable region

    def display_tiles(self):
        cols = 8  # Number of columns in the grid
        row = col = 0

        border_size = 2  # Adjust border size as needed
        border_color = "black"  # Adjust border color as needed

        for i, tile in enumerate(self.tiles):
            # Create a bordered version of the tile image
            bordered_tile = Image.new("RGB", (self.tile_width.get(), self.tile_height.get()), border_color)
            bordered_tile.paste(tile, (border_size, border_size))

            photo = ImageTk.PhotoImage(bordered_tile)
            label = tk.Label(self.frame, image=photo)
            label.image = photo  # Keep a reference to avoid garbage collection
            label.grid(row=row, column=col, padx=5, pady=5)

            # Display tile name at the bottom of the tile
            tile_name = f"{self.tileset_name}_{i:03d}"
            tile_name_label = tk.Label(self.frame, text=tile_name)
            tile_name_label.grid(row=row + 1, column=col, padx=5, pady=5)

            label.bind("<Button-1>", lambda event, index=i: self.toggle_highlight(event, index))

            col += 1
            if col == cols:
                col = 0
                row += 2  # Increment by 2 to leave space for the tile name label


    def toggle_highlight(self, event, index):
        if index in self.clicked_tiles:
            self.clicked_tiles.remove(index)
            self.unhighlight_tile(event.widget)
        else:
            self.clicked_tiles.append(index)
            self.highlight_tile(event.widget)

    def highlight_tile(self, label):
        label.config(highlightthickness=2, highlightbackground="blue")

    def unhighlight_tile(self, label):
        label.config(highlightthickness=0, highlightbackground="black")

    def create_list(self):
        self.text_box.delete(1.0, tk.END)  # Clear the text box
        self.text_box.insert(tk.END, "[\n")
        for index in self.clicked_tiles:
            tile_name = f"{self.tileset_name}_{index:03d}"
            self.text_box.insert(tk.END, f"    '{tile_name}',\n")
        self.text_box.insert(tk.END, "],\n")

    def clear_list(self):
        self.text_box.delete(1.0, tk.END)  # Clear the text box

    def clear_temp_list(self):
        self.clicked_tiles.clear()
        for child in self.frame.winfo_children():
            self.unhighlight_tile(child)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

def main():
    root = tk.Tk()
    app = ImageTileViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
