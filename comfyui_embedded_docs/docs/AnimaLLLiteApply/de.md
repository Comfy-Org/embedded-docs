# Anima LLLite anwenden

AnimaLLLiteApply wendet einen leichten Animations-Patch auf ein Diffusionsmodell an und ermöglicht so eine kontrollierte Bild-zu-Bild-Generierung mit anpassbarer Stärke und Zeitsteuerung. Es kombiniert einen vorkonfigurierten Modell-Patch mit einem Eingabebild und einer optionalen Maske und modifiziert die Attention- und MLP-Schichten des Modells, um den Generierungsprozess zu beeinflussen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Basis-Diffusionsmodell, auf das der Patch angewendet wird | MODEL | Ja | |
| `model_patch` | Der vorkonfigurierte Animations-Patch, der angewendet wird | MODEL_PATCH | Ja | |
| `image` | Das Referenzbild zur Steuerung der Generierung. Es werden nur die ersten 3 Farbkanäle (RGB) verwendet | IMAGE | Ja | |
| `strength` | Die Stärke des Patch-Effekts (Standard: 1.0, Schrittweite: 0.01) | FLOAT | Ja | -10.0 bis 10.0 |
| `start_percent` | Der Prozentsatz des Denoising-Prozesses, ab dem der Patch wirksam wird (Standard: 0.0, Schrittweite: 0.001) | FLOAT | Ja | 0.0 bis 1.0 |
| `end_percent` | Der Prozentsatz des Denoising-Prozesses, ab dem der Patch nicht mehr wirksam ist (Standard: 1.0, Schrittweite: 0.001) | FLOAT | Ja | 0.0 bis 1.0 |
| `mask` | Eine optionale Maske, um den Patch-Effekt auf bestimmte Bereiche des Bildes zu beschränken | MASK | Nein | |

**Hinweis zu Parametereinschränkungen:** Wenn der `model_patch` 4 Eingabekanäle hat und keine `mask` angegeben wird, wird automatisch eine Nullmaske erstellt, die zu den Bildabmessungen passt. Wenn der `model_patch` keine 4 Eingabekanäle hat, wird der Parameter `mask` ignoriert und auf `None` gesetzt. Es werden nur die ersten 3 Farbkanäle des Eingabebilds verwendet. Dieser Node ist in ComfyUI als experimentell gekennzeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `MODEL` | Das gepatchte Diffusionsmodell mit angewendetem Animations-Patch | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/de.md)

---
**Source fingerprint (SHA-256):** `48e455b767509a5a8c329365d5ffded86d6f4545d575c9fdc5ffbaf4da7c2287`
