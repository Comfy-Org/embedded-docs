# HiDreamO1ReferenceImages

Dieser Node hängt Referenzbilder sowohl an die positive als auch an die negative Konditionierung an, sodass nachgelagerte Nodes sie zur Steuerung der Generierung verwenden können. Referenzbilder werden in numerischer Reihenfolge ihrer Eingabe-Sockets angewendet. Wenn keine Referenzbilder verbunden sind, werden die positive und die negative Konditionierung unverändert weitergegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positive Konditionierung, an die Referenzbilder angehängt werden. | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierung, an die Referenzbilder angehängt werden. | CONDITIONING | Ja | - |
| `images` | Referenzbilder werden in numerischer Socket-Reihenfolge verwendet. Wenn Bilder bereitgestellt werden, werden sie sowohl an die positive als auch an die negative Konditionierung angehängt. | IMAGE | Nein | 0 bis 100 Bilder (`image_1` bis `image_100`) |

**Hinweis zum Parameter `images`:** Dies ist eine automatisch wachsende Eingabe, die nummerierte Sockets `image_1` bis `image_100` bereitstellt. Bilder werden in numerischer Socket-Reihenfolge verwendet. Die Eingabe ist optional: Wenn keine Referenzbilder verbunden sind, gibt der Node die Konditionierungen `positive` und `negative` unverändert zurück. Wenn Bilder verbunden sind, wird derselbe Satz von Referenzbildern an beide Ausgaben angehängt, und die negative Konditionierung wird zudem als negativ markiert, bevor die Bilder angehängt werden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die positive Konditionierung mit angehängten Referenzbildern. | CONDITIONING |
| `negative` | Die negative Konditionierung mit angehängten Referenzbildern. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/de.md)

---
**Source fingerprint (SHA-256):** `07f9f0ea19957523e95d04b9086dc994807bb0cd5262fe798dc784c1ecb4920d`
