#!/usr/bin/env python3
"""
Build script to create executable for Dynamic Task Wallpaper
Run this script to create a standalone Windows executable
"""

import os
import sys
import subprocess
import shutil

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        return True
    except ImportError:
        return False

def install_pyinstaller():
    """Install PyInstaller"""
    print("Installing PyInstaller...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def create_executable():
    """Create the executable using PyInstaller"""
    print("Creating executable...")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single file executable
        "--windowed",                   # No console window
        "--name", "TaskWallpaper",      # Executable name
        "--icon", "icon.ico",           # Icon file (if available)
        "--add-data", "tasks.txt;.",    # Include tasks file
        "--hidden-import", "PIL._tkinter_finder",  # Include PIL dependencies
        "task_wallpaper.py"
    ]
    
    # Remove icon parameter if icon file doesn't exist
    if not os.path.exists("icon.ico"):
        cmd.remove("--icon")
        cmd.remove("icon.ico")
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executable created successfully!")
        print("📁 Find your executable in the 'dist' folder")
        
        # Create a portable package
        create_portable_package()
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating executable: {e}")
        sys.exit(1)

def create_portable_package():
    """Create a portable package with executable and sample files"""
    print("Creating portable package...")
    
    # Create package directory
    package_dir = "TaskWallpaper_Portable"
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    os.makedirs(package_dir)
    
    # Copy executable
    shutil.copy("dist/TaskWallpaper.exe", package_dir)
    
    # Create sample tasks file
    sample_tasks = """# My Daily Tasks
- Review emails
- Complete project work
- Team meeting at 2 PM

# This Week
- Plan next sprint
- Update documentation
- Code review

# Personal
- Grocery shopping
- Exercise
- Read for 30 minutes

# Instructions
Edit this file to update your wallpaper!
Use # for headers and - for tasks
"""
    
    with open(os.path.join(package_dir, "tasks.txt"), "w") as f:
        f.write(sample_tasks)
    
    # Create README for the package
    readme_content = """# TaskWallpaper Portable

## Quick Start
1. Run TaskWallpaper.exe
2. Edit tasks.txt to update your wallpaper
3. Your desktop wallpaper will update automatically!

## Features
- Real-time wallpaper updates
- Simple text-based task management
- Beautiful dark theme
- Automatic file monitoring

## Usage
- Use # for section headers
- Use - for individual tasks
- Save the file to see changes instantly

Enjoy your productivity boost! 🚀
"""
    
    with open(os.path.join(package_dir, "README.txt"), "w") as f:
        f.write(readme_content)
    
    print(f"✅ Portable package created: {package_dir}/")

def clean_build_files():
    """Clean up build files"""
    print("Cleaning up build files...")
    for folder in ["build", "dist", "__pycache__"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
    
    # Remove spec file
    spec_file = "TaskWallpaper.spec"
    if os.path.exists(spec_file):
        os.remove(spec_file)

def main():
    print("🚀 Dynamic Task Wallpaper - Executable Builder")
    print("=" * 50)
    
    # Check if PyInstaller is installed
    if not check_pyinstaller():
        install_pyinstaller()
    
    # Create executable
    create_executable()
    
    # Ask if user wants to clean build files
    response = input("\n🧹 Clean build files? (y/n): ").strip().lower()
    if response == 'y':
        clean_build_files()
    
    print("\n✅ Build complete! Your executable is ready to use.")
    print("📝 Don't forget to star the repository if you find it useful!")

if __name__ == "__main__":
    main()