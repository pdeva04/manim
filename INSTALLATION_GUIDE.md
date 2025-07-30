# Installation Guide for Congruence of Arcs Animation

This guide will help you install Manim and run the educational animation about Congruence of Arcs.

## Quick Start

If you already have Manim installed, simply run:
```bash
manimgl congruent_arcs_animation.py CongruenceOfArcs
```

## Full Installation (Ubuntu/Debian)

### 1. Install System Dependencies

```bash
# Update package list
sudo apt update

# Install Python and development tools
sudo apt install python3 python3-pip python3-venv

# Install required system libraries for Manim
sudo apt install build-essential python3-dev python3-setuptools
sudo apt install libcairo2-dev libpango1.0-dev
sudo apt install ffmpeg
sudo apt install pkg-config
```

### 2. Install ManimGL

```bash
# Install ManimGL (Grant Sanderson's version - used in this project)
pip3 install manimgl

# Or if you prefer, create a virtual environment first:
python3 -m venv manim_env
source manim_env/bin/activate
pip install manimgl
```

### 3. Verify Installation

```bash
# Test the animation structure
python3 test_animation_structure.py

# Run a simple test scene
manimgl congruent_arcs_animation.py Scene1IntroductionToArcs
```

## Installation (macOS)

### 1. Install Homebrew (if not already installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Dependencies
```bash
# Install Python
brew install python

# Install required libraries
brew install cairo pango pkg-config ffmpeg

# Install ManimGL
pip3 install manimgl
```

## Installation (Windows)

### Option 1: Using Conda (Recommended)
```bash
# Install Anaconda or Miniconda first
# Then create a new environment
conda create -n manim python=3.9
conda activate manim

# Install ManimGL
conda install -c conda-forge cairo pango pkg-config
pip install manimgl
```

### Option 2: Using WSL (Windows Subsystem for Linux)
1. Install WSL2 with Ubuntu
2. Follow the Ubuntu installation instructions above

## Alternative: Manim Community Edition

If you prefer the Community Edition of Manim:

```bash
# Install Manim Community Edition instead
pip install manim

# You'll need to modify the import statement in the animation file:
# Change: from manimlib import *
# To: from manim import *
```

## Running the Animation

### Complete Animation (All 7 Scenes)
```bash
manimgl congruent_arcs_animation.py CongruenceOfArcs
```

### Individual Scenes
```bash
# Scene 1: Introduction to Arcs
manimgl congruent_arcs_animation.py Scene1IntroductionToArcs

# Scene 2: Defining Congruent Arcs
manimgl congruent_arcs_animation.py Scene2DefiningCongruentArcs

# Scene 3: Degrees and Length
manimgl congruent_arcs_animation.py Scene3DegreesAndLength

# Scene 4: Examples
manimgl congruent_arcs_animation.py Scene4Examples

# Scene 5: Exercise
manimgl congruent_arcs_animation.py Scene5Exercise

# Scene 6: Recap
manimgl congruent_arcs_animation.py Scene6Recap

# Scene 7: Closing
manimgl congruent_arcs_animation.py Scene7Closing
```

### Export Options
```bash
# Create video file
manimgl congruent_arcs_animation.py CongruenceOfArcs -w

# Create video and open when done
manimgl congruent_arcs_animation.py CongruenceOfArcs -o

# Preview final frame only
manimgl congruent_arcs_animation.py CongruenceOfArcs -s

# High quality render
manimgl congruent_arcs_animation.py CongruenceOfArcs -w --high_quality
```

## Troubleshooting

### Common Issues

#### "Command not found: manimgl"
```bash
# Check if ManimGL is installed
pip3 list | grep manim

# If not installed, install it:
pip3 install manimgl

# If using virtual environment, make sure it's activated
source manim_env/bin/activate
```

#### "ModuleNotFoundError: No module named 'manimlib'"
```bash
# Install ManimGL (not Manim Community Edition)
pip3 install manimgl

# Or if you have Manim CE, change the import in the file:
# from manimlib import * → from manim import *
```

#### "Package 'cairo' not found" (Linux)
```bash
sudo apt install libcairo2-dev libpango1.0-dev pkg-config
```

#### Animation runs too slowly
```bash
# Use lower quality for faster preview
manimgl congruent_arcs_animation.py CongruenceOfArcs --low_quality

# Or skip animations and see final result
manimgl congruent_arcs_animation.py CongruenceOfArcs -s
```

#### Black screen or no output
```bash
# Check display settings (for WSL users)
export DISPLAY=:0

# Or try different render settings
manimgl congruent_arcs_animation.py CongruenceOfArcs --leave_progress_bars
```

### Performance Optimization

For better performance:
```bash
# Use lower quality for testing
manimgl congruent_arcs_animation.py CongruenceOfArcs --low_quality

# Use medium quality for good balance
manimgl congruent_arcs_animation.py CongruenceOfArcs --medium_quality

# Use high quality only for final render
manimgl congruent_arcs_animation.py CongruenceOfArcs --high_quality -w
```

## File Structure

After installation, your project should look like:
```
project_folder/
├── congruent_arcs_animation.py      # Main animation file
├── test_animation_structure.py      # Validation script
├── CONGRUENT_ARCS_README.md        # Detailed documentation
├── INSTALLATION_GUIDE.md           # This file
└── outputs/                        # Generated videos (created automatically)
```

## Educational Use

This animation is designed for:
- **Classroom presentations** (use `-w` to create video files)
- **Individual student study** (run interactively with live preview)
- **Homework assignments** (students can run specific scenes)
- **Teacher preparation** (preview with `-s` flag)

## System Requirements

- **Python**: 3.7 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 500MB for dependencies, additional space for video outputs
- **Graphics**: Any modern graphics card (integrated graphics work fine)
- **OS**: Linux, macOS, or Windows (with WSL recommended)

## Getting Help

1. **Test your installation**: `python3 test_animation_structure.py`
2. **Check Manim documentation**: https://docs.manim.community/
3. **ManimGL documentation**: https://3b1b.github.io/manim/
4. **GitHub issues**: Check the Manim project's GitHub for common problems

## Next Steps

Once you have the animation running:
1. Explore individual scenes to understand the structure
2. Modify colors, timing, or text to suit your needs
3. Add additional examples or exercises
4. Create your own geometry animations using this as a template

Happy animating! 🎬✨