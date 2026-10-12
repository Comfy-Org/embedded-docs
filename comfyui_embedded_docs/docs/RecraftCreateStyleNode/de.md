# RecraftCreateStyleNode

Dieser Node erstellt einen benutzerdefinierten Stil für die Bildgenerierung durch Hochladen von Referenzbildern. Sie können zwischen 1 und 5 Bilder hochladen, um den neuen Stil zu definieren, und der Node gibt eine eindeutige Stil-ID zurück, die mit anderen Recraft-Nodes verwendet werden kann. Die kombinierte Gesamtdateigröße aller hochgeladenen Bilder darf 5 MB nicht überschreiten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `style` | Der Basisstil der generierten Bilder. | STRING | Ja | `"realistic_image"`<br>`"digital_illustration"` |
| `images` | Ein Satz von 1 bis 5 Referenzbildern, die zum Erstellen des benutzerdefinierten Stils verwendet werden. | IMAGE | Ja | 1 bis 5 Bilder |

**Hinweis:** Die Gesamtdateigröße aller Bilder im `images`-Eingang muss weniger als 5 MB betragen. Der Node schlägt fehl, wenn dieses Limit überschritten wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `style_id` | Die eindeutige Kennung für den neu erstellten benutzerdefinierten Stil. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreateStyleNode/de.md)

---
**Source fingerprint (SHA-256):** `36edcb0b96eed5930d9d7ff00a1812d129b7cd9b7ab0f0d758594a20791826b2`
