# Comfy Cloud Z-Image Turbo Text zu Bild [BETA]

Dieser Node generiert ein Bild aus einem Text-Prompt mithilfe des Z-Image Turbo-Modells, das in nur 8 Schritten fertig wird. Die Generierung läuft remote auf Comfy Cloud GPUs und wird nach der Laufzeit abgerechnet, wodurch dies eine der schnellsten und günstigsten Optionen hier ist, um Bildideen zu iterieren. Sobald die Generierung abgeschlossen ist, lädt der Node das fertige Bild herunter, damit es in Ihrem Workflow verwendet werden kann. Dieser Node ist Teil des Comfy Cloud Node-Sets, das als BETA gekennzeichnet ist: Optionen können hinzugefügt oder entfernt werden und ein Workflow kann außer Betrieb genommen werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt, der das zu generierende Bild beschreibt. Akzeptiert mehrzeilige Eingabe und wird vor dem Absenden getrimmt. Darf nach dem Trimmen nicht leer sein. Standard: "" (leer). | STRING | Ja | 1 - 4096 Zeichen |
| `seed` | Zufälliger Seed zur Steuerung der Reproduzierbarkeit der Generierung. Eine Änderung erzeugt eine andere Variation. Enthält eine Option zur Steuerung nach der Generierung. Standard: 42. | INT | Nein | 0 - 18446744073709551615 |
| `aspect_ratio` | Seitenverhältnis des generierten Bildes. Standard: "1:1". | COMBO | Nein | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Gesamtes Pixelbudget. 1.0 entspricht ungefähr 1024x1024 bei quadratischem Seitenverhältnis. Standard: 1.0. | FLOAT | Nein | 0.1 - 16.0<br>(Schrittweite 0.1) |

Hinweis: Eingabewerte werden validiert, bevor die Generierung übermittelt wird. Der `prompt` muss nach dem Entfernen von Leerraum zwischen 1 und 4.096 Zeichen enthalten, `aspect_ratio` muss eine der aufgeführten Optionen sein und `megapixels` muss in Schritten von 0.1 eingegeben werden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das generierte Bild, zurückgegeben als Bild-Tensor, bereit für weitere Bildverarbeitungs- oder Speicher-Nodes. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudZImageTurboNode/de.md)

---
**Source fingerprint (SHA-256):** `9c78bf9aca5800212d1c5a8f9581dc6c154a82220cd60a8b55ebe74111d2f542`
