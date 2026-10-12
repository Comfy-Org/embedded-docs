# TextEncodeJoyImageEdit

Dieser Node kodiert einen Text-Prompt und optionale Bilder in Konditionierungsdaten zur Verwendung mit JoyImage-Modellen. Er kombiniert einen CLIP-Textencoder mit optionalen Bildeingaben, um reichhaltige Konditionierung zu erzeugen, die Bilderzeugungs- oder Bildbearbeitungsaufgaben steuern kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip` | Das CLIP-Modell, das zum Kodieren des Text-Prompts verwendet wird | CLIP | Ja | - |
| `prompt` | Der zu kodierende Text-Prompt, unterstützt mehrzeilige Eingabe und dynamische Prompts | STRING | Ja | - |
| `vae` | Ein VAE-Modell zum Kodieren von Bildern in den latenten Raum | VAE | Nein | - |
| `images` | Optionale Bilder, die in die Konditionierung aufgenommen werden, bis zu maximal 6 Bilder. Jedes Bild wird als separate Eingabe verbunden (image_0 bis image_5) | IMAGE | Nein | 0 bis 6 Bilder |

Die Eingabe `images` ist eine AutoGrow-Gruppe, die zwischen 0 und 6 Bilder akzeptiert. Wenn keine Bilder verbunden sind, basiert die Konditionierung ausschließlich auf dem Text-Prompt.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `CONDITIONING` | Die kodierten Konditionierungsdaten, die den Text-Prompt und alle bereitgestellten Bilder kombinieren | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeJoyImageEdit/de.md)

---
**Source fingerprint (SHA-256):** `ef48523aa9fc990b2839d755cef272bcdfbacef5af8d961736fde5200c6f082d`
