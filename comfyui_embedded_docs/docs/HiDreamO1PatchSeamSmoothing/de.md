# HiDream-O1 Patch-Nahtglättung

Dieser Node reduziert sichtbare Nahtstellen in Bildern, die vom HiDream-O1-Modell erzeugt werden, indem die Modellausgabe über mehrere verschobene Patch-Grid-Positionen während des späteren Teils des Sampling-Prozesses gemittelt wird. Er führt das Modell mehrmals mit leicht unterschiedlichen Bildausrichtungen aus und mischt die Ergebnisse zusammen, was dabei hilft, die gitterartigen Artefakte zu eliminieren, die an Patch-Grenzen auftreten können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das die Nahtglättung angewendet werden soll. | MODEL | Ja | - |
| `start_percent` | Sampling-Fortschritt (0=Start, 1=Ende), bei dem die Mischung eingeschaltet wird. Standard: 0.8 | FLOAT | Ja | 0.0 to 1.0 (step: 0.01) |
| `end_percent` | Sampling-Fortschritt, bei dem die Mischung ausgeschaltet wird. Standard: 1.0 | FLOAT | Ja | 0.0 to 1.0 (step: 0.01) |
| `pattern` | Verschiebungs-Layout. `single_shift`: ein Durchlauf am natürlichen Patch-Grid + andere versetzt. `symmetric`: alle Durchläufe außerhalb des Gitters, Verschiebungen um den Ursprung aufgeteilt. Standard: "single_shift" | COMBO | Ja | `"single_shift"`<br>`"symmetric"` |
| `passes` | Anzahl der Durchläufe pro aktiviertem Schritt. `2`/`4` = fest. `ramp_*`: Die Durchlaufanzahl erhöht sich, wenn sich das Sampling dem Ende nähert (mehr Glättung dort, wo Nahtstellen am sichtbarsten sind). Standard: "2" | COMBO | Ja | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `blend` | `average`: gleichgewichtetes Mittel. `window`: Hann-Fenster-Gewichtung, die jeden Durchlauf weg von seinen Patch-Grenzen bevorzugt. `median`: Median pro Pixel, verwirft Wraparound-Ausreißer-Durchläufe. Standard: "average" | COMBO | Ja | `"average"`<br>`"window"`<br>`"median"` |
| `strength` | Interpolation zwischen der Vorhersage des natürlichen Gitters (0) und dem gemittelten Ergebnis (1). Standard: 1.0 | FLOAT | Ja | 0.0 to 1.0 (step: 0.01) |

**Hinweis zu Parameterbeschränkungen:**
- Der Glättungseffekt wird nicht angewendet, wenn `strength` 0.0 oder weniger beträgt oder wenn `end_percent` kleiner oder gleich `start_percent` ist. In diesen Fällen gibt der Node das Modell unverändert zurück.
- Die Ramp-Optionen des Parameters `passes` (`ramp_2_4`, `ramp_2_4_8`) sind nur dann sinnvoll, wenn `end_percent` größer als `start_percent` ist, da die Anzahl der Durchläufe zunimmt, wenn das Sampling diesen Bereich durchläuft.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendetem Nahtglättungs-Wrapper. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/de.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
