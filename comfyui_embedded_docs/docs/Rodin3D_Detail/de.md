# Rodin 3D Generate - Detail Generate

Der Node Rodin 3D Detail generiert detaillierte 3D-Assets mithilfe der Rodin-API. Er nimmt Eingabebilder entgegen und verarbeitet sie über den Rodin-Dienst, um hochwertige 3D-Modelle mit detaillierter Geometrie und Materialien zu erstellen. Der Node übernimmt den gesamten Workflow von der Erstellung der Aufgabe bis zum Herunterladen der endgültigen 3D-Modelldatei.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|--------|
| `Images` | Eingabebilder, die für die 3D-Modellgenerierung verwendet werden. Es ist mindestens 1 Bild erforderlich, und es können maximal 5 Bilder bereitgestellt werden. | IMAGE | Ja | - |
| `Seed` | Zufälliger Seed-Wert für reproduzierbare Ergebnisse (Standard: 0) | INT | Nein | 0 bis 65535 |
| `Material_Type` | Art des Materials, das auf das 3D-Modell angewendet wird (Standard: "PBR") | STRING | Nein | `"PBR"`<br>`"Shaded"` |
| `Polygon_count` | Ziel-Polygonanzahl für das generierte 3D-Modell. Bestimmt die Mesh-Qualitätsstufe (Standard: "18K-Quad") | STRING | Nein | `"4K-Quad"`<br>`"8K-Quad"`<br>`"18K-Quad"`<br>`"50K-Quad"`<br>`"200K-Triangle"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `3D Model Path` | Dateipfad zum generierten 3D-Modell (nur aus Gründen der Abwärtskompatibilität) | STRING |
| `GLB` | Das generierte 3D-Modell im GLB-Format | FILE3DGLB |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/de.md)

---
**Source fingerprint (SHA-256):** `941265733c20d27d67621a83a05be822731696f4dd376299510d4279a35f51ee`
