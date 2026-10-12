# AdjustBrightness

Der Node „Adjust Brightness“ ändert, wie hell ein Bild erscheint. Er multipliziert die Farbwerte des Bildes mit einem `factor` und hält die Ergebnisse im gültigen Bereich von 0.0 bis 1.0. Ein Faktor von 1.0 lässt das Bild unverändert, Werte unter 1.0 machen es dunkler und Werte über 1.0 heller.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das anzupassende Eingabebild. Akzeptiert ein einzelnes Bild oder einen Batch von Bildern. | IMAGE | Ja | - |
| `factor` | Helligkeitsfaktor. 1.0 = keine Änderung, <1.0 = dunkler, >1.0 = heller. (Standard: 1.0) | FLOAT | Nein | 0.0 - 2.0 |

Hinweis: Wenn das Eingabebild einen Alphakanal (RGBA) hat, werden nur die Farbkanäle angepasst. Der Alphakanal wird unverändert aus der Eingabe kopiert, da er Transparenz und nicht Farbe speichert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das Ausgabebild mit angepasster Helligkeit. Wenn die Eingabe einen Alphakanal hat, bleiben die Alpha-Werte unverändert. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/de.md)

---
**Source fingerprint (SHA-256):** `64c1499d16deb5922fa63538182cd227e8f2ba9ded5962064ce9f228a0f4a163`
