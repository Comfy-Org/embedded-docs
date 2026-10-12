# Depth Anything 3 laden

Der Node **Load Depth Anything 3** lädt ein Depth Anything 3-Modell aus einer Datei und bereitet es für Tiefenschätzungsaufgaben vor. Sie können die Modelldatei auswählen und optional die numerische Genauigkeit (den Datentyp) für die Gewichte des Modells festlegen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model_name` | Der Name der zu ladenden Depth Anything 3-Modelldatei. | STRING | Ja | Liste der verfügbaren Modelldateien im Ordner `geometry_estimation` |
| `weight_dtype` | Die numerische Genauigkeit (der Datentyp) für die Modellgewichte. `"default"` verwendet die ursprüngliche Genauigkeit des Modells, `"fp16"` verwendet 16-Bit-Gleitkommazahlen, `"bf16"` verwendet bfloat16 und `"fp32"` verwendet 32-Bit-Gleitkommazahlen. (Standard: `"default"`) | STRING | Nein | `"default"`<br>`"fp16"`<br>`"bf16"`<br>`"fp32"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `DA3_MODEL` | Das geladene Depth Anything 3-Modell, bereit für die Verwendung in Workflows zur Tiefenschätzung. | DA3_MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadDA3Model/de.md)

---
**Source fingerprint (SHA-256):** `b1b3f4075cd9172bc1f274848b9300bca20d3cbd53b23d3c4a9f0986b36e409e`
