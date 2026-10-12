# OpenAIDalle3

Erzeugt Bilder synchron über den DALL·E-3-Endpunkt von OpenAI. Dieser Node nimmt einen Text-Prompt entgegen und erstellt mithilfe des DALL·E-3-Modells von OpenAI entsprechende Bilder, wobei Sie Bildqualität, Stil und Abmessungen angeben können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Text-Prompt für DALL·E (Standard: "") | STRING | Ja | - |
| `seed` | Noch nicht im Backend implementiert (Standard: 0) | INT | Nein | 0 bis 2147483647 |
| `quality` | Bildqualität (Standard: "standard") | COMBO | Nein | "standard"<br>"hd" |
| `style` | Vivid bewirkt, dass das Modell zu hyperrealistischen und dramatischen Bildern neigt. Natural bewirkt, dass das Modell natürlichere, weniger hyperrealistisch wirkende Bilder erzeugt. (Standard: "natural") | COMBO | Nein | "natural"<br>"vivid" |
| `size` | Bildgröße (Standard: "1024x1024") | COMBO | Nein | "1024x1024"<br>"1024x1792"<br>"1792x1024" |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `IMAGE` | Das von DALL·E 3 generierte Bild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/de.md)

---
**Source fingerprint (SHA-256):** `9077628610503d8c0afdd04e30dadac46106bd577d10f2d7aa10864db4430605`
