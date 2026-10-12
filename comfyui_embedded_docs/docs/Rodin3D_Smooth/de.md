# Rodin 3D-Generierung – Glatte Generierung

Der Rodin 3D Smooth-Node generiert 3D-Assets mithilfe der Rodin API, indem er Eingabebilder verarbeitet und sie in glatte 3D-Modelle umwandelt. Er nimmt mehrere Bilder als Eingabe entgegen und erzeugt eine herunterladbare 3D-Modell-Datei. Der Node übernimmt den gesamten Generierungsprozess, einschließlich Aufgabenerstellung, Statusabfrage und automatischem Dateidownload.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Images` | Eingabebilder, die für die Generierung des 3D-Modells verwendet werden. Es können mehrere Bilder bereitgestellt werden (bis zu 5). | IMAGE | Ja | - |
| `Seed` | Zufälliger Seed-Wert für die Konsistenz der Generierung (Standard: 0). | INT | Nein | 0 to 65535 |
| `Material_Type` | Materialtyp, der auf das 3D-Modell angewendet wird (Standard: "PBR"). | STRING | Nein | "PBR"<br>"Shaded" |
| `Polygon_count` | Ziel-Polygonanzahl für das generierte 3D-Modell. Bestimmt die Mesh-Qualität und Detailstufe (Standard: "18K-Quad"). | STRING | Nein | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"200K-Triangle" |

**Hinweis:** Der Node akzeptiert bis zu 5 Eingabebilder. Wenn keine Bilder bereitgestellt werden, wird ein Fehler ausgelöst.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `3D Model Path` | Dateipfad zum heruntergeladenen 3D-Modell (nur für Abwärtskompatibilität). | STRING |
| `GLB` | Das generierte 3D-Modell im GLB-Format. | FILE3DGLB |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/de.md)

---
**Source fingerprint (SHA-256):** `c7dc23d2a7a8e2d425fc389476ef381f4ebf974f522c6e3774222866eee064e9`
