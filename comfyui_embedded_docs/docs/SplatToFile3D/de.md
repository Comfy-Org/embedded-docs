# SplatToFile3D

Der Node SplatToFile3D konvertiert einen Gaussian-Splat in ein File3D-Objekt, das mit Save- oder Preview-3D-Nodes verwendet werden kann. Er unterstützt nur ein Element pro Batch und ermöglicht die Auswahl aus verschiedenen Ausgabedateiformaten für die exportierten 3D-Daten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `splat` | Die Gaussian-Splat-Daten, die in eine Datei serialisiert werden sollen | SPLAT | Ja | - |
| `format` | Das Ausgabedateiformat für die 3D-Datei (Standard: "ply"). ply: Standard-3D-Gaussian-Splat mit vollständigen sphärischen Harmonischen. ksplat: mkkellogg SplatBuffer (Level 0, unkomprimiert), nur Basisfarbe. spz: Niantic gzip-komprimiert (~10x kleiner), nur Basisfarbe | COMBO | Ja | "ply"<br>"ksplat"<br>"spz" |

Hinweis: Dieser Node unterstützt nur ein Element pro Batch. Wenn der eingegebene Splat mehr als ein Element im Batch enthält, gibt der Node eine Warnung aus und verwendet das erste Element. Wenn ein nicht unterstütztes Format angegeben wird, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_3d` | Ein File3D-Objekt, das die serialisierten Gaussian-Splat-Daten im ausgewählten Format enthält und zum Speichern oder zur Vorschau bereit ist | FILE3D |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/de.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
