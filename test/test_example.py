from pathlib import Path

from wunlatex import Document
from wunlatex.components import Section


class TestDocument:

    def test_create_document(self):
        doc = Document(name="Test Document", template_path=Path(__file__).parent / "template.tex")

        doc.add_component(Section("One Section", components=[
            Section("Sub Section")
        ]))

        doc.compile(Path(__file__).parent, "TestDocument")

        assert (Path(__file__).parent / "TestDocument.pdf").is_file()
