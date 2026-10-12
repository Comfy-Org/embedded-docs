# OpenAIDalle2

Generiert Bilder synchron über den DALL·E-2-Endpunkt von OpenAI. Der Node sendet einen Text-Prompt an die OpenAI-DALL·E-2-API und gibt die resultierenden Bilder an ComfyUI zurück. Er kann auch ein vorhandenes Bild bearbeiten, wenn sowohl ein `image` als auch eine `mask` gemeinsam angegeben werden.

## Funktionsweise

Dieser Node verbindet sich mit der OpenAI-DALL·E-2-API, um Bilder auf Grundlage von Textbeschreibungen zu erstellen. Wenn Sie einen Text-Prompt angeben, sendet der Node ihn an die Server von OpenAI, die entsprechende Bilder generieren und an ComfyUI zurückgeben. Der Node kann in zwei Modi betrieben werden: Standard-Bildgenerierung nur mit einem Text-Prompt oder Bildbearbeitungsmodus, wenn sowohl ein Bild als auch eine Maske angegeben werden. Im Bearbeitungsmodus verwendet er die Maske, um zu bestimmen, welche Teile des Originalbilds geändert werden sollen, während andere Bereiche unverändert bleiben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt` | Text-Prompt für DALL·E (Standard: leer) | STRING | Ja | - |
| `seed` | noch nicht im Backend implementiert (Standard: 0) | INT | Nein | 0 bis 2147483647 |
| `size` | Bildgröße (Standard: "1024x1024") | COMBO | Nein | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Anzahl der zu generierenden Bilder (Standard: 1) | INT | Nein | 1 bis 8 |
| `image` | Optionales Referenzbild für die Bildbearbeitung. | IMAGE | Nein | - |
| `mask` | Optionale Maske für Inpainting (weiße Bereiche werden ersetzt) | MASK | Nein | - |

**Hinweis:** Der Bildbearbeitungsmodus wird nur aktiviert, wenn sowohl `image` als auch `mask` gemeinsam bereitgestellt werden. Wenn nur eines von beiden angegeben wird, wird ein Fehler ausgelöst. Die `mask` muss dieselbe Größe wie das `image` haben; andernfalls wird ein Fehler ausgelöst. Im Bearbeitungsmodus geben die weißen Bereiche der Maske die Regionen an, die ersetzt werden.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Die von DALL·E 2 generierten oder bearbeiteten Bilder | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/de.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`
