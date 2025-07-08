import os
import time
import ctypes
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading

class TaskWallpaperGenerator:
    def __init__(self, tasks_file="tasks.txt", wallpaper_path="task_wallpaper.png"):
        self.tasks_file = tasks_file
        self.wallpaper_path = wallpaper_path
        self.screen_width = 1920  # Adjust to your screen resolution
        self.screen_height = 1080
        
        # Create tasks file if it doesn't exist
        if not os.path.exists(tasks_file):
            with open(tasks_file, 'w') as f:
                f.write("# My Tasks\n")
                f.write("- Edit this file to update your wallpaper\n")
                f.write("- Tasks will appear on your desktop\n")
                f.write("- Use # for headers and - for tasks\n")
        
        # Generate initial wallpaper
        self.generate_wallpaper()
        self.set_wallpaper()
        
    def read_tasks(self):
        """Read tasks from the text file"""
        try:
            with open(self.tasks_file, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except Exception as e:
            return f"Error reading tasks: {str(e)}"
    
    def generate_wallpaper(self):
        """Generate wallpaper image from tasks"""
        # Create image with dark background
        img = Image.new('RGB', (self.screen_width, self.screen_height), color='#1a1a1a')
        draw = ImageDraw.Draw(img)
        
        # Try to load a nice font, fall back to default if not available
        try:
            title_font = ImageFont.truetype("arial.ttf", 32)
            header_font = ImageFont.truetype("arial.ttf", 24)
            task_font = ImageFont.truetype("arial.ttf", 18)
        except:
            title_font = ImageFont.load_default()
            header_font = ImageFont.load_default()
            task_font = ImageFont.load_default()
        
        # Read tasks content
        content = self.read_tasks()
        lines = content.split('\n')
        
        # Starting position
        y = 50
        x_margin = 50
        
        # Title
        draw.text((x_margin, y), "My Tasks", fill='#ffffff', font=title_font)
        y += 60
        
        # Process each line
        for line in lines:
            if y > self.screen_height - 100:  # Don't go too far down
                break
                
            line = line.strip()
            if not line:
                y += 10
                continue
                
            if line.startswith('#'):
                # Header
                header_text = line.lstrip('#').strip()
                draw.text((x_margin, y), header_text, fill='#4a9eff', font=header_font)
                y += 35
            elif line.startswith('-'):
                # Task item
                task_text = line.lstrip('-').strip()
                draw.text((x_margin + 20, y), f"• {task_text}", fill='#e0e0e0', font=task_font)
                y += 25
            else:
                # Regular text
                draw.text((x_margin, y), line, fill='#cccccc', font=task_font)
                y += 25
        
        # Add timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        draw.text((self.screen_width - 250, self.screen_height - 30), 
                 f"Updated: {timestamp}", fill='#666666', font=task_font)
        
        # Save image
        img.save(self.wallpaper_path)
        print(f"Wallpaper generated: {self.wallpaper_path}")
    
    def set_wallpaper(self):
        """Set the generated image as Windows wallpaper"""
        try:
            # Convert to absolute path
            abs_path = os.path.abspath(self.wallpaper_path)
            
            # Set wallpaper using Windows API
            ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)
            print(f"Wallpaper set to: {abs_path}")
        except Exception as e:
            print(f"Error setting wallpaper: {str(e)}")

class TaskFileHandler(FileSystemEventHandler):
    def __init__(self, wallpaper_generator):
        self.wallpaper_generator = wallpaper_generator
        self.last_modified = 0
        
    def on_modified(self, event):
        if event.is_directory:
            return
            
        if event.src_path.endswith(self.wallpaper_generator.tasks_file):
            # Debounce rapid file changes
            current_time = time.time()
            if current_time - self.last_modified < 1:
                return
            self.last_modified = current_time
            
            print("Tasks file changed, updating wallpaper...")
            time.sleep(0.5)  # Small delay to ensure file is fully written
            self.wallpaper_generator.generate_wallpaper()
            self.wallpaper_generator.set_wallpaper()

def main():
    print("Dynamic Task Wallpaper Generator")
    print("=" * 40)
    
    # Create wallpaper generator
    generator = TaskWallpaperGenerator()
    
    # Set up file watcher
    event_handler = TaskFileHandler(generator)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    observer.start()
    
    print(f"Watching {generator.tasks_file} for changes...")
    print("Edit the tasks file to update your wallpaper automatically!")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopping wallpaper generator...")
    
    observer.join()

if __name__ == "__main__":
    main()