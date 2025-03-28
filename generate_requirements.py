import os
import ast

def get_imports_from_file(file_path):
    """Extract imports from a given Python file."""
    imports = set()
    try:
        with open(file_path, 'r') as file:
            print(f"Reading file: {file_path}")  # Debugging line
            tree = ast.parse(file.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for n in node.names:
                        imports.add(n.name)
                elif isinstance(node, ast.ImportFrom):
                    imports.add(node.module)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return imports

def generate_requirements_txt(project_folder):
    """Generate a requirements.txt file from Python files in the project folder."""
    all_imports = set()

    for root, _, files in os.walk(project_folder):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                imports = get_imports_from_file(file_path)
                all_imports.update(imports)

    if not all_imports:
        print("No imports found. Please check if import statements are written properly.")
    
    with open('requirements.txt', 'w') as req_file:
        for imp in sorted(all_imports):
            req_file.write(f"{imp}\n")
    
    print(f"requirements.txt generated with {len(all_imports)} packages.")

def install_requirements():
    """Install the packages listed in requirements.txt."""
    os.system('pip install -r requirements.txt')

if __name__ == "__main__":
    project_folder = 'trading_ai copy'  # Update with your actual project folder if necessary
    generate_requirements_txt(project_folder)
    # install_requirements()

