# Bria Beleuchtung ändern

Dieser Node ändert die Lichtatmosphäre und die Lichtrichtung eines Bildes mithilfe von Bria. Das Bild wird von Bria neu gerendert, daher ist das Ergebnis nicht pixelgenau zum Eingabebild; das gesamte Bild wird mit etwa 1 Megapixel neu erzeugt.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Bild, dessen Licht geändert wird. Ein etwaiger Alphakanal wird entfernt, bevor das Bild hochgeladen wird. | IMAGE | Ja | - |
| `light_type` | Lichtatmosphäre, die angewendet werden soll. | COMBO | Ja | `"midday"`<br>`"blue hour light"`<br>`"low-angle sunlight"`<br>`"sunrise light"`<br>`"spotlight on subject"`<br>`"overcast light"`<br>`"soft overcast daylight lighting"`<br>`"cloud-filtered lighting"`<br>`"fog-diffused lighting"`<br>`"moonlight lighting"`<br>`"starlight nighttime"`<br>`"soft bokeh lighting"`<br>`"harsh studio lighting"` |
| `light_direction` | Woher das Licht kommt. Atmosphären mit hartem Licht wie midday, spotlight on subject und harsh studio lighting reagieren am stärksten darauf. | COMBO | Ja | `"front"`<br>`"side"`<br>`"bottom"`<br>`"top-down"` |
| `moderation` | Moderations-Einstellungen. Wählen Sie `"true"`, um die Moderationsoptionen einzublenden, oder `"false"`, um ohne sie auszuführen. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |

### Moderationseingaben

Diese Optionen werden angezeigt, wenn `moderation` auf `"true"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Aktiviert die Inhaltsmoderation für das Eingabebild. Standard: false. | BOOLEAN | Nein | `true`<br>`false` |
| `visual_output_moderation` | Aktiviert die Inhaltsmoderation für das generierte Ausgabebild. Standard: false. | BOOLEAN | Nein | `true`<br>`false` |

Hinweis: Bria rendert das gesamte Bild mit etwa 1 Megapixel neu, daher ist das Ergebnis nicht pixelgenau zum Eingabebild.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das von Bria zurückgegebene neu beleuchtete Bild. | IMAGE |
| `structured_prompt` | Strukturierte Beschreibung des bearbeiteten Bildes für eine nachfolgende Bearbeitung mit Bria FIBO Image Edit. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRelight/de.md)

---
**Source fingerprint (SHA-256):** `21fbe2186c99a7e8d99d5659ac25c3ab1a757492916dba4135487d4b293cb4f6`
