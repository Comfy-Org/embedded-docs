# TomePatchModel

TomePatchModel wendet Token-Merging (ToMe) auf ein Diffusionsmodell an, um den Rechenaufwand während der Inferenz zu senken. Dabei werden ähnliche Token im Aufmerksamkeitsmechanismus des Modells zusammengeführt, sodass das Modell weniger Token verarbeitet und die Ausgabequalität weitgehend erhalten bleibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, auf das Token-Merging angewendet werden soll | MODEL | Ja | - |
| `ratio` | Der Anteil der Token, die zusammengeführt werden (Standard: 0.3). Höhere Werte führen dazu, dass mehr Token zusammengeführt werden, was zu einer stärkeren Beschleunigung, aber möglicherweise zu einer geringeren Qualität führen kann. | FLOAT | Ja | 0.0 - 1.0 |

Hinweis: Wenn die Anzahl der Token in einem Aufmerksamkeitsblock klein genug ist, dass kein Downsampling erforderlich ist, werden die Merging-Funktionen durch No-Ops ersetzt, und das Modell wird für diesen Block unverändert ausgeführt.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendetem Token-Merging | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/de.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`
