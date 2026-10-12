# Rodin 3D Generate – Gen-2 generieren

Der Node Rodin3D_Gen2 erzeugt 3D-Assets mithilfe der Rodin-API. Er nimmt Eingabebilder entgegen und wandelt sie in 3D-Modelle mit verschiedenen Materialtypen und Polygonanzahlen um. Der Node übernimmt automatisch den gesamten Generierungsprozess, einschließlich Aufgabenerstellung, Statusabfrage und Dateidownload.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Images` | Eingabebilder für die 3D-Modellgenerierung. Akzeptiert 1 bis 5 Bilder. | IMAGE | Ja | - |
| `Seed` | Zufälliger Seed-Wert für die Generierung (Standard: 0) | INT | Nein | 0-65535 |
| `Material_Type` | Typ des Materials, das auf das 3D-Modell angewendet werden soll (Standard: "PBR") | COMBO | Nein | "PBR"<br>"Shaded" |
| `Polygon_count` | Ziel-Polygonanzahl und Mesh-Typ für das generierte 3D-Modell. "Quad"-Optionen verwenden quad-basierte Meshes, "Triangle"-Optionen verwenden dreiecksbasierte Meshes (Standard: "500K-Triangle") | COMBO | Nein | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" |
| `TAPose` | Gibt an, ob TAPose-Verarbeitung angewendet werden soll (Standard: False). Dies ist ein erweiterter Parameter. | BOOLEAN | Nein | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `3D Model Path` | Dateipfad zum generierten 3D-Modell (für Abwärtskompatibilität) | STRING |
| `GLB` | Das generierte 3D-Modell im GLB-Format | FILE3DGLB |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/de.md)

---
**Source fingerprint (SHA-256):** `6ee8b52152e84cca48c7875ce066ab19805a42e5cccc84865c6027a4f6fd3b16`
