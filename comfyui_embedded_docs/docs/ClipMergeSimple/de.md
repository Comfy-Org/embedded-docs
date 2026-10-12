# ClipMergeSimple

`CLIPMergeSimple` ist ein Modell-Merge-Node, der zwei CLIP-Textencoder-Modelle basierend auf einem angegebenen Verhältnis kombiniert. Er klont das erste CLIP-Modell und wendet gewichtete Patches aus dem zweiten CLIP-Modell an, wobei Positions-IDs und Logit-Scale-Komponenten übersprungen werden, um ein Hybridmodell zu erzeugen, das Merkmale aus beiden Quellen kombiniert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip1` | Das erste CLIP-Modell, das zusammengeführt werden soll. Es dient als Basismodell für den Merge-Prozess. | CLIP | Ja | - |
| `clip2` | Das zweite CLIP-Modell, das zusammengeführt werden soll. Seine Key-Patches, mit Ausnahme von Positions-IDs und Logit-Scale, werden basierend auf dem angegebenen Verhältnis auf das erste Modell angewendet. | CLIP | Ja | - |
| `ratio` | Bestimmt den Anteil der Merkmale aus dem zweiten Modell, der in das erste Modell eingemischt wird. Ein Verhältnis von 1.0 bedeutet, dass die Merkmale des zweiten Modells vollständig übernommen werden, während 0.0 nur die Merkmale des ersten Modells beibehält. Standard: 1.0. | FLOAT | Ja | 0.0 - 1.0 (step: 0.01) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip` | Das resultierende zusammengeführte CLIP-Modell, das Merkmale aus beiden Eingabemodellen gemäß dem angegebenen Verhältnis enthält. | CLIP |

## Erklärung des Merge-Mechanismus

### Merge-Algorithmus

Der Node verwendet gewichtete Mittelung, um die beiden Modelle zusammenzuführen:

1. **Basismodell klonen**: Zuerst wird `clip1` als Basismodell geklont
2. **Patches abrufen**: Alle Key-Patches aus `clip2` werden abgerufen
3. **Spezielle Schlüssel filtern**: Schlüssel, die mit `.position_ids` und `.logit_scale` enden, werden übersprungen
4. **Gewichteten Merge anwenden**: Verwendet die Formel `(1.0 - ratio) * clip1 + ratio * clip2`

### Erläuterung des Parameters `ratio`

- **ratio = 0.0**: Verwendet vollständig clip1, ignoriert clip2
- **ratio = 0.5**: 50 % Beitrag von jedem Modell
- **ratio = 1.0**: Verwendet vollständig clip2, ignoriert clip1

## Anwendungsfälle

1. **Modellstil-Fusion**: Kombinieren Sie Merkmale von CLIP-Modellen, die auf unterschiedlichen Daten trainiert wurden
2. **Leistungsoptimierung**: Stärken und Schwächen verschiedener Modelle ausbalancieren
3. **Experimentelle Forschung**: Kombinationen verschiedener CLIP-Encoder erkunden

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipMergeSimple/de.md)

---
**Source fingerprint (SHA-256):** `42c4b2042c56c3f21a9416aa577e2d41fef1dcc749c4e5c7953851110a4fb6bc`
