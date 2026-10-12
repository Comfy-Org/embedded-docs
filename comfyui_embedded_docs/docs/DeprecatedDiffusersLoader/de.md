# DeprecatedDiffusersLoader

Der DiffusersLoader-Node ist für das Laden von Modellen aus der Diffusers-Bibliothek konzipiert und übernimmt insbesondere das Laden von UNet-, CLIP- und VAE-Modellen basierend auf den angegebenen Modellpfaden. Er erleichtert die Integration dieser Modelle in das ComfyUI-Framework und ermöglicht erweiterte Funktionalitäten wie Text-zu-Bild-Generierung, Bildbearbeitung und mehr.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model_path` | Gibt den Pfad zu dem zu ladenden Modell an. Dieser Pfad ist entscheidend, da er bestimmt, welches Modell für nachfolgende Operationen verwendet wird, und die Ausgabe sowie die Fähigkeiten des Nodes beeinflusst. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das geladene UNet-Modell, das Teil des Ausgabe-Tupels ist. Dieses Modell ist wesentlich für Aufgaben der Bildsynthese und Bildbearbeitung innerhalb des ComfyUI-Frameworks. | MODEL |
| `clip` | Das geladene CLIP-Modell, das im Ausgabe-Tupel enthalten ist, falls angefordert. Dieses Modell ermöglicht erweiterte Fähigkeiten zum Verständnis und zur Bearbeitung von Text und Bildern. | CLIP |
| `vae` | Das geladene VAE-Modell, das im Ausgabe-Tupel enthalten ist, falls angefordert. Dieses Modell ist entscheidend für Aufgaben, die die Manipulation im latenten Raum und die Bilderzeugung betreffen. | VAE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedDiffusersLoader/de.md)
