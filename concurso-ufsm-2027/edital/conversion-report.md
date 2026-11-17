# Conversion report — UFSM 2027 edital PDFs → Markdown

Working directory: `/Users/egg/projects/concurso/concurso-ufsm-2027/edital/`

**Verification methods.** (a) Visual comparison with rendered pages (scans, screenshots, tables, spot-checks of emphasis); (b) automated comparison between the PDF text layer (`pdftotext`) and the Markdown — sequence diff and order-independent bag-of-words diff; (c) arithmetic cross-checks where available (score weights summing to 100%); (d) page-marker integrity (one `<!-- PDF page N -->` per PDF page, in order — checked for all 11 files); (e) every `.md` parses in Pandoc without warnings.

| PDF | Pages | Extraction method | Status | Issues |
|---|---:|---|---|---|
| anexo-I-instrucoes-especificas.pdf | 5 | text layer | VERIFIED | Token-identical to the PDF. Item numbering on PDF p. 2 jumps from "5." to "7." (reproduced as printed). Differs from the Anexo I embedded in the Edital — see observations. |
| anexo-II-tabela de-pontos-para-avaliacao-de-titulos.pdf | 3 | visual transcription (outlined-text scan, no text layer) + OCR cross-check | VERIFIED | **Byte-identical to barema-cc.pdf** (same MD5). Despite its name it contains the written / didactic / defense score sheets, *not* the title-points table. |
| barema-cc.pdf | 3 | visual transcription (outlined-text scan, no text layer) + OCR cross-check | VERIFIED | Weights on each sheet sum to 100%; OCR percentages match page by page. |
| barema-titulos.pdf | 4 | text layer + page images | VERIFIED | This is the document actually titled "Anexo II – Tabela de Pontos para Avaliação de Títulos". Its tables are equivalent to the Anexo II inside both Edital versions (token comparison). |
| edital-no-doi.pdf | 10 | pdfplumber (tables, 2-column zones) | VERIFIED | Diário Oficial da União, Seção 3, nº 206, 03/11/2026, pp. 58–67. Contains **unrelated notices** of other bodies (UFSM contract extracts on PDF p. 1; UNIFESP notices on PDF p. 10); transcribed and kept. Source quirk: Word error text "Erro! A referência de hiperlink não é válida." inside item 4.17. Invisible stray "." glyphs in table cells removed. No missing words in the bag-of-words diff. |
| edital-ufsm.pdf | 27 | pdfplumber (tables), font-aware | VERIFIED | Full Edital 252/2026 + Anexos I and II + PEN authentication sheet (p. 27, rebuilt from the page image). The PDF itself contains a duplicated item "j) Quando, e se, solicitado …" (within item 8.14.2) — reproduced twice. Heading levels added; no text added. |
| lei-8112.pdf | 45 | pdfplumber (font, strike-through and link detection) | VERIFIED | Planalto compiled text. **Struck-through (revoked) wording is preserved as `~~…~~`**; hyperlinks kept. Ordinal "o" of the text layer written as "º" (as rendered). Pension-duration table (PDF pp. 37–38) rebuilt as a table. PDF pp. 44–45 contain the "partes vetadas e mantidas" excerpt. |
| resolucao-ufsm-2022-112.pdf | 17 | pdfplumber, font-aware | VERIFIED | Letter-form irregularities of the source text layer (e.g. "Iinguagem", "iguaI", "Iivre", "cientÍfico") are reproduced verbatim. **The Annex (Tabela de Pontos) referred to in Arts. 40–41 is not part of this 17-page PDF.** Page 17 is a PEN authentication sheet. |
| tutorial-para-abertura-de-recursos-administrativos-e-vistas-de-provas.pdf | 6 | text layer + visual check | VERIFIED | Screenshots identified with NON-TEXT comments, not transcribed in full. |
| tutorial-para-envio-de-documentos-para-prova-titulos-1.pdf | 10 | text layer + visual check | VERIFIED | Same. |
| tutorial-para-envio-do-memorial-descritivo.pdf | 6 | text layer + visual check | VERIFIED | Same. |

## Totals

- PDFs discovered: **11** (matches the expected 11).
- PDFs converted: **11**; Markdown files verified: **11**; needing manual review: **0**.
- Distinct documents: **10** (two PDFs are byte-identical).
- Original PDFs: untouched (sizes/timestamps unchanged; no file outside this directory modified).

## Cross-document observations (recorded as found, **not reconciled**)

1. **`anexo-I-instrucoes-especificas.pdf` vs. the Anexo I inside `edital-ufsm.pdf` and `edital-no-doi.pdf`.** The programs of points, areas and process numbers are identical, but:
   - Artes Visuais, item 5: the standalone Anexo I gives "Departamento de Artes Visuais/Centro de Artes e Letras" and **Telefone (55) 3220-8161**; both Edital versions give "UFSM – Centro de Artes e Letras / Departamento de Artes Visuais" and **Telefone (55) 3220-8087**.
   - Economia: standalone Anexo I **(55) 3220-9327**; both Edital versions **(55) 3178-0583**.
   - Each Anexo I page in the standalone PDF carries a "EDITAL N. 252, DE 29 DE OUTUBRO DE 2026" header; the Edital versions do not repeat it.
2. **`edital-no-doi.pdf` (DOU) vs. `edital-ufsm.pdf` (portal), body text.** Apart from typographic quotes and the Word hyperlink-error string noted above, the only textual difference found is in item 8.13.19: the DOU version contains the phrase "dirigida à chefia do Departamento Didático responsável pelo concurso, dirigida à chefia do Departamento Didático" (duplicated wording); the portal version has only "dirigida à chefia do Departamento Didático". Conversely the portal PDF duplicates item "j)" (see table above). The portal version is signed "Reitora Martha Bohrer Adaime"; the DOU version ends with the signature name only.
3. **Naming mismatch.** `anexo-II-tabela de-pontos-…pdf` (= `barema-cc.pdf`) contains the written/didactic/defense evaluation sheets; the title-points table is in `barema-titulos.pdf`.
4. **Resolução UFSM 112/2022** refers to "Anexo I" for the title-points table, while the Edital calls it "Anexo II"; the Resolução's annex is not in the supplied PDF.
5. In the **Edital**, numbering starts at item "2. QUADRO DE VAGAS" (no item 1 exists in either version); item 3.2 reads "23h59min do 02 de dezembro de 2026" in both. Reproduced as printed.

## Limitations

- Screenshots in the three tutorials are described by NON-TEXT comments; their on-screen text is summarised, not transcribed in full (candidate/department names are blacked out in the originals).
- Emphasis (bold/italic/underline/colour) is reproduced from font names, strike-through rectangles and link colours; underline and text colour are not reproduced except where noted. Emphasis was spot-checked visually, not exhaustively.
- The two scanned documents (`barema-cc`, `anexo-II-…`) have no text layer; they were transcribed visually and cross-checked with OCR (English model only — no Portuguese language pack installed; all numbers and structure matched).
- Hyperlink targets are preserved for the tutorials, the Resolução, the Edital and the Lei; link *text* is always preserved.
- Text-layer irregularities of the sources (capital "I" for "l", lowercase "r$", "sore", "REALIZAÇAO", duplicated "§ 1º", etc.) were deliberately **not** corrected.
