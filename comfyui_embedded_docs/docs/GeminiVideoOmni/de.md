# Google Gemini Omni (Video)

Erzeugen Sie mit dem Gemini Omni Flash-Modell von Google ein Video mit Audio aus einem Text-Prompt. Optional können Sie Referenzbilder und/oder -videos bereitstellen, um das Ergebnis zu steuern oder zu bearbeiten. Beschreiben Sie die gewünschte Länge (3–10 s) und das Seitenverhältnis (16:9 oder 9:16) direkt im Prompt.

**Hinweis:** Dieser Node ist im Quellcode als veraltet markiert.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Gemini-Videomodell, das zum Generieren des Videos verwendet wird. | DYNAMIC_COMBO | Ja | "Omni Flash" |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 42). | INT | Ja | 0 bis 2147483647 |

### Omni Flash Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Beschreibt das zu generierende Video. Geben Sie die Länge und das Seitenverhältnis direkt im Prompt an, z. B. „ein 6-Sekunden-Clip in 16:9“. Die Länge kann 3–10 Sekunden betragen; das Seitenverhältnis muss 16:9 (Querformat) oder 9:16 (Hochformat) sein. Die Ausgabe ist 720p, 24 FPS, mit Audio. | STRING | Ja | Mindestens 1 Zeichen nach Entfernen von Leerzeichen |
| `temperature` | Steuert die Zufälligkeit. Niedriger ist fokussierter/deterministischer, höher ist variabler (Standard: 1.0). | FLOAT | Nein | 0.0 bis 2.0 |
| `top_p` | Nucleus-Sampling: Aus dem kleinsten Token-Set sampeln, dessen kumulative Wahrscheinlichkeit `top_p` erreicht (Standard: 0.95). | FLOAT | Nein | 0.0 bis 1.0 |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Erweiterbarer Slot: Verbinden Sie ein oder mehrere Referenzbilder (`image_1`...`image_14`), um das Video zu steuern oder zu animieren. Insgesamt bis zu 14 Bilder. | IMAGE | Nein | 0 bis 14 Bilder |
| `videos` | Erweiterbarer Slot: Verbinden Sie ein oder mehrere Referenzvideos (`video_1`...`video_3`), um das Video zu steuern oder zu bearbeiten. Bis zu 3 Videos, jeweils bis zu 10 Sekunden lang. | VIDEO | Nein | 0 bis 3 Videos, jeweils max. 10 Sekunden |

Hinweise:
- Wenn eine Bildeingabe mehrere Frames enthält, wird jeder Frame auf das Maximum von 14 Bildern angerechnet.
- Wenn Referenzbilder oder -videos bereitgestellt werden, muss die gesamte kodierte Mediengröße unter etwa 90 MB bleiben; andernfalls löst der Node einen Fehler aus.
- Wenn keine Referenzbilder oder -videos bereitgestellt werden, generiert der Node das Video nur aus dem Text-Prompt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das generierte Video mit Audio vom Gemini-Modell. | VIDEO |
| `STRING` | Jede Textantwort des Modells, z. B. Begründungen oder Erklärungen. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/de.md)

---
**Source fingerprint (SHA-256):** `da533824adf93b7502465cf985941f70e0ae4d6813c951f4ffa98c007437c03c`
