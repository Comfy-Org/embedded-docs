# Bilder vergleichen

## Überblick

Der Node Image Compare bietet eine visuelle Oberfläche, um zwei Bilder mithilfe eines ziehbaren Schiebereglers Seite an Seite zu vergleichen. Er ist als Ausgabe-Node konzipiert, das heißt, er gibt keine Daten an andere Nodes weiter, sondern zeigt die Bilder direkt in der Benutzeroberfläche zur Prüfung an.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image_a` | Das erste zu vergleichende Bild. | IMAGE | Nein | - |
| `image_b` | Das zweite zu vergleichende Bild. | IMAGE | Nein | - |
| `compare_view` | Das Steuerelement, das die Schieberegler-Vergleichsansicht in der Benutzeroberfläche aktiviert. | IMAGECOMPARE | Ja | - |

**Hinweis:** Dieser Node ist ein Ausgabe-Node. Obwohl `image_a` und `image_b` optional sind, muss mindestens ein Bild bereitgestellt werden, damit der Node eine sichtbare Wirkung hat. Der Node zeigt einen leeren Bereich für jede Bildeingabe an, die nicht verbunden ist. Jeder bereitgestellte Bild-Batch wird im temporären Speicher unter den Präfixen `comfy.compare.a` bzw. `comfy.compare.b` gespeichert und anschließend in der Schieberegleransicht angezeigt.

## Ausgaben

Dieser Node ist ein Ausgabe-Node und erzeugt keine Datenausgaben zur Verwendung in anderen Nodes. Seine Funktion besteht darin, die bereitgestellten Bilder in der ComfyUI-Oberfläche anzuzeigen.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/de.md)

---
**Source fingerprint (SHA-256):** `bc065572c5631ed80c0590aabae775c51d0f607895a87cb2cca78037ab9a6638`
