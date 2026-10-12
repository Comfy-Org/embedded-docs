# Luma Ray 3.2 Video neu einrahmen

Dieser Node ändert das Seitenverhältnis eines vorhandenen Videos mit Luma Ray 3.2, wodurch die neu freigelegten Leinwandbereiche mit generierten Inhalten gefüllt werden. Das Quellvideo kann bis zu 30 Sekunden lang sein, und die Abrechnung erfolgt pro Sekunde der Ausgabe.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Quellvideo, das neu gerahmt werden soll. Bis zu 30 Sekunden. | VIDEO | Ja | - |
| `prompt` | Beschreibt, wie die neu freigelegten Leinwandbereiche gefüllt werden sollen. | STRING | Ja | Min. Länge: 1 Zeichen<br>Max. Länge: 6000 Zeichen |
| `aspect_ratio` | Das Zielseitenverhältnis für das neu gerahmte Video (Standard: "16:9"). | STRING | Ja | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9" |
| `resolution` | Die Ausgabeauflösung des neu gerahmten Videos (Standard: "720p"). | STRING | Ja | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `seed` | Seed für reproduzierbare Generierung. | INT | Ja | - |

**Hinweis:** Die `1080p`-Auflösung ist bei vertikalen Seitenverhältnissen (`9:16` und `3:4`) beim Neu-Rahmen nicht verfügbar.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das neu gerahmte Video mit dem neuen Seitenverhältnis und gefüllten Leinwandbereichen. | VIDEO |
| `generation_id` | Der eindeutige Bezeichner für die Generierungsanfrage. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoReframeNode/de.md)

---
**Source fingerprint (SHA-256):** `d35ff5b63a850e4e44a40857188918ab5cde00b9159e3720a189a81807cfa7cb`
