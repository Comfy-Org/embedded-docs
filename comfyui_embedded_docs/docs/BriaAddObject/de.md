# Bria Objekt hinzufügen

Dieser Node fügt ein in Klartext beschriebenes Objekt mithilfe von Bria in ein Bild ein. Bria rendert das gesamte Bild mit etwa 1 Megapixel neu, sodass das Ergebnis nicht pixelgenau zum Eingabebild ausgerichtet ist.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Bild, dem das beschriebene Objekt hinzugefügt wird. Der Alphakanal wird vor dem Hochladen des Bildes entfernt. | IMAGE | Ja | - |
| `instruction` | Was hinzugefügt werden soll und wo, zum Beispiel 'Platzieren Sie eine rote Vase mit Blumen auf dem Tisch'. Darf nicht leer sein. Standard: "" (leere Zeichenkette). | STRING | Ja | - |
| `seed` | Bria verwendet hier keinen Seed und erzeugt die Bearbeitung bei jedem Aufruf neu, sodass wiederholte Ausführungen abweichen können. Der Wert wird nie gesendet: Er ändert nur den Cache-Schlüssel dieses Nodes, damit ein ansonsten identischer Graph die Bearbeitung erneut ausführt, anstatt das zwischengespeicherte Ergebnis zurückzugeben. Standard: 42. | INT | Ja | 0 bis 2147483647 |
| `moderation` | Moderationseinstellungen. Wählen Sie "true", um die unten stehenden Moderation-Flags einzublenden. | DYNAMIC_COMBO | Ja | "false"<br>"true" |

### Eingaben bei aktivierter Moderation

Verfügbar, wenn `moderation` auf "true" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Aktiviert die Inhaltsmoderation für das Eingabebild. Standard: False. | BOOLEAN | Nein | True / False |
| `visual_output_moderation` | Aktiviert die Inhaltsmoderation für das generierte Ausgabebild. Standard: False. | BOOLEAN | Nein | True / False |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das bearbeitete Bild mit dem hinzugefügten beschriebenen Objekt. | IMAGE |
| `structured_prompt` | Strukturierte Beschreibung des bearbeiteten Bildes für eine nachfolgende Bearbeitung mit Bria FIBO Image Edit. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaAddObject/de.md)

---
**Source fingerprint (SHA-256):** `41c9a3e511763372d8dc8be9da4f70158e53d5156a88eb3c66f81149efdbd566`
