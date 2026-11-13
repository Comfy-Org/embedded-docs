# Krea 2 Stilreferenz

Der Node Krea 2 Style Reference ermöglicht es Ihnen, ein Referenzbild hinzuzufügen, um den Stil einer Krea 2-Bildgenerierung zu beeinflussen. Sie können mehrere Stilreferenzen miteinander verketten (bis zu insgesamt 10) und das kombinierte Ergebnis in einen Krea 2 Image-Node einspeisen. Jedes von Ihnen bereitgestellte Bild wird in den ComfyAPI-Speicher hochgeladen und als URL übergeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Referenzbild, dessen Stil die Generierung beeinflusst. | IMAGE | Ja | - |
| `strength` | Referenzstärke (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.05) |
| `style_reference` | Optionale eingehende Kette von Stilreferenzen; dieser Node hängt eine weitere an. | STYLE_REF | Nein | - |

**Hinweis zu Einschränkungen:** Sie können insgesamt maximal 10 Stilreferenzen verketten. Wenn Sie versuchen, eine 11. Referenz hinzuzufügen, gibt der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `style_reference` | Eine Liste von Stilreferenz-Einträgen, die jeweils eine URL und einen Stärkewert enthalten. Speisen Sie diese Ausgabe in einen Krea 2 Image-Node ein. | STYLE_REF |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2StyleReferenceNode/de.md)

---
**Source fingerprint (SHA-256):** `6f68e5eea264e77beed4f9c5f4c8830fce7c25dfac813ffbf1951eafbb7edf72`
