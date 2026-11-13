# MiniMax H3 Image

Erzeugt Bilder aus Text mit MiniMax H3 Image oder bearbeitet und kombiniert bis zu 16 Referenzbilder. Der Prompt verweist in der Reihenfolge der Verbindungen auf die Referenzen: `@Image1`, `@Image2` und so weiter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | `MiniMax-H3-Image` oder `MiniMax-H3-Image-Highspeed` für schnellere Läufe. Standard: `"MiniMax-H3-Image"`. | COMBO | Ja | `"MiniMax-H3-Image"`<br>`"MiniMax-H3-Image-Highspeed"` |
| `prompt` | Was generiert werden soll oder wie die Referenzen bearbeitet werden sollen. Bei verbundenen Referenzbildern sind höchstens 8.000 Zeichen möglich. Standard: leer. | STRING | Ja | 1 bis 8000 Zeichen |
| `size` | `2K` und `4K` leiten die Größe aus einem Seitenverhältnis ab; `custom` legt eine exakte Breite und Höhe fest. Standard: `"2K"`. | DYNAMIC_COMBO | Ja | `"2K"`<br>`"4K"`<br>`"custom"` |
| `enhance_prompt` | MiniMax schreibt den Prompt vor der Generierung in eine detaillierte Szenenbeschreibung um. Bildbearbeitungen werden immer verbessert. Wenn deaktiviert, wählen Sie ein festes Seitenverhältnis oder eine benutzerdefinierte Größe. Standard: true. | BOOLEAN | Nein | true<br>false |
| `seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Nein | 0 bis 2147483647 |
| `images` | Referenzbilder zum Bearbeiten oder Kombinieren, die im Prompt in der Reihenfolge der Verbindungen als `@Image1` bis `@Image16` adressiert werden. | AUTOGROW | Nein | Bis zu 16 Bilder |

### Eingaben für Größe „2K“ und „4K“

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Bei `auto` wählt MiniMax das Verhältnis anhand des Prompts oder richtet sich nach dem Referenzbild, wenn eines verbunden ist. Text zu Bild mit deaktiviertem `enhance_prompt` erfordert ein festes Verhältnis. Standard: `"auto"`. | COMBO | Ja | Mehrere Optionen verfügbar |

### Eingaben für Größe „custom“

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Ausgabebreite in Pixeln. Standard: 2048. | INT | Ja | 512 bis 7680 (Schritt 16) |
| `height` | Ausgabehöhe in Pixeln. Standard: 2048. | INT | Ja | 512 bis 7680 (Schritt 16) |

Hinweis: Bei einer benutzerdefinierten Größe muss Breite mal Höhe zwischen 655.360 und 20.000.000 Pixeln liegen, wobei das Seitenverhältnis höchstens 3:1 betragen darf.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das generierte oder bearbeitete Bild als PNG. | IMAGE |
| `revised_prompt` | Der umgeschriebene Prompt, den MiniMax verwendet hat, wenn die Prompt-Verbesserung aktiviert war. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxH3ImageNode/de.md)

---
**Source fingerprint (SHA-256):** `723eb4c2d3b303ece041f98bd5b773c669affb9a7b3da0c08ffcac4ee89f8e11`
