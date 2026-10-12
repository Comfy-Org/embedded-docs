# BriaIncreaseResolution

Bria Increase Resolution skaliert ein Eingabebild um das 2- oder 4-Fache mithilfe des Bild-Upscaling-Dienstes von Bria hoch, wobei der ursprüngliche Inhalt erhalten bleibt. Der Node lädt das Bild hoch, reicht es zur Verarbeitung beim Bria-Dienst ein, wartet auf das Ergebnis und gibt das hochskalierte Bild zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `image` | Das Eingabebild, das hochskaliert werden soll. | IMAGE | Ja | Einzelbild |
| `desired_increase` | Auflösungsmultiplikator. Die Ausgabe darf auf jeder Seite 8192 Pixel nicht überschreiten. | COMBO | Ja | "2"<br>"4" |
| `auto_downscale` | Verringert automatisch den Multiplikator und skaliert das Eingabebild herunter, falls dies noch nicht ausreicht, wenn die Ausgabe den Grenzwert überschreiten würde. (Standard: False) | BOOLEAN | Ja | True<br>False |
| `moderation` | Moderationseinstellungen. Wenn auf "true" gesetzt, werden die Unteroptionen `visual_input_moderation` und `visual_output_moderation` aktiviert, die beide standardmäßig auf False gesetzt sind. | DYNAMIC_COMBO | Ja | "false"<br>"true" |

Hinweise:
- Wenn `moderation` auf "true" gesetzt ist, werden die Unteroptionen `visual_input_moderation` und `visual_output_moderation` verfügbar, die beide standardmäßig auf False gesetzt sind. Sie steuern die Moderation des Eingabebilds und des Inhalts des Ausgabebilds.
- Der Node erzwingt eine maximale Seitenlänge der Ausgabe von 8192 Pixeln. Wenn der ausgewählte Multiplikator diesen Grenzwert überschreiten würde und `auto_downscale` deaktiviert ist, wird ein Fehler ausgelöst. Wenn `auto_downscale` aktiviert ist, kann der Node stattdessen automatisch einen niedrigeren Multiplikator verwenden oder das Eingabebild herunterskalieren.
- Bria vergrößert zunächst die kurze Seite des Eingabebilds auf mindestens 224 Pixel, bevor die Hochskalierung erfolgt. Zu stark gestreckte Bilder können einen Fehler auslösen, der dazu auffordert, sie auf eine quadratischere Form zuzuschneiden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `IMAGE` | Das hochskalierte Bild, das vom Bria-Dienst zurückgegeben wird. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/de.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
