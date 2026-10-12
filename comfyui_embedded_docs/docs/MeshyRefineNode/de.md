# Meshy: Entwurfsmodell verfeinern

Der Node Meshy: Refine Draft Model nimmt ein 3D-Entwurfsmodell aus einer vorherigen Meshy-Aufgabe entgegen und verbessert es; optional können Texturen mithilfe eines Text-Prompts oder eines Referenzbilds hinzugefügt werden. Er übermittelt den Verfeinerungsauftrag an die Meshy-API und gibt das fertige Modell nach Abschluss der Aufgabe als GLB- und FBX-Dateien zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das KI-Modell, das zum Verfeinern des Entwurfsmodells verwendet wird. | COMBO | Ja | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | Die eindeutige Aufgaben-ID des Entwurfsmodells, das Sie verfeinern möchten. | MESHY_TASK_ID | Ja | - |
| `enable_pbr` | PBR-Maps (Metallic, Roughness, Normal) zusätzlich zur Grundfarbe generieren. Hinweis: Dies sollte auf false gesetzt werden, wenn der Sculpture-Stil verwendet wird, da der Sculpture-Stil einen eigenen Satz von PBR-Maps generiert. (Standard: False) | BOOLEAN | Ja | - |
| `texture_prompt` | Geben Sie einen Text-Prompt an, um den Texturierungsprozess zu steuern. Maximal 600 Zeichen. Kann nicht gleichzeitig mit `texture_image` verwendet werden. (Standard: leere Zeichenkette) | STRING | Ja | Maximal 600 Zeichen |
| `texture_image` | Es darf nur eines von `texture_image` oder `texture_prompt` gleichzeitig verwendet werden. | IMAGE | Nein | - |
| `texture_resolution` | Auflösung der Grundfarbtextur. Höhere Auflösungen erfassen mehr Oberflächendetails. | COMBO | Ja | `"2k"`<br>`"4k"`<br>`"8k"` |

**Hinweis:** Die Eingaben `texture_prompt` und `texture_image` schließen sich gegenseitig aus. Sie können im selben Vorgang nicht sowohl einen Text-Prompt als auch ein Bild für die Texturierung angeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Der Dateiname des generierten GLB-Modells. (Nur zur Abwärtskompatibilität) | STRING |
| `meshy_task_id` | Die eindeutige Aufgaben-ID für den übermittelten Verfeinerungsauftrag. | MESHY_TASK_ID |
| `GLB` | Das fertig verfeinerte 3D-Modell im GLB-Format. | FILE3DGLB |
| `FBX` | Das fertig verfeinerte 3D-Modell im FBX-Format. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/de.md)

---
**Source fingerprint (SHA-256):** `d9aac584e6abf9688c97bf01ea515bca13844d08c93923a672fb2853266926c8`
