# FluxProCannyNode

Erzeugt ein Bild mithilfe eines Steuerbilds (Canny). Dieser Node nimmt ein Steuerbild entgegen und generiert ein neues Bild basierend auf dem bereitgestellten Prompt, wobei die im Steuerbild erkannte Kantenstruktur befolgt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `control_image` | Das Eingabebild, das für die Canny-Kantenerkennung als Steuerung verwendet wird | IMAGE | Ja | - |
| `prompt` | Prompt für die Bilderzeugung (Standard: leerer String) | STRING | Nein | - |
| `prompt_upsampling` | Ob ein Upsampling des Prompts durchgeführt werden soll. Wenn aktiviert, wird der Prompt automatisch für eine kreativere Generierung geändert, die Ergebnisse sind jedoch nicht deterministisch (derselbe Seed erzeugt nicht exakt dasselbe Ergebnis). (Standard: False) | BOOLEAN | Nein | - |
| `canny_low_threshold` | Niedriger Schwellenwert für die Canny-Kantenerkennung; wird ignoriert, wenn `skip_preprocessing` True ist (Standard: 0.1) | FLOAT | Nein | 0.01 - 0.99 |
| `canny_high_threshold` | Hoher Schwellenwert für die Canny-Kantenerkennung; wird ignoriert, wenn `skip_preprocessing` True ist (Standard: 0.4) | FLOAT | Nein | 0.01 - 0.99 |
| `skip_preprocessing` | Ob die Vorverarbeitung übersprungen werden soll; auf True setzen, wenn `control_image` bereits als Canny-Bild vorliegt, auf False, wenn es ein Rohbild ist. (Standard: False) | BOOLEAN | Nein | - |
| `guidance` | Stärke der Guidance für den Bilderzeugungsprozess (Standard: 30) | FLOAT | Nein | 1 - 100 |
| `steps` | Anzahl der Schritte für den Bilderzeugungsprozess (Standard: 50) | INT | Nein | 15 - 50 |
| `seed` | Der Zufallsseed, der zum Erzeugen des Rauschens verwendet wird. (Standard: 0) | INT | Nein | 0 - 18446744073709551615 |

**Hinweis:** Wenn `skip_preprocessing` auf True gesetzt ist, werden die Parameter `canny_low_threshold` und `canny_high_threshold` ignoriert, da angenommen wird, dass das Steuerbild bereits als Canny-Kantenbild verarbeitet wurde. Das `control_image` wird dann direkt als vorverarbeitetes Bild verwendet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output_image` | Das generierte Bild basierend auf dem Steuerbild und dem Prompt | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/de.md)

---
**Source fingerprint (SHA-256):** `dedf55a2b2c183519d7f5be0d9a96abbe40716a247f574fc0d50f10f715949a7`
