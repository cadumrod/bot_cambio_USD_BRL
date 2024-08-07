# hyperlink.py
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import RGBColor


def add_hyperlink(paragrafo, url, color=RGBColor(0, 0, 255), underline=True):
    part = paragrafo.part
    r_id = part.relate_to(
        url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)

    # Cria um elemento w:r e um novo w:rPr
    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")

    # Adiciona cor
    if color:
        c = OxmlElement("w:color")
        c.set(qn("w:val"), str(color))
        rPr.append(c)

    # Adiciona underline
    if underline:
        u = OxmlElement("w:u")
        u.set(qn("w:val"), "single")
        rPr.append(u)

    # Adiciona w:rPr no elemento w:r
    new_run.append(rPr)

    # Cria um elemento w:t com o texto
    text_elem = OxmlElement("w:t")
    text_elem.text = url
    new_run.append(text_elem)

    # Adiciona o elemento w:r ao w:hyperlink
    hyperlink.append(new_run)

    # Adiciona o hyperlink no paragrafo
    paragrafo._p.append(hyperlink)

    return hyperlink
