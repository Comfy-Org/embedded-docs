# Konditionierung (Multiplizieren)

Dieser Node multipliziert die Konditionierungswerte mit einem angegebenen Faktor, sodass Sie den Einfluss der Konditionierung auf den Generierungsprozess skalieren können. Dazu wird der Multiplikator sowohl auf den Haupt-Konditionierungstensor als auch auf die gepoolten Ausgabewerte angewendet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `conditioning` | Die zu skalierenden Konditionierungsdaten | CONDITIONING | Ja | - |
| `multiplier` | Der Faktor, mit dem die Konditionierungswerte multipliziert werden (Standard: 1.0) | FLOAT | Ja | -100.0 bis 100.0 (Schritt: 0.01) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `CONDITIONING` | Die skalierten Konditionierungsdaten mit multiplizierten Werten | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/de.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`
