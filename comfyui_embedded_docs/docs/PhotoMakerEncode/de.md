# PhotoMaker Encode

Der Knoten PhotoMakerEncode kombiniert ein Referenzbild mit einem Text-Prompt, um Conditioning-Daten für die Bilderzeugung zu erstellen. Wenn der Text das Wort „photomaker“ enthält, verwendet der Knoten das PhotoMaker-Modell, um die visuelle Identität des Referenzbildes an dieser Position im Prompt in die Conditioning-Daten einzufügen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `photomaker` | Das PhotoMaker-Modell, das verwendet wird, um das Referenzbild zu verarbeiten und bildbasierte Embeddings zu erzeugen | PHOTOMAKER | Ja | - |
| `image` | Das Referenzbild, das die visuellen Eigenschaften für die Conditioning-Daten bereitstellt | IMAGE | Ja | - |
| `clip` | Das CLIP-Modell, das für die Text-Tokenisierung und Textkodierung verwendet wird | CLIP | Ja | - |
| `text` | Der Text-Prompt für die Erzeugung der Conditioning-Daten. Unterstützt mehrzeiligen Text und dynamische Prompts (Standard: "photograph of photomaker") | STRING | Ja | Beliebige Zeichenkette |

**Hinweis:** Wenn der Text „photomaker“ als eigenständiges Wort enthält, entfernt der Knoten dieses Wort aus dem kodierten Prompt und wendet an dieser Position die Identität des Referenzbildes mithilfe des PhotoMaker-Modells an. Wenn „photomaker“ nicht im Text gefunden wird, gibt der Knoten Standard-Text-Conditioning ohne Bildeinfluss zurück.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Conditioning-Daten, die die Text- und Bild-Embeddings enthalten, welche die Bilderzeugung steuern, zusammen mit der gepoolten Ausgabe des CLIP-Text-Encoders | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/de.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
