# File3DToSplat

Dieser Node wandelt eine 3D-Datei mit Gaussian-Splat-Daten in ein Gaussian-Splat-Format um, das im Node-Graph verwendet werden kann. Er unterstützt die Dateiformate PLY, SPLAT, KSPLAT und SPZ, wobei das Dateiformat automatisch aus dem Dateiinhalt erkannt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Eine 3D-Datei mit Gaussian-Splat-Daten | FILE3D | Ja | - |

Die Eingabedatei muss in einem der unterstützten Formate vorliegen: PLY, SPLAT, KSPLAT oder SPZ. PLY-Dateien enthalten vollständige Spherical-Harmonics-Daten, während die anderen Formate nur Basis-Farbinformationen enthalten. Das Format wird automatisch aus dem Dateiinhalt erkannt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `splat` | Ein Gaussian-Splat mit Position, Skalierung, Rotation, Deckkraft und Spherical-Harmonics-Daten | SPLAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/File3DToSplat/de.md)

---
**Source fingerprint (SHA-256):** `9f45210a1366e57a91de6e1251f0e2e09f39e6498dbec1db7bf9826ebedd167b`
