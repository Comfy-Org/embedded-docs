# FluxProDepthNode

Dieser Node erzeugt Bilder mithilfe eines Tiefen-Kontrollbilds als Steuerung. Er nimmt ein Kontrollbild und einen Text-Prompt entgegen und erstellt anschließend ein neues Bild, das sowohl den Tiefeninformationen aus dem Kontrollbild als auch der Beschreibung im Prompt folgt. Der Node verbindet sich mit einer externen API, um den Bilderzeugungsprozess durchzuführen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `control_image` | Das Tiefen-Kontrollbild, das zur Steuerung der Bilderzeugung verwendet wird | IMAGE | Ja | - |
| `prompt` | Prompt für die Bilderzeugung (Standard: leere Zeichenkette) | STRING | Nein | - |
| `prompt_upsampling` | Ob ein Upsampling des Prompts durchgeführt werden soll. Wenn aktiviert, wird der Prompt automatisch für eine kreativere Generierung geändert, aber die Ergebnisse sind nicht deterministisch (derselbe Seed erzeugt nicht exakt dasselbe Ergebnis). (Standard: False) | BOOLEAN | Nein | - |
| `skip_preprocessing` | Ob die Vorverarbeitung übersprungen werden soll; auf True setzen, wenn `control_image` bereits ein Tiefenbild ist, auf False, wenn es sich um ein Rohbild handelt. (Standard: False) | BOOLEAN | Nein | - |
| `guidance` | Guidance-Stärke für den Bilderzeugungsprozess (Standard: 15) | FLOAT | Nein | 1-100 |
| `steps` | Anzahl der Schritte für den Bilderzeugungsprozess (Standard: 50) | INT | Nein | 15-50 |
| `seed` | Der Zufallsseed, der zur Erzeugung des Rauschens verwendet wird. (Standard: 0) | INT | Nein | 0-18446744073709551615 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output_image` | Das generierte Bild basierend auf dem Tiefen-Kontrollbild und dem Prompt | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/de.md)

---
**Source fingerprint (SHA-256):** `34b80d7d63158b7dc4ad02da6b3a573b713d77efd0955d3477409f776f964462`
