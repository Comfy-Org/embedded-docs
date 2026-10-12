# LoadMoGeModel

Lädt ein MoGe-Modell (Monokulare Geometrie) aus einer Datei und bereitet es für die Verwendung in Aufgaben zur Geometrieschätzung vor. Der Node liest die ausgewählte Modelldatei aus dem Ordner `geometry_estimation` und initialisiert das MoGe-Modell mit den darin gespeicherten Gewichten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model_name` | Der Name der zu ladenden MoGe-Modelldatei. Wählen Sie aus den Modelldateien, die im Ordner `geometry_estimation` Ihrer ComfyUI-Installation verfügbar sind. | COMBO | Ja | Liste der verfügbaren Modelldateien im Ordner `geometry_estimation` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MOGE_MODEL` | Die geladene MoGe-Modellinstanz, bereit zur Verwendung in Workflows zur Geometrieschätzung. | MOGE_MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/de.md)

---
**Source fingerprint (SHA-256):** `b5b55f94d3762852d5a1480c0b00d15da4e534adbeb544bf7c47da012e5a6353`
