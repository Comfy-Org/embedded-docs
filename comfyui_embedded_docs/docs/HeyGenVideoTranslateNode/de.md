# HeyGenVideoTranslateNode

Übersetzen Sie ein gesprochenes Video mit Voice-Cloning und Lip-Sync in eine andere Sprache. Dieser Node klont die Stimme des ursprünglichen Sprechers und animiert den Mund neu, damit er zur übersetzten Sprachausgabe passt, wodurch ein natürlich wirkendes Ergebnis entsteht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Video mit zu übersetzender Sprachaufnahme. | VIDEO | Ja | - |
| `output_language` | Zielsprache für das übersetzte Video. | COMBO | Ja | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `mode` | 'speed' ist schneller; 'precision' erzeugt Lip-Sync in höherer Qualität zu einem höheren Preis. (Standard: "speed") | COMBO | Ja | "speed"<br>"precision" |
| `translate_audio_only` | Nur die Audiospur austauschen, wobei die ursprünglichen Mundbewegungen beibehalten werden (kein Lip-Sync). (Standard: False) | BOOLEAN | Nein | True<br>False |
| `speaker_count` | Anzahl der Sprecher im Video. 0 = automatisch erkennen. Werte über 0 werden als Anzahl der Sprecher an die API gesendet. (Standard: 0) | INT | Nein | 0 bis 10 |
| `seed` | Wird nicht an HeyGen gesendet; ändern Sie ihn, um einen erneuten Durchlauf zu erzwingen. (Standard: 42) | INT | Nein | 0 bis 2147483647 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das übersetzte Video mit angewendetem Voice-Cloning und Lip-Sync. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/de.md)

---
**Source fingerprint (SHA-256):** `709438c0c713d6db750643cc48f75352c6f293ae1ff2fd82c1bacb03b2581923`
