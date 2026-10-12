# TopazVideoEnhance

Der Node Topaz Video Enhance verleiht Videos mit leistungsstarker Upscaling- und Wiederherstellungstechnologie neues Leben und nutzt eine externe API zur Verbesserung der Videoqualität. Er kann die Videoauflösung hochskalieren, die Bildrate durch Interpolation erhöhen und Kompression anwenden. Der Node verarbeitet ein eingehendes MP4-Video und gibt eine verbesserte Version basierend auf den ausgewählten Einstellungen zurück. Dieser Node ist als veraltet (Legacy) markiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Die eingehende Videodatei, die verbessert werden soll. | VIDEO | Ja | - |
| `upscaler_enabled` | Aktiviert oder deaktiviert die Video-Upscaling-Funktion (Standard: True). | BOOLEAN | Ja | - |
| `upscaler_model` | Das KI-Modell, das zum Hochskalieren des Videos verwendet wird. | COMBO | Ja | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` |
| `upscaler_resolution` | Die Zielauflösung für das hochskalierte Video. | COMBO | Ja | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_creativity` | Kreativitätsstufe (gilt nur für Starlight (Astra) Creative). (Standard: "low") | COMBO | Nein | `"low"`<br>`"middle"`<br>`"high"` |
| `interpolation_enabled` | Aktiviert oder deaktiviert die Frame-Interpolation-Funktion (Standard: False). | BOOLEAN | Nein | - |
| `interpolation_model` | Das für die Frame-Interpolation verwendete Modell (Standard: "apo-8"). | COMBO | Nein | `"apo-8"` |
| `interpolation_slowmo` | Auf das Eingabevideo angewendeter Zeitlupenfaktor. Beispielsweise bewirkt 2, dass die Ausgabe doppelt so langsam ist und sich die Dauer verdoppelt. (Standard: 1) | INT | Nein | 1 bis 16 |
| `interpolation_frame_rate` | Ausgabebildrate. (Standard: 60) | INT | Nein | 15 bis 240 |
| `interpolation_duplicate` | Analysiert die Eingabe auf doppelte Frames und entfernt diese. (Standard: False) | BOOLEAN | Nein | - |
| `interpolation_duplicate_threshold` | Erkennungsempfindlichkeit für doppelte Frames. (Standard: 0.01) | FLOAT | Nein | 0.001 bis 0.1 |
| `dynamic_compression_level` | CQP-Stufe. (Standard: "Low") | COMBO | Nein | `"Low"`<br>`"Mid"`<br>`"High"` |

**Hinweis:** Mindestens eine Verbesserungsfunktion muss aktiviert sein. Der Node löst einen Fehler aus, wenn sowohl `upscaler_enabled` als auch `interpolation_enabled` auf False gesetzt sind. Das eingehende Video muss im MP4-Format vorliegen. Die Einstellung `upscaler_creativity` gilt nur, wenn `upscaler_model` auf "Starlight (Astra) Creative" gesetzt ist. Sehr große Videodateien, die Multipart-Uploads erfordern, werden nicht unterstützt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Die verbesserte Ausgabevideodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/de.md)

---
**Source fingerprint (SHA-256):** `b3b14a301b529256ddf04b7e3a9b99814ad5bfa149366b2a5c51c396dbffb190`
