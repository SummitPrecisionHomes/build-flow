import os
import shutil
from datetime import datetime

def export_project():
    # Define the project directory and output archive name
    project_dir = os.path.dirname(os.path.abspath(__file__))
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = f"project_export_{timestamp}.zip"

    # Define files and directories to exclude
    exclude_dirs = ['__pycache__', 'migrations', 'venv']
    exclude_files = ['*.pyc', '*.pyo']

    def exclude_filter(directory, contents):
        excluded = []
        for item in contents:
            if item in exclude_dirs or any(item.endswith(ext) for ext in exclude_files):
                excluded.append(item)
        return excluded

    # Create the archive
    shutil.make_archive(output_filename.replace('.zip', ''), 'zip', project_dir, ignore=exclude_filter)

    print(f"Project exported successfully to {output_filename}")

if __name__ == "__main__":
    export_project()