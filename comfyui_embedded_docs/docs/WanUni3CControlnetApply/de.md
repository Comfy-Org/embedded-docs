# Wan Uni3C ControlNet anwenden

## Übersicht

Dieser Node wendet ein Uni3C ControlNet auf ein Wan-Video-Diffusionsmodell an und verwendet ein gerendertes Führungsvideo (z. B. gewarpete Punktwolken-Renderings), um die Ausgabe des Modells zu beeinflussen. Er injiziert Steuersignale in bestimmte Blockebenen und ermöglicht so eine kameratrajektoriebasierte Steuerung während der Videogenerierung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das Wan-Diffusionsmodell, das gepatcht werden soll. | MODEL | Ja | – |
| `model_patch` | Ein Uni3C ControlNet-Patch (muss eine Instanz von `comfy.ldm.wan.uni3c.WanUni3CControlnet` sein). | MODEL_PATCH | Ja | – |
| `vae` | Der VAE, der zum Kodieren des Führungsvideos in Latents verwendet wird. | VAE | Ja | – |
| `render_video` | Das aus der Kameratrajektorie gerenderte Führungsvideo, am häufigsten gewarpete Punktwolken-Renderings des Eingabebilds. | IMAGE | Ja | – |
| `strength` | Die Stärke des angewendeten Steuersignals. | FLOAT | Ja | -10.0 bis 10.0 (Standard: 1.0) |
| `start_percent` | Der Prozentsatz des Denoising-Prozesses, bei dem die Steuerung beginnt. | FLOAT | Ja | 0.0 bis 1.0 (Standard: 0.0) |
| `end_percent` | Der Prozentsatz des Denoising-Prozesses, bei dem die Steuerung endet. | FLOAT | Ja | 0.0 bis 1.0 (Standard: 1.0) |

**Hinweise:**
- Der `model_patch` muss ein Uni3C ControlNet sein; andernfalls löst der Node einen Fehler aus.
- Das Uni3C ControlNet funktioniert nur mit Wan-Modellen; es wird ein Fehler ausgelöst, wenn das Modell nicht auf Wan basiert.
- Die interne Dimension des ControlNet muss mit der Dimension des Wan-Modells übereinstimmen – bei Abweichungen wird ein Fehler ausgelöst.
- Das `render_video`-Eingabebild wird im RGB-Format erwartet (nur die ersten 3 Kanäle werden verwendet).
- Dieser Node ist experimentell.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `MODEL` | Das gepatchte Wan-Modell mit angewendetem Uni3C ControlNet. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanUni3CControlnetApply/de.md)

---
**Source fingerprint (SHA-256):** `f69253f06aba9208778f713ad36e9995f53a15d2e61243b853b9ac9131637371`
