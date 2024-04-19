import typer
from typing import List
from pathlib import Path
from avatar_generator import AvatarGenerator

app = typer.Typer()

@app.command()
def merge_files(image_paths: List[Path]= typer.Option(..., "--input-paths", "-i"), output_path: str = typer.Option(..., "--output-path", "-o")):
    print(image_paths)
    gen = AvatarGenerator(None)
    gen.generate_custom_avatar(image_paths, output_path)

if __name__ == "__main__":
    app()