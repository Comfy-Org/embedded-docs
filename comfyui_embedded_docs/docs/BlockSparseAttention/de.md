# BlockSparseAttention

Der **Block Sparse Attention**-Node modifiziert ein Modell so, dass seine Attention-Layer sich nur auf die relevantesten Teile der Eingabe konzentrieren, statt alles auf einmal zu berücksichtigen, wodurch der Rechenaufwand für lange Sequenzen verringert wird. Die Einsparungen wachsen mit der Sequenzlänge, da kurze Sequenzen mit normaler (dichter) Attention normalerweise schneller sind.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|-----------|--------------|--------|
| `model` | Das Modell, das gepatcht werden soll. | MODEL | Ja | N/A |
| `selection` | Methode zum Auswählen von Key-Blöcken für vollständige Attention auf Token-Ebene (wird als `method` angezeigt). <br>`sol-attn`: Sparsifying Online Attention verwendet einen trainingsfreien adaptiven Schwellenwert für jeden Attention-Head und Query-Block.<br>`sla`: Sparse-Linear Attention behält einen festen Prozentsatz der Key-Blöcke mit den höchsten Scores; nur mit Modellgewichten verwenden, die für dieses Muster trainiert wurden.<br>`vsa`: Video Sparse Attention (FastVideo) verwendet 3D-Video-Cube-Tiling und einen gelernten groben Attention-Zweig; erfordert FastH3-Modellgewichte. | DYNAMIC_COMBO | Ja | `"sol-attn"`<br>`"sla"`<br>`"vsa"` |
| `start_percent` | Prozentpunkt, an dem die sparse Attention beginnt. Vor diesem Punkt bleibt die Attention dicht. Standard: 0.2. | FLOAT | Nein | min: 0.0, max: 1.0, step: 0.01 |
| `end_percent` | Prozentpunkt, an dem die sparse Attention endet. Nach diesem Punkt wird die Attention wieder dicht. Standard: 1.0. | FLOAT | Nein | min: 0.0, max: 1.0, step: 0.01 |
| `dense_blocks` | Transformer-Blöcke, die immer dicht ausgeführt werden, z. B. '0, 1, 47-49'. Standard: "" (leer). Erweiterte Eingabe. | STRING | Nein | Default: "" |
| `min_tokens` | Sequenzen, die kürzer als dieser Wert sind, bleiben dicht. Standard: 12288. Erweiterte Eingabe. | INT | Nein | min: 0, max: 1048576, step: 512 |
| `extra_tokens` | Zusätzliche Tokens mit den höchsten Scores, die jeder Query-Block über seine ausgewählten Blöcke hinaus beachtet. Näher an dicht bedeutet mehr Attention-Zeit; 256 empfohlen, 0 deaktiviert. Wird für VSA ignoriert. Standard: 256. Erweiterte Eingabe. | INT | Nein | min: 0, max: 256, step: 64 |
| `sink_conditioning` | Nur MiniMax-H3. `exact_kv`: jede Query beachtet die gepackten Text-/Audio-/Referenzzeilen exakt (etwa 3 % Kosten). `exact_kv_and_rows`: führt zusätzlich die Ziel-Audio-Query-Zeilen dicht aus (hält generiertes Audio intakt). `off` deaktiviert dieses Verhalten. Standard: "exact_kv_and_rows". Erweiterte Eingabe. | COMBO | Nein | `"exact_kv"`<br>`"exact_kv_and_rows"`<br>`"off"` |
| `verbose` | Protokolliert, ob jede Attention-Form sparse Attention verwendet hat oder warum sie dicht geblieben ist. Standard: False. Erweiterte Eingabe. | BOOLEAN | Nein | Default: False |

### sol-attn Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|-----------|--------------|--------|
| `tau` | Schwellenwert in Sigma-Einheiten der Score-Verteilung. Höher ist sparser: 1.0 behält etwa 16 % der Key-Blöcke exakt, 1.5 etwa 7 %, 2.0 etwa 2.7 %. Standard: 1.3. | FLOAT | Nein | min: 0.0, max: 4.0, step: 0.05 |

### sla Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|-----------|--------------|--------|
| `keep_percent` | Prozentsatz der Key-Blöcke, die jeder Query-Block exakt behält (Sinks und die Diagonale kommen zusätzlich hinzu). Die Auswahl, gegen die SLA-artige LoRAs destilliert werden; ohne ein solches LoRA ist ein höherer Wert näher an dicht. Standard: 10.0. | FLOAT | Nein | min: 0.5, max: 95.0, step: 0.5 |

### vsa Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|-----------|--------------|--------|
| `keep_percent` | Prozentsatz der Video-Würfel, die jeder Query-Würfel behält; FastH3-VSA-Checkpoints sind auf 10 trainiert. Verwendet die `to_gate_compress`-Layer des Modells für den groben Zweig, falls vorhanden. Standard: 10.0. | FLOAT | Nein | min: 0.5, max: 95.0, step: 0.5 |

**Hinweis:** Nur die Parameter, die zur aktuell ausgewählten Methode gehören, werden in der Oberfläche angezeigt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|-----------|
| `model` | Das Modell mit angewendeter Block-Sparse-Attention. | MODEL |

## Einschränkungen und Limitierungen

- Sequenzen, die kürzer als `min_tokens` sind, Blöcke, die in `dense_blocks` aufgeführt sind, und Sampling-Schritte außerhalb des Fensters von `start_percent` bis `end_percent` fallen auf das dichte Modell-Attention-Backend zurück, das vom Node Model Attention Backend ausgewählt wurde.
- `extra_tokens` wird ignoriert, wenn die Methode `vsa` ausgewählt ist. Es wird eine Meldung protokolliert, da VSA-Gewichte auf ihr sparses Muster trainiert wurden.
- Die Methode `vsa` erfordert ein MiniMax-H3-Modell; jedes andere Modell löst einen Fehler aus. Wenn dem Modell `to_gate_compress`-Layer fehlen, läuft die Fein-Stufe ohne den groben Zweig und es wird eine Warnung protokolliert.
- `dense_blocks` wird für Modelle ignoriert, die keine Blockindizes melden; dies wird im Protokoll vermerkt, wenn `verbose` aktiviert ist.
- `sink_conditioning` gilt nur für MiniMax-H3-Modelle, die ein Layout melden, das zur aktuellen Sequenzlänge passt.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/de.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
