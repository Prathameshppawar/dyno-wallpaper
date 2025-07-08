# Dynamic Task Wallpaper 📝💻

**Keep your tasks always visible on your Windows desktop!**

This Python application automatically converts your text-based task list into a beautiful desktop wallpaper that updates in real-time. No more forgetting important tasks - they're always right there on your desktop background.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 The Problem This Solves

- **Forgetting tasks** because they're hidden in apps or files
- **Context switching** between work and task management tools
- **Cluttered desktop** with sticky notes and reminders
- **Out of sight, out of mind** syndrome with todo lists

## ✨ The Solution

Transform your Windows wallpaper into a **live task dashboard** that:
- Updates automatically when you edit a simple text file
- Displays beautifully formatted tasks with headers and bullet points
- Uses a clean, dark theme that's easy on the eyes
- Shows a timestamp of the last update
- Requires zero configuration - just edit and save!

## 🚀 How It Works

1. **Edit `tasks.txt`** with your tasks using simple markdown-like syntax
2. **Save the file** - your wallpaper updates instantly
3. **Work normally** - your tasks are always visible in the background
4. **Stay productive** - never lose track of what needs to be done

## 📋 Task Format

Simple and intuitive formatting:

```text
# Today's Priority
- Finish the presentation slides
- Review pull requests
- Call Sarah about the meeting

# This Week
- Plan the project timeline
- Update documentation
- Test the new features

# Personal
- Buy groceries
- Schedule dentist appointment
- Read for 30 minutes

You can also write regular notes without bullets
These will show up as plain text on your wallpaper
```

## 💻 Quick Start

### Prerequisites
- Windows 10/11
- Python 3.7 or higher
- pip (comes with Python)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/yourusername/dynamic-task-wallpaper.git
   cd dynamic-task-wallpaper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or use the automated setup:
   ```bash
   setup.bat
   ```

3. **Run the application**
   ```bash
   python task_wallpaper.py
   ```

4. **Edit your tasks**
   - Open `tasks.txt` in any text editor (Notepad, VS Code, etc.)
   - Add your tasks using the format shown above
   - Save the file and watch your wallpaper change!

That's it! The application will keep running and monitoring your tasks file.

## 🔧 Creating a Standalone Executable

Want to run this without Python? Create a `.exe` file:

```bash
python build_executable.py
```

This creates:
- `TaskWallpaper.exe` - Ready to run on any Windows PC
- `TaskWallpaper_Portable/` - Complete package with sample tasks

## 🎨 Customization

Edit the `task_wallpaper.py` file to customize:

- **Colors**: Change the dark theme colors
- **Fonts**: Use different fonts or sizes
- **Layout**: Adjust spacing and positioning
- **Screen Resolution**: Set your monitor's resolution
- **Text Effects**: Add shadows, outlines, or other styling

Example customizations:
```python
# Change background color
img = Image.new('RGB', (self.screen_width, self.screen_height), color='#2c3e50')

# Use different colors for headers
draw.text((x_margin, y), header_text, fill='#e74c3c', font=header_font)

# Adjust font sizes
title_font = ImageFont.truetype("arial.ttf", 36)  # Bigger title
```

## 🐛 Troubleshooting

**Wallpaper not updating?**
- Make sure you're saving the `tasks.txt` file
- Check if Windows is blocking the wallpaper change
- Try running as administrator if needed

**Script crashes or won't start?**
- Ensure Python 3.7+ is installed
- Install missing dependencies: `pip install -r requirements.txt`
- Check if antivirus is blocking the script

**Fonts look weird?**
- The script uses Arial by default, falls back to system font
- You can specify different fonts in the code

**Performance issues?**
- The file watcher is optimized to prevent excessive updates
- Close other resource-intensive applications if needed

## 🚢 Docker Support (Experimental)

For development purposes, you can run this in Docker:

```bash
docker-compose up --build
```

**Note**: GUI applications in Docker require additional X11 setup on Windows.

## 🤝 Contributing

**We'd love your help making this better!** 

This project is perfect for contributors of all skill levels. Here's how you can help:

### 🌟 Please Star This Repo!
If you find this useful, please give it a star ⭐ - it helps others discover the project!

### 💡 Feature Ideas We'd Love to See:
- **GUI settings panel** for easy customization
- **Multiple themes** (light mode, colorful themes)
- **Task categories** with different colors
- **Markdown support** for rich formatting
- **Task completion tracking** (check off completed tasks)
- **Reminder notifications** for important tasks
- **Cloud sync** to sync tasks across devices
- **Mobile companion app** to edit tasks on phone
- **Team collaboration** features
- **Productivity analytics** (track completion rates)
- **Calendar integration** 
- **Voice input** for adding tasks
- **Drag and drop** task reordering
- **Export options** (PDF, image formats)

### 🛠️ How to Contribute:
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes
4. **Test** thoroughly on Windows
5. **Commit** with clear messages (`git commit -m 'Add voice input feature'`)
6. **Push** to your branch (`git push origin feature/amazing-feature`)
7. **Open** a Pull Request

### 🎯 Good First Issues:
- Add more color themes
- Improve error handling
- Add configuration file support
- Create better sample tasks
- Write unit tests
- Improve documentation

**All skill levels welcome!** Whether you're fixing typos or adding major features, every contribution matters.

## 📈 Roadmap

- [ ] **v1.1**: GUI settings panel
- [ ] **v1.2**: Multiple theme support
- [ ] **v1.3**: Task categories and colors
- [ ] **v1.4**: Markdown formatting support
- [ ] **v1.5**: System tray integration
- [ ] **v2.0**: Cloud synchronization
- [ ] **v2.1**: Mobile companion app
- [ ] **v2.2**: Team collaboration features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python and the amazing open-source community
- Uses [Pillow](https://pillow.readthedocs.io/) for image generation
- Uses [Watchdog](https://python-watchdog.readthedocs.io/) for file monitoring
- Windows API for seamless wallpaper integration

## 💝 Support the Project

If this project helps you stay productive:

- ⭐ **Star the repository** (it really helps!)
- 🐦 **Share it** with friends and colleagues
- 🤝 **Contribute** new features or improvements
- 📝 **Write about it** on your blog or social media
- 🐛 **Report bugs** you encounter
- 💡 **Suggest features** you'd like to see

---

**Made with ❤️ for productivity enthusiasts everywhere**

*Your tasks deserve to be seen, not hidden in apps!*