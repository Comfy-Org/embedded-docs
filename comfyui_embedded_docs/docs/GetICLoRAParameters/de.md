# IC-LoRA-Parameter abrufen

Dieser Node liest die Metadaten aus einem mit LoRA geladenen Modell, um IC-LoRA-Parameter wie den Referenz-Downscale-Faktor zu extrahieren. Er gibt diese Parameter als strukturiertes Objekt aus, das mit dem LTXVAddGuide-Node verbunden werden kann, wenn eine LoRA eine spezielle Behandlung der Guides erfordert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `iclora_model` | Direkte Ausgabe eines LoRA Loaders für das spezifische IC-LoRA, aus dem die Metadaten extrahiert werden sollen. | MODEL | Ja | N/A |

Hinweis: Wenn die LoRA-Metadaten fehlen oder keinen `reference_downscale_factor`-Eintrag enthalten, gibt der Node einen Standardwert von 1 aus. Wenn vorhanden, wird der Faktor gerundet und auf einen Mindestwert von 1 gesetzt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `iclora_parameters` | Aus den LoRA-Metadaten extrahierte IC-LoRA-Parameter (z. B. reference_downscale_factor). Mit LTXVAddGuide verbinden, wenn die LoRA eine spezielle Behandlung der Guides erfordert. | IC_LORA_PARAMETERS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/de.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
