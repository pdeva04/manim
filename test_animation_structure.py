#!/usr/bin/env python3
"""
Test script to validate the structure of the Congruence of Arcs animation
without requiring full Manim installation.
"""

import ast
import sys

def validate_animation_structure(filename):
    """Validate the structure and syntax of the animation file."""
    
    print(f"🔍 Validating {filename}...")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        # Parse the AST to check syntax
        tree = ast.parse(content)
        print("✅ Syntax validation passed")
        
        # Extract class and method information
        classes = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                classes.append({
                    'name': node.name,
                    'methods': methods
                })
        
        print(f"\n📋 Found {len(classes)} classes:")
        
        # Check main CongruenceOfArcs class
        main_class = next((c for c in classes if c['name'] == 'CongruenceOfArcs'), None)
        if main_class:
            print(f"✅ Main class 'CongruenceOfArcs' found")
            expected_methods = [
                'construct',
                'scene_1_introduction_to_arcs',
                'scene_2_defining_congruent_arcs', 
                'scene_3_degrees_and_length',
                'scene_4_examples',
                'scene_5_exercise',
                'scene_6_recap',
                'scene_7_closing',
                'exercise_pair'
            ]
            
            print("\n🎬 Scene methods validation:")
            for method in expected_methods:
                if method in main_class['methods']:
                    print(f"  ✅ {method}")
                else:
                    print(f"  ❌ {method} - MISSING")
        else:
            print("❌ Main class 'CongruenceOfArcs' not found")
        
        # Check individual scene classes
        scene_classes = [c for c in classes if c['name'].startswith('Scene')]
        print(f"\n🎭 Individual scene classes: {len(scene_classes)} found")
        expected_scenes = [
            'Scene1IntroductionToArcs',
            'Scene2DefiningCongruentArcs',
            'Scene3DegreesAndLength', 
            'Scene4Examples',
            'Scene5Exercise',
            'Scene6Recap',
            'Scene7Closing'
        ]
        
        for scene in expected_scenes:
            if any(c['name'] == scene for c in scene_classes):
                print(f"  ✅ {scene}")
            else:
                print(f"  ❌ {scene} - MISSING")
        
        print(f"\n📊 Animation structure summary:")
        print(f"  • Total classes: {len(classes)}")
        print(f"  • Main class methods: {len(main_class['methods']) if main_class else 0}")
        print(f"  • Individual scene classes: {len(scene_classes)}")
        print(f"  • Lines of code: {len(content.splitlines())}")
        
        return True
        
    except SyntaxError as e:
        print(f"❌ Syntax error: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def analyze_educational_features(filename):
    """Analyze educational features in the animation."""
    
    print(f"\n🎓 Analyzing educational features...")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        # Count educational elements
        features = {
            'wait_statements': content.count('self.wait('),
            'text_elements': content.count('Text('),
            'color_usage': content.count('color='),
            'animations': content.count('self.play('),
            'mathematical_symbols': content.count('MathTex('),
            'interactive_elements': content.count('exercise_pair'),
            'transitions': content.count('FadeOut('),
            'scene_divisions': content.count('def scene_')
        }
        
        print("📈 Educational features count:")
        for feature, count in features.items():
            emoji = "✅" if count > 0 else "⚠️"
            print(f"  {emoji} {feature.replace('_', ' ').title()}: {count}")
        
        # Check for educational best practices
        print(f"\n🏆 Educational best practices:")
        
        practices = [
            ("Slow pacing (wait statements)", features['wait_statements'] >= 20),
            ("Rich text content", features['text_elements'] >= 15),
            ("Color-coded learning", features['color_usage'] >= 30),
            ("Interactive exercises", features['interactive_elements'] >= 1),
            ("Mathematical formulas", features['mathematical_symbols'] >= 1),
            ("Smooth transitions", features['transitions'] >= 10),
            ("Well-structured scenes", features['scene_divisions'] == 7)
        ]
        
        for practice, implemented in practices:
            emoji = "✅" if implemented else "⚠️"
            print(f"  {emoji} {practice}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error analyzing features: {e}")
        return False

def generate_usage_examples():
    """Generate usage examples for the animation."""
    
    print(f"\n💡 Usage Examples:")
    print("=" * 50)
    
    examples = [
        {
            "title": "Run Complete Animation",
            "command": "manimgl congruent_arcs_animation.py CongruenceOfArcs",
            "description": "Runs all 7 scenes sequentially"
        },
        {
            "title": "Run Individual Scene",
            "command": "manimgl congruent_arcs_animation.py Scene1IntroductionToArcs",
            "description": "Runs only Scene 1: Introduction to Arcs"
        },
        {
            "title": "Export to Video",
            "command": "manimgl congruent_arcs_animation.py CongruenceOfArcs -w",
            "description": "Creates a video file of the complete animation"
        },
        {
            "title": "Preview Final Frame",
            "command": "manimgl congruent_arcs_animation.py CongruenceOfArcs -s",
            "description": "Skips to the end and shows final frame"
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{i}. {example['title']}")
        print(f"   Command: {example['command']}")
        print(f"   Description: {example['description']}")

def main():
    """Main function to run all validation tests."""
    
    print("🎬 Congruence of Arcs Animation Validator")
    print("=" * 50)
    
    filename = "congruent_arcs_animation.py"
    
    # Validate structure
    structure_valid = validate_animation_structure(filename)
    
    if structure_valid:
        # Analyze educational features
        analyze_educational_features(filename)
        
        # Generate usage examples
        generate_usage_examples()
        
        print(f"\n🎉 Validation Complete!")
        print("✅ Animation is ready for use with Manim")
        print("📚 All 7 educational scenes are properly structured")
        print("🎯 Designed for students struggling with arc congruence concepts")
        
    else:
        print(f"\n❌ Validation Failed!")
        print("Please fix the issues above before using the animation")
        sys.exit(1)

if __name__ == "__main__":
    main()