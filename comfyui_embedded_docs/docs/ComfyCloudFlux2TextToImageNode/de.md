# Comfy Cloud Flux 2 Text zu Bild [BETA]

Führt das Flux 2 dev Text-zu-Bild-Modell auf einer Comfy Cloud GPU aus und gibt das generierte Bild zurück. Die Option `turbo` wendet das Turbo LoRA mit einem kurzen Zeitplan für einen deutlich schnelleren Lauf an, auf Kosten einer etwas geringeren Wiedergabetreue; wenn sie deaktiviert wird, wird der vollständige Dev-Durchlauf ohne das LoRA ausgeführt. Dies ist ein Beta-Node-Set, dessen Abrechnung auf der Laufzeit in Credits basiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Der Text-Prompt, der das zu generierende Bild beschreibt. Führende und nachfolgende Leerzeichen werden vor der Übermittlung entfernt. | STRING | Ja | 1 bis 4096 Zeichen |
| `seed` | Zufälliger Seed, der das generierte Ergebnis zur Reproduzierbarkeit steuert (Standard: 42). | INT | Ja | 0 bis 18446744073709551615 |
| `aspect_ratio` | Seitenverhältnis des Ausgabebilds (Standard: "1:1"). | COMBO | Ja | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Gesamtes Pixelbudget. 1.0 entspricht etwa 1024x1024 bei quadratischem Seitenverhältnis (Standard: 1.0). | FLOAT | Ja | 0.1 bis 16.0 (Schritt 0.1) |
| `turbo` | Führt das Turbo LoRA mit einem kurzen Zeitplan aus und tauscht etwas Wiedergabetreue gegen einen deutlich schnelleren Lauf. Aus führt den vollständigen Dev-Lauf ohne LoRA aus (Standard: True). | BOOLEAN | Ja | True / False |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das aus dem Text-Prompt generierte Bild, zurückgegeben als ComfyUI-Bildtensor, der an andere Nodes übergeben werden kann. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudFlux2TextToImageNode/de.md)

---
**Source fingerprint (SHA-256):** `1b51a8ab89ae7c355dec4256a1a25a09a15e192c72fc8d1862c652dbdf337fcb`
