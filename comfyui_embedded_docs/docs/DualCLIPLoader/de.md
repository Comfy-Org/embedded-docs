# DualClipLoader

Der Node DualCLIPLoader ist für das gleichzeitige Laden von zwei CLIP-Modellen konzipiert und erleichtert Vorgänge, die die Integration oder den Vergleich von Merkmalen aus beiden Modellen erfordern.

Dieser Node erkennt Modelle, die sich im Ordner `ComfyUI/models/text_encoders` befinden.

## Eingaben

| Parameter | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `clip_name1` | Gibt den Namen des ersten zu ladenden CLIP-Modells an. Dieser Parameter ist entscheidend, um das richtige Modell aus einer vordefinierten Liste verfügbarer CLIP-Modelle zu identifizieren und abzurufen. | COMBO[STRING] |
| `clip_name2` | Gibt den Namen des zweiten zu ladenden CLIP-Modells an. Dieser Parameter ermöglicht das Laden eines zweiten eigenständigen CLIP-Modells für vergleichende oder integrative Analysen zusammen mit dem ersten Modell. | COMBO[STRING] |
| `type` | Wählen Sie aus „sdxl“, „sd3“, „flux“, um sich an verschiedene Modelle anzupassen. | `option` |

* Die Reihenfolge des Ladens hat keinen Einfluss auf das Ausgabeergebnis

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip` | Die Ausgabe ist ein kombiniertes CLIP-Modell, das die Merkmale oder Funktionalitäten der beiden angegebenen CLIP-Modelle integriert. | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCLIPLoader/de.md)
