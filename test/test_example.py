from pathlib import Path

from wunlatex import Document
from wunlatex.components import Section
import wunlatex
import pandas as pd
from matplotlib import pyplot as plt


class TestDocument:

    def test_create_document(self):
        doc = Document(name="Test Document", template_path=Path(__file__).parent / "template.tex")

        doc.add_component(Section("One Section", components=[
            Section("Sub Section")
        ]))

        doc.compile(Path(__file__).parent, "TestDocument")

        assert (Path(__file__).parent / "TestDocument.pdf").is_file()

    def test_2(self):
        doc = wunlatex.Document("Test")

        df = pd.DataFrame([(1, 2, 3, 4)], columns=["One", "JJJ", "LKAS", "ONENEE"])
        tbl = wunlatex.components.Table("Random Numbers", df)
        doc.add_component(tbl)

        # Sections within other sections are subsections, then subsubsections etc.
        doc.add_component(
            wunlatex.components.Section("First", components=[
                wunlatex.components.Section("Subsection 1", components=[tbl]),
                wunlatex.components.Section("Subsection 2", components=[
                    wunlatex.components.Section("SubSubSection 3")
                ])
            ])
        )

        fig, ax = plt.subplots()
        ax.plot([1, 1], [0, 1])
        figname = Path(__file__).parent / "testfig.png"
        plt.savefig(figname)
        f = wunlatex.components.Figure("Test Fig", path=figname)
        doc.add_component(f)

        doc.compile(Path(__file__).parent, filename="Testpdf")
