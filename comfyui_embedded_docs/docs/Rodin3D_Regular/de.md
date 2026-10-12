# Rodin3D_Regular

Der Node Rodin 3D Regular erzeugt 3D-Assets mithilfe der Rodin API. Er nimmt Eingabebilder entgegen und verarbeitet sie über den Rodin-Dienst, um 3D-Modelle zu erstellen. Der Node übernimmt den gesamten Workflow von der Aufgabenerstellung bis zum Herunterladen der endgültigen 3D-Modelldateien.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `Images` | Eingabebilder, die für die 3D-Modellgenerierung verwendet werden. Es können bis zu 5 Bilder bereitgestellt werden. Mindestens 1 Bild ist erforderlich. | IMAGE | Ja | - |
| `Seed` | Zufälliger Seed-Wert für reproduzierbare Ergebnisse (Standard: 0). | INT | Nein | 0 bis 65535 |
| `Material_Type` | Typ des Materials, das auf das 3D-Modell angewendet wird (Standard: "PBR"). | STRING | Nein | `"PBR"`<br>`"Shaded"` |
| `Polygon_count` | Ziel-Polygonanzahl und Mesh-Typ für das generierte 3D-Modell (Standard: "18K-Quad"). | STRING | Nein | `"4K-Quad"`<br>`"8K-Quad"`<br>`"18K-Quad"`<br>`"50K-Quad"<br>`"200K-Triangle"` |

**Hinweis:** Mindestens 1 Bild ist für die 3D-Modellgenerierung erforderlich. Es können maximal 5 Bilder bereitgestellt werden.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `3D Model Path` | Dateipfad zum generierten 3D-Modell (aus Gründen der Abwärtskompatibilität beibehalten). | STRING |
| `GLB` | Das generierte 3D-Modell im GLB-Format. | FILE3DGLB |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Regular/de.md)

---
**Source fingerprint (SHA-256):** `e0bd8ef311f33481fec877801dea80302eba076f2d9e12f52467e889242a9637`
