# ViduReferenceVideoNode

Der Vidu Reference Video Node generiert Videos aus mehreren Referenzbildern und einem Text-Prompt. Er verwendet KI-Modelle, um konsistenten Videoinhalt auf Grundlage der bereitgestellten Bilder und Beschreibung zu erstellen. Der Node unterstützt verschiedene Videoeinstellungen, einschließlich Dauer, Seitenverhältnis, Auflösung und Bewegungssteuerung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Modellname für die Videoerzeugung (Standard: "viduq1") | COMBO | Ja | `"viduq1"` |
| `images` | Bilder, die als Referenzen verwendet werden, um ein Video mit konsistenten Subjekten zu generieren (maximal 7 Bilder) | IMAGE | Ja | - |
| `prompt` | Eine textuelle Beschreibung für die Videoerzeugung | STRING | Ja | - |
| `duration` | Dauer des Ausgabevideos in Sekunden (Standard: 5) | INT | Nein | 5-5 |
| `seed` | Seed für die Videoerzeugung (0 für zufällig) (Standard: 0) | INT | Nein | 0-2147483647 |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos | COMBO | Nein | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `resolution` | Unterstützte Werte können je nach Modell und Dauer variieren (Standard: "1080p") | COMBO | Nein | `"1080p"` |
| `movement_amplitude` | Die Bewegungsamplitude von Objekten im Frame (Standard: "auto") | COMBO | Nein | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Einschränkungen und Begrenzungen:**

- Das Feld `prompt` ist erforderlich und darf nicht leer sein
- Maximal 7 Bilder als Referenz zulässig
- Jedes Bild muss ein Seitenverhältnis zwischen 1:4 und 4:1 haben
- Jedes Bild muss eine Mindestgröße von 128x128 Pixeln haben
- Die Dauer ist fest auf 5 Sekunden eingestellt

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Das generierte Video basierend auf den Referenzbildern und dem Prompt | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `087ce07dbf0bdad9dcb1f1487dd95cf1b50d627cc8b1f8a17ff26d74016c2c3e`
