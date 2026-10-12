# Rodin 3D-Generierung – Skizzengenerierung

Dieser Node generiert 3D-Assets mithilfe der Rodin-API. Er nimmt Eingabebilder und konvertiert sie über einen externen Dienst in 3D-Modelle. Der Node übernimmt den gesamten Prozess von der Erstellung der Aufgabe bis zum Herunterladen der endgültigen 3D-Modelldateien.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `Images` | Eingabebilder, die in 3D-Modelle konvertiert werden sollen. Sie können zwischen 1 und 5 Bilder angeben. | IMAGE | Ja | 1 bis 5 Bilder |
| `Seed` | Zufälliger Seed-Wert für die Generierung (Standard: 0). Auf 0 setzen, um einen zufälligen Seed zu verwenden. | INT | Nein | 0 bis 65535 |

**Hinweis:** Der Node erfordert mindestens 1 Bild und unterstützt maximal 5 Bilder. Wenn keine Bilder bereitgestellt werden, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `3D Model Path` | Dateipfad zum generierten 3D-Modell (nur aus Gründen der Abwärtskompatibilität) | STRING |
| `GLB` | Das generierte 3D-Modell im GLB-Format | FILE3DGLB |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/de.md)

---
**Source fingerprint (SHA-256):** `0b77ce871e267450af63f3e2fe0e36fe81ababc25cbb11498546ad8f487b65e5`
