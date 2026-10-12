# Vidu Start- und Endbild-zu-Video-Generierung

Der Node Vidu Start End To Video Generation erstellt ein Video, indem er Frames zwischen einem Start-Frame und einem End-Frame generiert. Er verwendet einen Text-Prompt, um den Videogenerierungsprozess zu steuern, und unterstützt verschiedene Videomodelle mit unterschiedlichen Auflösungs- und Bewegungseinstellungen. Der Node validiert vor der Verarbeitung, dass Start- und End-Frame kompatible Seitenverhältnisse aufweisen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|--------|
| `model` | Modellname | COMBO | Ja | `"viduq1"` |
| `first_frame` | Start-Frame | IMAGE | Ja | - |
| `end_frame` | End-Frame | IMAGE | Ja | - |
| `prompt` | Eine textuelle Beschreibung für die Videogenerierung | STRING | Nein | - |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5, fest auf 5 Sekunden) | INT | Nein | 5-5 |
| `seed` | Seed für die Videogenerierung (0 für zufällig) (Standard: 0) | INT | Nein | 0-2147483647 |
| `resolution` | Unterstützte Werte können je nach Modell und Dauer variieren (Standard: "1080p") | COMBO | Nein | `"1080p"` |
| `movement_amplitude` | Die Bewegungsamplitude von Objekten im Frame (Standard: "auto") | COMBO | Nein | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Hinweis:** Die Start- und End-Frames müssen kompatible Seitenverhältnisse aufweisen (validiert mit min_rel=0.8, max_rel=1.25 Toleranz für das Seitenverhältnis).

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Die generierte Videodatei | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `5e8a566373fac84111e90d00c00a6932a23e827f9b4669950c223256c08dd96c`
