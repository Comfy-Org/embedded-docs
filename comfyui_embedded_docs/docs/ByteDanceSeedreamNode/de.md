# ByteDanceSeedreamNode

Der ByteDance Seedream 4.5 & 5.0-Node bietet eine einheitliche Text-zu-Bild-Generierung und präzise Bearbeitung mit einem einzigen Satz bei bis zu 4K-Auflösung. Er kann neue Bilder aus Text-Prompts erstellen oder vorhandene Bilder mithilfe von Textanweisungen bearbeiten. Der Node unterstützt sowohl die Generierung eines einzelnen Bildes als auch die sequenzielle Generierung mehrerer zusammenhängender Bilder.

**Hinweis:** Dieser Node ist im Quellcode als veraltet markiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Seedream-Modell, das für die Generierung verwendet werden soll. | STRING | Ja | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |
| `prompt` | Text-Prompt zum Erstellen oder Bearbeiten eines Bildes. Muss mindestens 1 Zeichen lang sein. | STRING | Ja | - |
| `image` | Eingabebild(er) für die Bild-zu-Bild-Generierung. Referenzbild(er) für die Generierung mit einer oder mehreren Referenzen. Maximal 14 Referenzbilder für seedream-5-0-260128 oder 10 für andere Modelle. | IMAGE | Nein | - |
| `size_preset` | Wählen Sie eine empfohlene Größe. Wählen Sie Custom, um die unten angegebene Breite und Höhe zu verwenden. | STRING | Nein | Mehrere Optionen verfügbar |
| `width` | Benutzerdefinierte Breite für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 6240 (Schritt 2) |
| `height` | Benutzerdefinierte Höhe für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 4992 (Schritt 2) |
| `sequential_image_generation` | Modus für die Gruppenbildgenerierung. "disabled" generiert ein einzelnes Bild. "auto" lässt das Modell entscheiden, ob mehrere zusammenhängende Bilder generiert werden (z. B. Story-Szenen, Charaktervarianten). Standard: "disabled". | STRING | Nein | "disabled"<br>"auto" |
| `max_images` | Maximale Anzahl der zu generierenden Bilder, wenn sequential_image_generation='auto'. Die Gesamtzahl der Bilder (Eingabe + generiert) darf 15 nicht überschreiten. Standard: 1. | INT | Nein | 1 bis 15 (Schritt 1) |
| `seed` | Seed für die Generierung. Standard: 0. | INT | Nein | 0 bis 2147483647 (Schritt 1) |
| `watermark` | Ob dem Bild ein Wasserzeichen "AI generated" hinzugefügt werden soll. Standard: False. | BOOLEAN | Nein | - |
| `fail_on_partial` | Wenn aktiviert, wird die Ausführung abgebrochen, wenn angeforderte Bilder fehlen oder einen Fehler zurückgeben. Standard: True. | BOOLEAN | Nein | - |

**Hinweise zu Parametereinschränkungen:**
- Die minimale Bildauflösung hängt vom ausgewählten Modell ab: 3,68 MP für seedream-4-5- und seedream-5-0-Modelle, 0,92 MP für seedream-4-0-Modelle.
- Die maximale Bildauflösung beträgt 10,4 MP für seedream-5-0-Modelle und 16,78 MP für andere Modelle.
- Referenzbilder müssen ein Seitenverhältnis zwischen 1:3 und 3:1 haben.
- Wenn `sequential_image_generation` auf "auto" gesetzt ist, darf die Gesamtzahl der Eingabebilder plus `max_images` 15 nicht überschreiten.
- Die Parameter `width` und `height` werden nur verwendet, wenn `size_preset` auf "Custom" gesetzt ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Generierte(s) Bild(er) basierend auf den Eingabeparametern und dem Prompt. Gibt einen einzelnen Bildtensor oder einen Batch von Bildtensoren zurück, wenn mehrere Bilder generiert werden. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/de.md)

---
**Source fingerprint (SHA-256):** `78086df431c887c241796ddb5db1ebbfe5b57faab0839da842be81480f1e113b`
