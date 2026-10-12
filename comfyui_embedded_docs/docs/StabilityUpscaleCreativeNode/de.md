# StabilityUpscaleCreativeNode

Skaliert ein Bild mit minimalen Änderungen auf 4K-Auflösung hoch. Dieser Node verwendet die kreative Upscaling-Technologie von Stability AI, um die Bildauflösung zu verbessern, während der ursprüngliche Inhalt erhalten bleibt und subtile kreative Details hinzugefügt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das hochskaliert werden soll | IMAGE | Ja | - |
| `prompt` | Was Sie im Ausgabebild sehen möchten. Ein starker, beschreibender Prompt, der Elemente, Farben und Motive klar definiert, führt zu besseren Ergebnissen. (Standard: leere Zeichenkette) | STRING | Ja | - |
| `creativity` | Steuert die Wahrscheinlichkeit, zusätzliche Details zu erzeugen, die nicht stark durch das Initialbild konditioniert werden. (Standard: 0.3) | FLOAT | Ja | 0.1-0.5 |
| `style_preset` | Optionaler gewünschter Stil des generierten Bildes. (Standard: "None") | STRING | Ja | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` |
| `seed` | Der Zufallsseed, der zur Erzeugung des Rauschens verwendet wird. (Standard: 0) | INT | Ja | 0-4294967294 |
| `negative_prompt` | Schlüsselwörter für Inhalte, die Sie im Ausgabebild nicht sehen möchten. Dies ist eine erweiterte Funktion. (Standard: leere Zeichenkette) | STRING | Nein | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das hochskalierte Bild in 4K-Auflösung | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/de.md)

---
**Source fingerprint (SHA-256):** `dc9bfacee3bfa663cff22cd0bcef6759f7808e2ae8e19526de28d55a3bef26e6`
