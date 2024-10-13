import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Simulated video data
VIDEOS = [
    {"title": "CDU Danala Campus Tour", "length": "12:34"},
    {"title": "OOP tutorial in python", "length": "10:20"},
    {"title": "Tkinter gui tutorial", "length": "8:45"},
    {"title": "Sunset at Mindil beach", "length": "15:30"},
    {"title": "Machine Learning Fundamentals", "length": "20:10"},
]

# BasicApp class sets up the basic window (Inheritance)
class BasicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Youtube alternative")
        self.root.geometry("900x500")
        self.root.configure(bg="lightgray")

        # Create style
        self.style = ttk.Style(self.root)
        self.style.configure("TButton", font=("Helvetica", 12), padding=6)
        self.style.configure("TLabel", font=("Helvetica", 14), padding=10)
        self.style.configure("TFrame", background="lightgray")
        self.style.configure("TListbox", font=("Helvetica", 12))

# VideoPlayer class handles the "video player" area (Encapsulation)
class VideoPlayer:
    def __init__(self, parent):
        self.parent = parent
        self.player_frame = ttk.Frame(self.parent)
        self.player_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.current_video_label = ttk.Label(self.player_frame, text="Select a video to play", background="black", foreground="white", font=("Arial", 16))
        self.current_video_label.pack(pady=20, expand=True, fill=tk.BOTH)

    def play_video(self, video_title):
        # Visual feedback for playing video
        self.current_video_label.config(text=f"Playing: {video_title}")

# VideoList class handles the video listing (Polymorphism: can be extended later)
class VideoList:
    def __init__(self, parent, player):
        self.parent = parent
        self.player = player

        self.list_frame = ttk.Frame(self.parent)
        self.list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.label = ttk.Label(self.list_frame, text="Videos")
        self.label.pack(pady=5)

        # Customizing the Listbox using ttk
        self.video_listbox = tk.Listbox(self.list_frame, height=15, font=("Arial", 12), selectbackground="lightblue", relief="flat", borderwidth=0)
        self.video_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the video list
        self.scrollbar = ttk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.video_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.video_listbox.yview)

        self.populate_videos()

        self.video_listbox.bind("<<ListboxSelect>>", self.on_video_select)

    def populate_videos(self):
        # Populate the video list with titles
        for video in VIDEOS:
            self.video_listbox.insert(tk.END, f"{video['title']} ({video['length']})")

    def on_video_select(self, event):
        # Play selected video
        selected_index = self.video_listbox.curselection()
        if selected_index:
            video_title = self.video_listbox.get(selected_index).split(" (")[0]
            self.player.play_video(video_title)

# Decorator example: Logging function calls
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} was called.")
        return func(*args, **kwargs)
    return wrapper

# Search bar with decorator
class SearchBar:
    def __init__(self, parent, video_list):
        self.parent = parent
        self.video_list = video_list
        self.search_frame = ttk.Frame(self.parent)
        self.search_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.search_label = ttk.Label(self.search_frame, text="Search:")
        self.search_label.pack(side=tk.LEFT, padx=5)

        self.search_entry = ttk.Entry(self.search_frame, font=("Arial", 12))
        self.search_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search_videos)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = ttk.Button(self.search_frame, text="Reset", command=self.reset_videos)
        self.reset_button.pack(side=tk.LEFT, padx=5)

    @log_function_call
    def search_videos(self):
        # Search functionality: Filtering the list based on search
        query = self.search_entry.get().lower()
        if query:
            filtered_videos = [video for video in VIDEOS if query in video["title"].lower()]
            self.video_list.video_listbox.delete(0, tk.END)  # Clear the listbox
            for video in filtered_videos:
                self.video_list.video_listbox.insert(tk.END, f"{video['title']} ({video['length']})")
        else:
            messagebox.showinfo("Search", "Please enter a search term.")

    @log_function_call
    def reset_videos(self):
        # Reset the video list to display all videos
        self.search_entry.delete(0, tk.END)
        self.video_list.video_listbox.delete(0, tk.END)
        self.video_list.populate_videos()

# Main application class (Multiple Inheritance: Combines VideoPlayer, VideoList, and BasicApp)
class YouTubeApp(BasicApp):
    def __init__(self, root):
        super().__init__(root)

        # Video Player section
        self.video_player = VideoPlayer(self.root)

        # Video List section
        self.video_list = VideoList(self.root, self.video_player)

        # Search bar
        self.search_bar = SearchBar(self.root, self.video_list)

# Custom app with overriding (Method Overriding: Extending the base behavior)
class CYT(YouTubeApp):
    def __init__(self, root):
        super().__init__(root)

    # Overriding play_video to add more functionality
    def play_video(self, video_title):
        super().play_video(video_title)
        # Adding custom behavior such as logging or analytics
        print(f"Video {video_title} was played.")
