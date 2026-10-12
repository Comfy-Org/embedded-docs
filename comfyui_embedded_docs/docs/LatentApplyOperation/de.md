# LatentApplyOperation

Der Node LatentApplyOperation wendet eine angegebene latente Operation auf latente Samples an. Er nimmt latente Daten und eine Operation als Eingaben entgegen, verarbeitet die latenten Samples mithilfe der bereitgestellten Operation und gibt die modifizierten latenten Daten zurück. Mit diesem Node können Sie latente Repräsentationen in Ihrem Workflow transformieren oder manipulieren. Dieser Node ist derzeit als experimentell gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples` | Die latenten Samples, die von der Operation verarbeitet werden sollen | LATENT | Ja | - |
| `operation` | Die Operation, die auf die latenten Samples angewendet werden soll | LATENT_OPERATION | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die modifizierten latenten Samples nach Anwendung der Operation | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/de.md)

---
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
