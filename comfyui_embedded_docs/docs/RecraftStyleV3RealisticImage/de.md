# Recraft Style – Realistisches Bild

Dieser Node erstellt eine Stilkonfiguration zur Generierung realistischer Bilder über die Recraft-API. Er wählt den Stil `realistic_image` aus und ermöglicht Ihnen, einen optionalen Substil auszuwählen, um das Erscheinungsbild der Ausgabe fein abzustimmen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `substyle` | Der spezifische Substil, der auf den Stil `realistic_image` angewendet werden soll. Wenn auf "None" gesetzt, wird kein Substil angewendet. | STRING | Ja | Mehrere Optionen verfügbar (durch Recraft-API festgelegt) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `recraft_style` | Ein Recraft-Stilkonfigurationsobjekt, das den Stil `realistic_image` und die Einstellungen des ausgewählten Substils enthält. Diese Ausgabe kann mit anderen Recraft-Nodes verbunden werden, die eine Stil-Eingabe akzeptieren. | STYLEV3 |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/de.md)

---
**Source fingerprint (SHA-256):** `df3a09ae0956dd5807b7475248359085fdbe5abb5c40291e37db3ceabafef2ac`
