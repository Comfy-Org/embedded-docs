# RecraftStyleV3InfiniteStyleLibrary

Dieser Node ermöglicht es Ihnen, einen Stil aus Recrafts Infinite Style Library mithilfe einer vorhandenen UUID auszuwählen. Er ruft die Stilinformationen anhand der bereitgestellten Stil-ID ab und gibt sie zur Verwendung in anderen Recraft-Nodes zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `style_id` | UUID des Stils aus der Infinite Style Library. | STRING | Ja | Beliebige gültige UUID |

**Hinweis:** Die Eingabe `style_id` darf nicht leer sein. Wenn eine leere Zeichenkette bereitgestellt wird, löst der Node eine Ausnahme aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `recraft_style` | Das ausgewählte Stilobjekt aus Recrafts Infinite Style Library | STYLEV3 |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/de.md)

---
**Source fingerprint (SHA-256):** `4554acaaba9e83373d6fb44ea5465175182efcf7c9220c2328c4749c2febd40f`
