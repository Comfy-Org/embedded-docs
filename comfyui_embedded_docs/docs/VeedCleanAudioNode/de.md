# VEED Clean Audio

Entfernen Sie Hintergrundgeräusche aus Sprache mit VEED. Es ist für Sprache in jeder Sprache konzipiert: Geräusche unter der Stimme werden bereinigt, Pausen werden vollständig bereinigt und Musik sowie Soundeffekte werden entfernt statt beibehalten. Die Ausgabe ist 48 kHz Mono-Audio.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Sprachaufnahme, kürzer als 30 Minuten. | AUDIO | Ja | Bis zu 1799 Sekunden |
| `strength` | Wie viel Rauschen unter der Sprache entfernt wird. Niedrigere Werte behalten mehr Raumklang hinter der Stimme; Pausen zwischen Wörtern werden immer vollständig bereinigt, und Werte über dem Standardwert ändern wenig. (Standard: 0.874) | FLOAT | Ja | 0.0 bis 1.0 (Schritt 0.001) |
| `loudness` | Ob die Ausgangslautstärke normalisiert werden soll. `"normalize"` setzt die Ausgabe auf `target_lufs`; `"keep input level"` belässt den Pegel unverändert. Die Auswahl einer Option zeigt deren Parameter an. (Standard: `"normalize"`) | DYNAMIC_COMBO | Ja | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | Integrierte Lautheit der Ausgabe in LUFS. Spitzenwerte werden bei -1.1 dBTP begrenzt, sodass laute Ziele früh stoppen (etwa -15 LUFS für typische Sprache). Verfügbar, wenn `loudness` auf `"normalize"` gesetzt ist (Standard: -19.0). | FLOAT | Ja | -40.0 bis -8.0 (Schritt 0.1) |

Der Node bricht mit einem Fehler ab, wenn die Aufnahme länger als 1799 Sekunden ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `AUDIO` | Die bereinigte Sprache als 48 kHz Mono-Audio. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanAudioNode/de.md)

---
**Source fingerprint (SHA-256):** `c85949385109a5d320e52619e9df17c245b19f8f16cc1a0b69a37ae2e7bb5b6d`
