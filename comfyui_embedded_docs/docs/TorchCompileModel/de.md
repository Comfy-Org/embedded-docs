# TorchCompileModel

Der TorchCompileModel-Node wendet PyTorch-Kompilierung auf ein Modell an, um dessen Leistung zu optimieren. Er erstellt eine Kopie des Eingabemodells und umhüllt es mit der PyTorch-Kompilierungsfunktionalität unter Verwendung des angegebenen Backends. Dies kann die Ausführungsgeschwindigkeit des Modells während der Inferenz verbessern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das zu kompilierende und zu optimierende Modell | MODEL | Ja | - |
| `backend` | Das für die Optimierung zu verwendende PyTorch-Kompilierungs-Backend (Standard: "inductor") | STRING | Ja | "inductor"<br>"cudagraphs" |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das kompilierte Modell mit angewendeter PyTorch-Kompilierung | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/de.md)

---
**Source fingerprint (SHA-256):** `240c6eb84ce2b93fe4d7c04fcf69df571e662f17893a4fd8e721241ea082edc8`
