#!/usr/bin/env python3
"""
Static Preview Generator for Congruence of Arcs Animation
Creates matplotlib-based previews of what each scene would look like in Manim
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import Arc, Circle, FancyBboxPatch
import matplotlib.patches as mpatches

# Set up the plotting style
plt.style.use('dark_background')

def create_scene_preview(scene_num, title, save_path=None):
    """Create a preview of a specific scene"""
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Add scene title
    ax.text(0, 3.5, f"Scene {scene_num}: {title}", 
            fontsize=20, color='lime', ha='center', weight='bold')
    
    if scene_num == 1:
        preview_scene_1(ax)
    elif scene_num == 2:
        preview_scene_2(ax)
    elif scene_num == 3:
        preview_scene_3(ax)
    elif scene_num == 4:
        preview_scene_4(ax)
    elif scene_num == 5:
        preview_scene_5(ax)
    elif scene_num == 6:
        preview_scene_6(ax)
    elif scene_num == 7:
        preview_scene_7(ax)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, facecolor='black', dpi=150, bbox_inches='tight')
        print(f"✅ Scene {scene_num} preview saved to {save_path}")
    
    return fig, ax

def preview_scene_1(ax):
    """Scene 1: Introduction to Arcs"""
    
    # Draw circle
    circle = Circle((0, 0), 2, fill=False, color='white', linewidth=3)
    ax.add_patch(circle)
    
    # Draw points A and B
    angle_a = np.pi/6
    angle_b = 5*np.pi/6
    point_a = (2*np.cos(angle_a), 2*np.sin(angle_a))
    point_b = (2*np.cos(angle_b), 2*np.sin(angle_b))
    
    ax.plot(point_a[0], point_a[1], 'ro', markersize=10)
    ax.plot(point_b[0], point_b[1], 'ro', markersize=10)
    ax.text(point_a[0]+0.2, point_a[1]+0.2, 'A', fontsize=16, color='red', weight='bold')
    ax.text(point_b[0]-0.2, point_b[1]+0.2, 'B', fontsize=16, color='red', weight='bold')
    
    # Draw arc AB
    arc_angles = np.linspace(angle_a, angle_b, 100)
    arc_x = 2 * np.cos(arc_angles)
    arc_y = 2 * np.sin(arc_angles)
    ax.plot(arc_x, arc_y, 'yellow', linewidth=6)
    
    # Add definition
    ax.text(0, -3, "Arc: Part of a circle between two points", 
            fontsize=16, color='white', ha='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='gray', alpha=0.3))

def preview_scene_2(ax):
    """Scene 2: Defining Congruent Arcs"""
    
    # Draw two circles
    circle1 = Circle((-3, 0), 1.5, fill=False, color='white', linewidth=3)
    circle2 = Circle((3, 0), 1.5, fill=False, color='white', linewidth=3)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    
    # Draw congruent arcs
    arc_angle = np.pi/3
    start_angle = np.pi/6
    
    # Arc PQ (blue)
    arc_angles1 = np.linspace(start_angle, start_angle + arc_angle, 50)
    arc_x1 = -3 + 1.5 * np.cos(arc_angles1)
    arc_y1 = 1.5 * np.sin(arc_angles1)
    ax.plot(arc_x1, arc_y1, 'blue', linewidth=6)
    
    # Arc RS (red)
    arc_angles2 = np.linspace(start_angle, start_angle + arc_angle, 50)
    arc_x2 = 3 + 1.5 * np.cos(arc_angles2)
    arc_y2 = 1.5 * np.sin(arc_angles2)
    ax.plot(arc_x2, arc_y2, 'red', linewidth=6)
    
    # Add labels
    ax.text(-3, -2.2, "Arc PQ", fontsize=14, color='blue', ha='center', weight='bold')
    ax.text(3, -2.2, "Arc RS", fontsize=14, color='red', ha='center', weight='bold')
    
    # Add measurements
    ax.text(-3, 2.2, "60°", fontsize=12, color='yellow', ha='center')
    ax.text(3, 2.2, "60°", fontsize=12, color='yellow', ha='center')
    
    # Definition
    ax.text(0, -3, "Congruent Arcs: Arcs with equal measure (length or degrees)", 
            fontsize=14, color='white', ha='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='gray', alpha=0.3))

def preview_scene_3(ax):
    """Scene 3: Degrees and Length of Arcs"""
    
    # Draw circle
    circle = Circle((0, 0), 2, fill=False, color='white', linewidth=3)
    ax.add_patch(circle)
    
    # Center point
    ax.plot(0, 0, 'wo', markersize=8)
    ax.text(-0.3, -0.3, 'O', fontsize=14, color='white', weight='bold')
    
    # Draw arc
    start_angle = np.pi/4
    arc_angle = np.pi/2
    arc_angles = np.linspace(start_angle, start_angle + arc_angle, 50)
    arc_x = 2 * np.cos(arc_angles)
    arc_y = 2 * np.sin(arc_angles)
    ax.plot(arc_x, arc_y, 'blue', linewidth=6)
    
    # Draw radii
    point_c = (2*np.cos(start_angle), 2*np.sin(start_angle))
    point_d = (2*np.cos(start_angle + arc_angle), 2*np.sin(start_angle + arc_angle))
    
    ax.plot([0, point_c[0]], [0, point_c[1]], 'lime', linewidth=3)
    ax.plot([0, point_d[0]], [0, point_d[1]], 'lime', linewidth=3)
    
    # Points C and D
    ax.plot(point_c[0], point_c[1], 'bo', markersize=10)
    ax.plot(point_d[0], point_d[1], 'bo', markersize=10)
    ax.text(point_c[0]+0.2, point_c[1]+0.2, 'C', fontsize=16, color='blue', weight='bold')
    ax.text(point_d[0]-0.2, point_d[1]+0.2, 'D', fontsize=16, color='blue', weight='bold')
    
    # Central angle marking
    angle_arc = np.linspace(start_angle, start_angle + arc_angle, 20)
    angle_x = 0.5 * np.cos(angle_arc)
    angle_y = 0.5 * np.sin(angle_arc)
    ax.plot(angle_x, angle_y, 'yellow', linewidth=4)
    ax.text(0.7, 0.7, '90°', fontsize=14, color='yellow', weight='bold')
    
    # Formula
    ax.text(0, -3, "Arc length = (central angle/360°) × circumference", 
            fontsize=14, color='yellow', ha='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='darkblue', alpha=0.5))

def preview_scene_4(ax):
    """Scene 4: Examples of Congruent and Non-congruent Arcs"""
    
    # Four circles in a 2x2 grid
    positions = [(-3, 1), (3, 1), (-3, -1.5), (3, -1.5)]
    
    for i, pos in enumerate(positions):
        circle = Circle(pos, 1.2, fill=False, color='white', linewidth=2)
        ax.add_patch(circle)
    
    # Congruent arcs (top row) - same angle
    arc_angle1 = np.pi/3
    
    # First arc (green)
    arc_angles = np.linspace(0, arc_angle1, 30)
    arc_x1 = -3 + 1.2 * np.cos(arc_angles)
    arc_y1 = 1 + 1.2 * np.sin(arc_angles)
    ax.plot(arc_x1, arc_y1, 'lime', linewidth=5)
    ax.text(-3, 0.2, "60°", fontsize=12, color='lime', ha='center')
    
    # Second arc (green)
    arc_angles = np.linspace(np.pi/6, np.pi/6 + arc_angle1, 30)
    arc_x2 = 3 + 1.2 * np.cos(arc_angles)
    arc_y2 = 1 + 1.2 * np.sin(arc_angles)
    ax.plot(arc_x2, arc_y2, 'lime', linewidth=5)
    ax.text(3, 0.2, "60°", fontsize=12, color='lime', ha='center')
    
    # Non-congruent arcs (bottom row) - different angles
    arc_angle2 = np.pi/6
    arc_angle3 = np.pi/2
    
    # Third arc (red)
    arc_angles = np.linspace(0, arc_angle2, 20)
    arc_x3 = -3 + 1.2 * np.cos(arc_angles)
    arc_y3 = -1.5 + 1.2 * np.sin(arc_angles)
    ax.plot(arc_x3, arc_y3, 'red', linewidth=5)
    ax.text(-3, -2.3, "30°", fontsize=12, color='red', ha='center')
    
    # Fourth arc (red)
    arc_angles = np.linspace(0, arc_angle3, 40)
    arc_x4 = 3 + 1.2 * np.cos(arc_angles)
    arc_y4 = -1.5 + 1.2 * np.sin(arc_angles)
    ax.plot(arc_x4, arc_y4, 'red', linewidth=5)
    ax.text(3, -2.3, "90°", fontsize=12, color='red', ha='center')
    
    # Labels
    ax.text(0, 2.5, "CONGRUENT", fontsize=16, color='lime', ha='center', weight='bold')
    ax.text(0, -3, "NOT CONGRUENT", fontsize=16, color='red', ha='center', weight='bold')

def preview_scene_5(ax):
    """Scene 5: Exercise - Identifying Congruent Arcs"""
    
    # Exercise setup
    ax.text(0, 2.8, "Exercise: Are these arcs congruent?", 
            fontsize=16, color='white', ha='center', weight='bold')
    
    # Example pair
    circle1 = Circle((-2.5, 0), 1.5, fill=False, color='white', linewidth=3)
    circle2 = Circle((2.5, 0), 1.5, fill=False, color='white', linewidth=3)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    
    # Arc 1 (45°)
    arc_angle1 = np.pi/4
    arc_angles1 = np.linspace(0, arc_angle1, 30)
    arc_x1 = -2.5 + 1.5 * np.cos(arc_angles1)
    arc_y1 = 1.5 * np.sin(arc_angles1)
    ax.plot(arc_x1, arc_y1, 'blue', linewidth=6)
    ax.text(-2.5, -2, "45°", fontsize=14, color='blue', ha='center', weight='bold')
    
    # Arc 2 (45°)
    arc_angles2 = np.linspace(np.pi/6, np.pi/6 + arc_angle1, 30)
    arc_x2 = 2.5 + 1.5 * np.cos(arc_angles2)
    arc_y2 = 1.5 * np.sin(arc_angles2)
    ax.plot(arc_x2, arc_y2, 'yellow', linewidth=6)
    ax.text(2.5, -2, "45°", fontsize=14, color='yellow', ha='center', weight='bold')
    
    # Answer
    ax.text(0, -2.8, "✓ CONGRUENT", fontsize=18, color='lime', ha='center', weight='bold')

def preview_scene_6(ax):
    """Scene 6: Recap and Key Points"""
    
    ax.text(0, 2.5, "Key Points Recap", fontsize=20, color='lime', ha='center', weight='bold')
    
    key_points = [
        "• Arc: Part of a circle between two points",
        "• Congruent arcs have equal central angles", 
        "• Congruent arcs have equal lengths",
        "• Arc length = (central angle/360°) × circumference"
    ]
    
    for i, point in enumerate(key_points):
        ax.text(-5, 1.5 - i*0.8, point, fontsize=14, color='white', 
                va='center', weight='bold')

def preview_scene_7(ax):
    """Scene 7: Closing Remarks"""
    
    ax.text(0, 1.5, "Remember:", fontsize=20, color='yellow', ha='center', weight='bold')
    ax.text(0, 0.5, "Congruent arcs must have", fontsize=16, color='white', ha='center')
    ax.text(0, 0, "equal central angles and equal lengths", fontsize=16, color='white', ha='center')
    
    ax.text(0, -1.5, "Thank you for learning with us!", fontsize=18, color='cyan', 
            ha='center', weight='bold')

def generate_all_previews():
    """Generate previews for all scenes"""
    
    scenes = [
        (1, "Introduction to Arcs"),
        (2, "Defining Congruent Arcs"), 
        (3, "Degrees and Length of Arcs"),
        (4, "Examples of Congruent and Non-congruent Arcs"),
        (5, "Exercise - Identifying Congruent Arcs"),
        (6, "Recap and Key Points"),
        (7, "Closing Remarks")
    ]
    
    print("🎬 Generating Static Previews of Congruence of Arcs Animation")
    print("=" * 60)
    
    for scene_num, title in scenes:
        filename = f"scene_{scene_num}_preview.png"
        fig, ax = create_scene_preview(scene_num, title, filename)
        plt.close(fig)
    
    print("\n✅ All scene previews generated successfully!")
    print("📁 Files created:")
    for i in range(1, 8):
        print(f"   • scene_{i}_preview.png")
    
    print(f"\n💡 These previews show what the Manim animation would look like")
    print(f"🎯 Each scene is designed for clear student comprehension")

def create_combined_preview():
    """Create a single image showing all scenes"""
    
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    fig.patch.set_facecolor('black')
    fig.suptitle("Congruence of Arcs - Complete Animation Preview", 
                 fontsize=24, color='lime', weight='bold')
    
    scenes = [
        (1, "Introduction to Arcs"),
        (2, "Defining Congruent Arcs"), 
        (3, "Degrees and Length of Arcs"),
        (4, "Examples of Congruent and Non-congruent Arcs"),
        (5, "Exercise - Identifying Congruent Arcs"),
        (6, "Recap and Key Points"),
        (7, "Closing Remarks")
    ]
    
    # Plot first 4 scenes in top row
    for i in range(4):
        ax = axes[0, i]
        ax.set_facecolor('black')
        ax.set_xlim(-6, 6)
        ax.set_ylim(-4, 4)
        ax.set_aspect('equal')
        ax.axis('off')
        
        if i < len(scenes):
            scene_num, title = scenes[i]
            ax.text(0, 3.5, f"Scene {scene_num}", fontsize=12, color='lime', 
                   ha='center', weight='bold')
            
            if scene_num == 1:
                preview_scene_1(ax)
            elif scene_num == 2:
                preview_scene_2(ax)
            elif scene_num == 3:
                preview_scene_3(ax)
            elif scene_num == 4:
                preview_scene_4(ax)
    
    # Plot remaining scenes in bottom row
    for i in range(3):
        ax = axes[1, i]
        ax.set_facecolor('black')
        ax.set_xlim(-6, 6)
        ax.set_ylim(-4, 4)
        ax.set_aspect('equal')
        ax.axis('off')
        
        scene_num, title = scenes[i + 4]
        ax.text(0, 3.5, f"Scene {scene_num}", fontsize=12, color='lime', 
               ha='center', weight='bold')
        
        if scene_num == 5:
            preview_scene_5(ax)
        elif scene_num == 6:
            preview_scene_6(ax)
        elif scene_num == 7:
            preview_scene_7(ax)
    
    # Hide the last subplot
    axes[1, 3].axis('off')
    
    plt.tight_layout()
    plt.savefig("complete_animation_preview.png", facecolor='black', dpi=150, bbox_inches='tight')
    plt.close(fig)
    
    print("✅ Combined preview saved as 'complete_animation_preview.png'")

if __name__ == "__main__":
    generate_all_previews()
    create_combined_preview()
    
    print(f"\n🎉 Preview Generation Complete!")
    print(f"📚 These static images show what your Manim animation will look like")
    print(f"🔄 To see the actual animated version, install Manim and run:")
    print(f"   manimgl congruent_arcs_animation.py CongruenceOfArcs")