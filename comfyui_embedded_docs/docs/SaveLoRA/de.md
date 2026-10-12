# SaveLoRA

Der SaveLoRA-Node speichert ein LoRA-(Low-Rank Adaptation)-Modell in einer Datei. Er nimmt ein LoRA-Modell als Eingabe entgegen und schreibt es in eine `.safetensors`-Datei im Ausgabeverzeichnis. Sie können ein Dateinamenpräfix und optional eine Schrittanzahl angeben, die in den endgültigen Dateinamen aufgenommen wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `lora` | Das zu speichernde LoRA-Modell. Verwenden Sie kein Modell mit angewendeten LoRA-Schichten. | LORA_MODEL | Ja | N/A |
| `prefix` | Das Präfix, das für die gespeicherte LoRA-Datei verwendet werden soll (Standard: "loras/ComfyUI_trained_lora"). | STRING | Ja | N/A |
| `steps` | Optional: Die Anzahl der Schritte, für die das LoRA trainiert wurde, wird zum Benennen der gespeicherten Datei verwendet. | INT | Nein | N/A |

**Hinweis:** Die Eingabe `lora` muss ein reines LoRA-Modell sein. Stellen Sie kein Basismodell bereit, auf das LoRA-Schichten angewendet wurden.

**Hinweis:** Die Datei wird im ComfyUI-Ausgabeverzeichnis mit der Erweiterung `.safetensors` gespeichert. Der Dateiname wird aus dem `prefix` und einem mit Nullen aufgefüllten Zähler (5 Stellen) gebildet, um ein Überschreiben vorhandener Dateien zu vermeiden. Wenn `steps` angegeben wird, wird die Schrittanzahl ebenfalls in den Dateinamen aufgenommen (zum Beispiel `1000_steps` für 1000 Schritte).

**Hinweis:** Dieser Node ist als experimentell gekennzeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| *None* | Dieser Node gibt keine Daten an den Workflow aus. Es ist ein Ausgabe-Node, der eine Datei auf dem Datenträger speichert. | N/A |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/de.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
