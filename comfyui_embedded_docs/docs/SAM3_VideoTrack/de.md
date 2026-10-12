# SAM3_VideoTrack

Verfolgen Sie Objekte über Videoframes hinweg mit dem speicherbasierten Tracker von SAM3. Der Node verarbeitet eine Sequenz von Videoframes und behält Objektidentitäten über Frames hinweg bei, wobei entweder initiale Masken oder Text-Prompts verwendet werden, um festzulegen, was verfolgt werden soll, und kann dabei neue Objekte mithilfe von Textkonditionierung erkennen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Videoframes als gebatchte Bilder | IMAGE | Ja | Gebatchte Videoframes |
| `model` | Das für die Verfolgung zu verwendende SAM3-Modell | MODEL | Ja | SAM3-Modell |
| `initial_mask` | Maske(n) für den ersten zu verfolgenden Frame (eine pro Objekt) | MASK | Nein | Eine Maske pro Objekt |
| `conditioning` | Textkonditionierung zum Erkennen neuer Objekte während der Verfolgung | CONDITIONING | Nein | Textkonditionierung |
| `detection_threshold` | Score-Schwellenwert für die Erkennung per Text-Prompt (Standard: 0.5) | FLOAT | Nein | 0.0 bis 1.0 (Schritt 0.01) |
| `max_objects` | Maximale Anzahl verfolgter Objekte. Initiale Masken werden auf dieses Limit angerechnet. 0 verwendet die interne Obergrenze von 64. (Standard: 4) | INT | Nein | 0 bis 64 |
| `detect_interval` | Erkennung alle N Frames ausführen (1 = jeder Frame). Höhere Werte sparen Rechenleistung. (Standard: 1) | INT | Nein | 1 oder höher |

**Hinweis:** Entweder `initial_mask` oder `conditioning` muss angegeben werden. Wenn beide fehlen, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `track_data` | Tracking-Daten, die Objektmasken und Metadaten über alle Videoframes hinweg enthalten | SAM3_TRACK_DATA |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/de.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
