# SaveLatent

SaveLatent speichert latente Tensoren als `.latent`-Dateien auf der Festplatte, damit sie später wiederverwendet oder geteilt werden können. Es nimmt latente Samples entgegen, schreibt sie mit einem automatisch generierten Namen in den Ausgabeordner und kann Workflow-Metadaten wie den Prompt in die gespeicherte Datei einbetten. Dieselben latenten Samples werden außerdem unverändert für die weitere Verarbeitung durchgereicht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples` | Die latenten Samples, die auf der Festplatte gespeichert werden sollen. | LATENT | Ja | - |
| `filename_prefix` | Das Präfix, das zum Erstellen des Ausgabedateinamens verwendet wird. Es kann Unterordner enthalten, zum Beispiel "latents/ComfyUI" (Standard: "latents/ComfyUI"). | STRING | Ja | - |
| `prompt` | Der Workflow-Prompt, als JSON serialisiert und in den Metadaten der gespeicherten Datei abgelegt (verborgener Parameter, wird automatisch bereitgestellt). | PROMPT | Nein | - |
| `extra_pnginfo` | Zusätzliche Workflow-Informationen, als JSON serialisiert und in den Metadaten der gespeicherten Datei abgelegt (verborgener Parameter, wird automatisch bereitgestellt). | EXTRA_PNGINFO | Nein | - |

Hinweis: Jede gespeicherte Datei wird unter Verwendung des Präfixes und eines 5-stelligen Zählers benannt, zum Beispiel `ComfyUI_00001_.latent`, und im Ausgabeverzeichnis abgelegt. Die Datei enthält den latenten Tensor und eine Markierung für die Version des Latent-Formats. Metadaten werden nur dann in die gespeicherte Datei eingebettet, wenn die Metadatenunterstützung aktiviert ist, d. h., wenn ComfyUI nicht mit der Option `--disable-metadata` gestartet wurde.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Dieselben latenten Samples, die als Eingabe bereitgestellt wurden, unverändert durchgereicht. | LATENT |
| `ui` | UI-Anzeigedaten, die die gespeicherte Datei beschreiben: ihren Dateinamen, Unterordner und Ausgabetyp ("output"). | UI |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/de.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`
