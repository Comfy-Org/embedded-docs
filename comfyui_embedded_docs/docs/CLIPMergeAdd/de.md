# CLIPMergeAdd

Der CLIPMergeAdd-Node kombiniert zwei CLIP-Modelle, indem er Patches aus dem zweiten Modell zum ersten Modell hinzufügt. Er erstellt eine Kopie des ersten CLIP-Modells und übernimmt selektiv Schlüssel-Patches aus dem zweiten Modell, wobei Positions-IDs und Logit-Scale-Parameter ausgeschlossen werden. Dadurch können Sie CLIP-Modellkomponenten zusammenführen und gleichzeitig die Struktur des Basismodells beibehalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip1` | Das Basis-CLIP-Modell, das geklont und als Grundlage für das Zusammenführen verwendet wird | CLIP | Ja | - |
| `clip2` | Das sekundäre CLIP-Modell, das Schlüssel-Patches bereitstellt, die dem Basismodell hinzugefügt werden | CLIP | Ja | - |

Schlüssel aus `clip2`, die auf `.position_ids` oder `.logit_scale` enden, werden übersprungen, sodass diese Parameter die Werte von `clip1` behalten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CLIP` | Ein zusammengeführtes CLIP-Modell, das die Struktur des Basismodells mit hinzugefügten Patches aus dem sekundären Modell enthält | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/de.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`
