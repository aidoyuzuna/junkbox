import yaml
import json
import os
from pathlib import Path

import obsidian_canvas.v1_0 as oc


def extract_header(file_path: Path) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    is_inside_header = False
    header_lines = []
    for line in lines:
        if line.startswith("---"):
            is_inside_header = not is_inside_header
            if is_inside_header:
                continue
            else:
                break
        if not is_inside_header:
            continue
        header_lines.append(line)
    header_str = "\n".join(header_lines)
    return yaml.safe_load(header_str)


def has_tag(file_path: Path, tag: str) -> bool:
    header = extract_header(file_path)
    if header is not None:
        tags = header.get("tags", [])
        if tag in tags:
            return True
    content = file_path.read_text(encoding="utf-8")
    return f"#{tag}" in content


def main():
    vault_path = Path(r"I:\05_Output\051_Git\yuzunamemo\quartz\content\02_Inbox")
    relative_path = vault_path.relative_to(r"I:\05_Output\051_Git\yuzunamemo\quartz\content")
    print(relative_path)
    search_tag = "ルナリターン"
    canvas_path = Path(r"I:\05_Output\051_Git\yuzunamemo\quartz\content\06_Canvas") / f"summary_{search_tag}.canvas"

    matched_files = [
        file_path
        for file_path in vault_path.glob("*.md")
        if has_tag(file_path, search_tag)
    ]

    nodes = []
    width = 900
    height = 800
    for i, file_path in enumerate(matched_files):
        print(os.path.join(relative_path,file_path.name))
        node = oc.Node(
            id=str(i),
            x=0,
            y=0 + i * int(height * 0.5),
            width=width,
            height=height,
            # content=oc.File(file=f"{vault_path.relative_to(r"I:\05_Output\051_Git\yuzunamemo\quartz\content")}/{file_path.name}")
            content=oc.File(file=os.path.join(relative_path,file_path.name))
        )
        nodes.append(node)
    canvas = oc.Canvas(nodes=nodes)
    with open(canvas_path, "w", encoding="utf-8") as f:
        json.dump(canvas.to_json(), f)


if __name__ == '__main__':
    main()