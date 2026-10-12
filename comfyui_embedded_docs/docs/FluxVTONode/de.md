# FluxVTONode

Dieser Node führt eine virtuelle Anprobe durch, indem er eine Person mit einem bereitgestellten Bekleidungsbild ankleidet. Er sendet die Personen- und Bekleidungsbilder an den BFL Flux VTO-Dienst, der ein realistisches Bild der Person erzeugt, die das Kleidungsstück trägt. Eine optionale Textanweisung kann beschreiben, wie das Kleidungsstück sitzen oder aussehen soll.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `person` | Bild der Person, die angekleidet werden soll. | IMAGE | Ja | - |
| `garment` | Bild des anzuwendenden Kleidungsstücks. | IMAGE | Ja | - |
| `prompt` | Optionale Styling-Anweisung in natürlicher Sprache (z. B. wie das Kleidungsstück sitzen soll). Standardwert ist eine leere Zeichenkette. | STRING | Nein | - |
| `seed` | Der Zufallswert, der für die Erzeugung des Rauschens verwendet wird. Standard: 0. | INT | Nein | 0 bis 18446744073709551615 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das resultierende Bild, das die Person mit dem bereitgestellten Kleidungsstück zeigt. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/de.md)

---
**Source fingerprint (SHA-256):** `5e0777dedcbd6275e31a16f6f5d78f4166147266c0c88531c5843a027702e594`
