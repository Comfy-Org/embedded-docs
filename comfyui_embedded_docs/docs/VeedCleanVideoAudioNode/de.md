# VEED Clean Audio (in Video)

Entfernen Sie Hintergrundgeräusche aus der Sprache in einem Video mit VEED. Nur die Tonspur ändert sich: Sie wird durch die bereinigte 48-kHz-Mono-Sprache ersetzt, während Bild, Auflösung und Bildrate unverändert bleiben. Es ist für Sprache in jeder Sprache geeignet, und Musik sowie Soundeffekte werden entfernt und nicht beibehalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Video mit einer Sprach-Tonspur, kürzer als 30 Minuten. Das Video muss eine Audiospur enthalten. | VIDEO | Ja | Bis zu 1799 Sekunden |
| `strength` | Wie stark Rauschen unter der Sprache entfernt wird. Ein niedrigerer Wert behält mehr Raumklang hinter der Stimme bei; Pausen zwischen Wörtern werden immer vollständig bereinigt, und Werte über dem Standardwert ändern wenig. (Standard: 0.874) | FLOAT | Ja | 0.0 bis 1.0 (Schritt 0.001) |
| `loudness` | Ob die Sprachlautstärke normalisiert werden soll. `"normalize"` setzt sie auf `target_lufs`; `"keep input level"` belässt die Lautstärke unverändert. Bei Auswahl einer Option werden ihre Parameter eingeblendet. (Standard: `"normalize"`) | DYNAMIC_COMBO | Ja | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | Integrierte Lautheit der bereinigten Sprache in LUFS. Spitzenwerte werden auf -1.1 dBTP begrenzt, daher stoppen laute Zielwerte früh (etwa -15 LUFS bei typischer Sprache). Verfügbar, wenn `loudness` auf `"normalize"` steht (Standard: -19.0). | FLOAT | Ja | -40.0 bis -8.0 (Schritt 0.1) |

Der Node bricht mit einem Fehler ab, wenn der Clip länger als 1799 Sekunden ist und wenn das Video keine Audiospur hat.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `VIDEO` | Das Eingabevideo, dessen Tonspur durch die bereinigte Sprache ersetzt wurde. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanVideoAudioNode/de.md)

---
**Source fingerprint (SHA-256):** `b8ff533f3ce45691cccd3449596252b0216178fdef0e7e728ccccbc9a8712217`
