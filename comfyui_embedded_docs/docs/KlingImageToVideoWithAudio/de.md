# Kling 2.6 Bild (erstes Frame) zu Video mit Audio

Der Node „Kling Image(First Frame) to Video with Audio“ verwendet das Kling AI-Modell, um aus einem einzelnen Startbild und einem Text-Prompt ein kurzes Video zu generieren. Er erzeugt eine Videosequenz, die mit dem bereitgestellten Bild beginnt und optional KI-generiertes Audio enthalten kann, das die visuellen Inhalte begleitet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Die spezifische Version des Kling AI-Modells, die für die Videogenerierung verwendet werden soll. | COMBO | Ja | `"kling-v2-6"` |
| `start_frame` | Das Bild, das als erstes Frame des generierten Videos dient. Das Bild muss mindestens 300x300 Pixel groß sein und ein Seitenverhältnis zwischen 1:2.5 und 2.5:1 haben. | IMAGE | Ja | - |
| `prompt` | Positiver Text-Prompt. Dieser beschreibt den Videoinhalt, den Sie generieren möchten. Der Prompt muss zwischen 1 und 2500 Zeichen lang sein. | STRING | Ja | - |
| `mode` | Der Betriebsmodus für die Videogenerierung. | COMBO | Ja | `"pro"` |
| `duration` | Die Länge des zu generierenden Videos in Sekunden. | COMBO | Ja | `5`<br>`10` |
| `generate_audio` | Wenn aktiviert, generiert der Node Audio zum Video. Wenn deaktiviert, ist das Video stumm. (Standard: True) | BOOLEAN | Nein | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Die generierte Videodatei, die je nach Eingabe `generate_audio` Audio enthalten kann. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/de.md)

---
**Source fingerprint (SHA-256):** `e0b834a297f7afd72cfb779a92557f0dc680eacd4d0e18bab0e7c59ae8624965`
