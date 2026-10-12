# Dualer CFG-Guider

Der Node Dual CFG Guider erstellt ein Guidance-System für das Sampling, das zwei Konditionierungseingaben zusammen mit einer negativen Konditionierungseingabe verwendet. Er wendet zwei separate Guidance-Skalen an, um zu steuern, wie stark jede Konditionierung das generierte Ergebnis beeinflusst, und unterstützt zwei Arten der Kombination dieser Skalen: "regular" und "nested".

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das für die Guidance zu verwendende Modell | MODEL | Ja | - |
| `cond1` | Die erste positive Konditionierungseingabe | CONDITIONING | Ja | - |
| `cond2` | Die zweite Konditionierungseingabe, verwendet als Referenz zwischen der ersten positiven Konditionierung und der negativen Konditionierung | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierungseingabe | CONDITIONING | Ja | - |
| `cfg_conds` | Auf die erste positive Konditionierung angewendete Guidance-Skala (Standard: 8.0) | FLOAT | Ja | 0.0 - 100.0 |
| `cfg_cond2_negative` | Guidance-Skala, die zwischen der zweiten Konditionierung und der negativen Konditionierung angewendet wird (Standard: 8.0) | FLOAT | Ja | 0.0 - 100.0 |
| `style` | Der anzuwendende Guidance-Stil (Standard: "regular"). Wenn auf "nested" gesetzt, wird die Guidance verschachtelt angewendet | COMBO | Ja | "regular"<br>"nested" |

Hinweis: Im Stil `regular` wird `cfg_cond2_negative` zwischen `cond2` und `negative` angewendet, und `cfg_conds` wird zwischen `cond1` und `cond2` angewendet. Im Stil `nested` wird `cfg_conds` zuerst zwischen `cond1` und `cond2` angewendet, und die resultierende Vorhersage wird dann mithilfe von `cfg_cond2_negative` von `negative` weggelenkt.

Hinweis: Im Stil `regular` wird die negative Konditionierung übersprungen, wenn `cfg_cond2_negative` gleich 1.0 ist, und wenn `cfg_conds` ebenfalls gleich 1.0 ist, wird auch die zweite Konditionierung übersprungen. Dadurch wird die Anzahl der durchgeführten Modellauswertungen reduziert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `GUIDER` | Ein konfiguriertes Guidance-System, bereit zur Verwendung beim Sampling | GUIDER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/de.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
