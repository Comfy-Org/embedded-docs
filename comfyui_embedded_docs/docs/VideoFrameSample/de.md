# VideoFrameSample

Der `VideoFrameSample`-Node extrahiert eine feste Anzahl von Frames aus einem Video mithilfe einer von vier Strategien. Bei den zusammenhängenden Strategien "head" und "tail" ist die Ausgabe eine Lazy-Video-Referenz (Frames werden nicht dekodiert); bei den nicht zusammenhängenden Strategien "uniform" und "random" werden nur die ausgewählten Frames dekodiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `video` | Eingabevideo. | VIDEO | Ja | – |
| `num_frames` | Anzahl der zu sampelnden Frames (Standard: 16). | INT | Ja | 1 – 9999 |
| `strategy` | "uniform": gleichmäßig verteilt, "head": die ersten N, "tail": die letzten N, "random": zufällig sortiert (Standard: "uniform"). | COMBO | Ja | "uniform"<br>"head"<br>"tail"<br>"random" |
| `seed` | Zufalls-Seed, wird nur mit der Strategie "random" verwendet (Standard: 0). | INT | Ja | 0 – 18446744073709551615 |

- `num_frames` wird automatisch auf die Gesamtzahl der Frames des Eingabevideos begrenzt.
- Der Parameter `seed` hat keine Auswirkung, sofern `strategy` nicht auf `"random"` gesetzt ist.
- Wenn `strategy` auf `"uniform"` gesetzt ist und `num_frames` 1 ist, wird der mittlere Frame des Videos ausgewählt.
- Ein nicht erkannter `strategy`-Wert löst einen Fehler aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `video` | Gesampeltes Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoFrameSample/de.md)

---
**Source fingerprint (SHA-256):** `727504a9cf7fe5505c33da071cb8f21a38e1b7c0f964c5da172d9cedfc2f2300`
