# MOSS-Image Color/Depth Control

Fügt die Farbregions- und Tiefenkarten eines MOSS-Image-Farb-/Tiefen-Control-Adapters dem Conditioning hinzu. Verbinden Sie die positiven und negativen Conditionings, ein VAE und eine oder beide Karten: Die Karten werden in Latents kodiert, zu einem Farb-/Tiefen-Steuersignal zusammengeführt und an das Conditioning für den von Ihnen gewählten Teil des Samplings angehängt. Verwenden Sie ihn zusammen mit einem MOSS-Image-Control-Adapter, der über einen LoRA-Loader geladen wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Positives Conditioning, an das das Steuersignal angehängt wird. | CONDITIONING | Ja | N/A |
| `negative` | Negatives Conditioning, an das das Steuersignal angehängt wird. | CONDITIONING | Ja | N/A |
| `vae` | VAE, mit dem die Karten in Latents kodiert werden. | VAE | Ja | N/A |
| `color_map` | Eine einheitliche Farbe pro Region in der Ausgabegröße. Die Farben sind nur Regions-IDs. | IMAGE | Nein | N/A |
| `depth_map` | Tiefenkarte in der Ausgabegröße; nahe Bereiche sind weiß. | IMAGE | Nein | N/A |
| `strength` | Skaliert den Beitrag der Karten zu den Bild-Tokens. 0.0 entspricht keinen Karten, 1.0 entspricht der trainierten Stärke (Standard: 1.0). | FLOAT | Ja | 0.0 bis 10.0 (Schritt 0.01) |
| `start_percent` | Sampling-Prozentsatz, bei dem die Steuerung beginnt (Standard: 0.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt 0.001) |
| `end_percent` | Sampling-Prozentsatz, bei dem die Steuerung endet. Ein frühes Beenden behält Layout und Tiefe bei, während die übrigen Schritte die Formen lockern (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt 0.001) |

**Hinweis:** Verbinden Sie mindestens eine der Karten `color_map` und `depth_map`; ohne eine von beiden gibt der Node die Conditionings unverändert zurück. Eine fehlende Karte wird durch Nullen ersetzt, sodass sowohl reine Farb- als auch reine Tiefen-Setups funktionieren. Wenn sich die beiden Karten in ihrer Größe unterscheiden, wird die kleinere auf die Größe der anderen hochskaliert. Dieser Node ist in ComfyUI als experimentell gekennzeichnet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Das positive Conditioning mit angehängtem Steuersignal. | CONDITIONING |
| `negative` | Das negative Conditioning mit angehängtem Steuersignal. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageControl/de.md)

---
**Source fingerprint (SHA-256):** `c4a40c76f26237408e47cb9f683c13bccc3507bd775bec1b89919947a308c115`
