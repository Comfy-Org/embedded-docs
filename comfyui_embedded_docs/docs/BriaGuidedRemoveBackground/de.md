# Bria Guided Remove Background

Dieser Node entfernt den Hintergrund aus einem Bild mit Bria und behält dabei bei, was der Prompt beschreibt. Die ursprünglichen Pixel werden in voller Auflösung mit einem neuen Alphakanal zurückgegeben, anstatt neu gerendert zu werden, sodass feine Details und Kanten erhalten bleiben. Ein Prompt, der auf nichts passt, liefert ein vollständig transparentes Bild. Für einen einfachen Freisteller ohne Vorgaben ist Bria Remove Image Background kostengünstiger.

## Eingaben

Der Selektor `moderation` blendet zusätzliche Moderationsoptionen ein, wenn er auf `"true"` gesetzt ist.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das freizustellende Bild. | IMAGE | Ja | - |
| `prompt` | Was beibehalten werden soll und optional, was entfernt oder eingeschränkt werden soll, z. B. „die Person mit der Matte und der Pflanze“, „die Frau an ihrem Schreibtisch ohne die Lampe“ oder „nur der Stuhl“. Darf nicht leer sein. Wenn nichts auf den Prompt passt, ist das Ergebnis vollständig transparent. Standard: `""` (leerer String). | STRING | Ja | 1 Zeichen oder mehr |
| `moderation` | Moderationseinstellungen. Wenn auf `"true"` gesetzt, werden die unten aufgeführten visuellen Moderationsflags verfügbar. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |

### Moderation "true" Eingaben

Diese Parameter erscheinen nur, wenn `moderation` auf `"true"` gesetzt ist. Die Option `"false"` fügt keine zusätzlichen Eingaben hinzu.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Aktiviert die Inhaltsmoderation für das Eingabebild. Standard: `False`. | BOOLEAN | Nein | True / False |
| `visual_output_moderation` | Aktiviert die Inhaltsmoderation für das generierte Bild. Standard: `False`. | BOOLEAN | Nein | True / False |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das freigestellte Bild: die ursprünglichen Pixel mit einem neuen Alphakanal. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGuidedRemoveBackground/de.md)

---
**Source fingerprint (SHA-256):** `210fa214a0d0d8ad19a15ea4f6baa9f13499bc4c3767e270f19f2a08d67e25ac`
