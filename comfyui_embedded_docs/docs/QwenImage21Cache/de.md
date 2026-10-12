# Qwen Image 2.1 Cache

Der QwenImage21Cache-Node konfiguriert den KV-Präfix-Cache des Qwen-Image 2.1-Modells: wo die zwischengespeicherten Keys und Values gespeichert werden und mit welcher Präzision. Text- und Referenz-Tokens werden einmal berechnet und über Sampling-Schritte hinweg wiederverwendet, was den Großteil der Geschwindigkeitssteigerung bei Edit-Workflows ausmacht. Mit diesem Node können Sie Speicher gegen Geschwindigkeit eintauschen oder den Cache vollständig deaktivieren. Dieser Node ist als experimentell gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Qwen-Image 2.1-Modell, dessen Präfix-Cache konfiguriert wird. | MODEL | Ja | - |
| `device` | Wo die zwischengespeicherten Keys und Values gespeichert werden. `"auto"` (Standard) nutzt zuerst freien VRAM und dann RAM; `"gpu"` speichert den Cache im VRAM; `"cpu"` speichert ihn im RAM und lädt ihn im Hintergrund der Berechnung vorab, was kaum Geschwindigkeit kostet; `"off"` berechnet das Präfix bei jedem Schritt neu, was langsamer ist, aber die einzige Möglichkeit darstellt, den Cache vollständig zu deaktivieren. | COMBO | Ja | `"auto"`<br>`"gpu"`<br>`"cpu"`<br>`"off"` |
| `dtype` | Speicherpräzision des Cache. `"default"` ist verlustfrei; `"int8"` halbiert den Cache bei etwa bf16-Genauigkeit; `"int4"` viertelt ihn, verdoppelt aber ungefähr den Fehler pro Schritt. | COMBO | Ja | `"default"`<br>`"int8"`<br>`"int4"` |

Wenn der Cache nicht passt, berechnet das Modell das Präfix neu, anstatt den Slot des anderen Zweigs zu verdrängen. Eine zu groß gewählte Einstellung reduziert daher die Geschwindigkeit, anstatt den Lauf fehlschlagen zu lassen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Das Modell mit angewendetem Cache-Gerät und angewendeter Präzision, bereit zum Sampling. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImage21Cache/de.md)

---
**Source fingerprint (SHA-256):** `0c10cdb465d1ee4063273ffbb4913def3830f7e329694cd0a2e292d6f3c37ae4`
