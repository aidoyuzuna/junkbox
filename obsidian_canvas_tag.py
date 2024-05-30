import yaml
from pathlib import Path
from pyjsoncanvas import (
    Canvas,
    FileNode,
)


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
    vault_root = Path(r"I:\05_Output\051_Git\yuzunamemo_old\quartz\content")
    vault_path = vault_root / "Inbox"
    search_tag = "西洋占星術"
    canvas_path = Path(r"I:\05_Output\051_Git\yuzunamemo_old\quartz\content\Canvas") / f"summary_{search_tag}.canvas"

    matched_files = [
        file_path
        for file_path in vault_path.glob("*.md")
        if has_tag(file_path, search_tag)
    ]

    canvas = Canvas(nodes=[], edges=[])
    width = 800
    height = 900

    for i, file_path in enumerate(matched_files):
        node = FileNode(
            id=str(i),
            x=0,
            y=0 + i * int(height * 0.5),
            width=width,
            height=height,
            file=str(file_path.relative_to(vault_root).as_posix())
        )

        canvas.add_node(node)

    with open(canvas_path, "w", encoding="utf-8") as f:
        f.write(canvas.to_json())


if __name__ == '__main__':
    main()
