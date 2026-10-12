# KlingDualCharacterVideoEffectNode

Der Kling Dual Character Video Effect Node erstellt Videos mit Spezialeffekten basierend auf der ausgewählten Szene. Er nimmt zwei Bilder entgegen und positioniert das erste Bild auf der linken Seite und das zweite Bild auf der rechten Seite des zusammengesetzten Videos. Je nach gewählter Effektszene werden unterschiedliche visuelle Effekte angewendet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image_left` | Bild für die linke Seite | IMAGE | Ja | - |
| `image_right` | Bild für die rechte Seite | IMAGE | Ja | - |
| `effect_scene` | Der Typ der Spezialeffekt-Szene, die auf die Videogenerierung angewendet wird | COMBO | Ja | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` |
| `model_name` | Das Modell, das für Charaktereffekte verwendet werden soll (Standard: "kling-v1") | COMBO | Nein | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` |
| `mode` | Der Videogenerierungsmodus (Standard: "std") | COMBO | Nein | `"std"`<br>`"pro"` |
| `duration` | Die Dauer des generierten Videos in Sekunden | COMBO | Ja | `"5"`<br>`"10"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das generierte Video mit Effekten für zwei Charaktere | VIDEO |
| `duration` | Die Dauerinformation des generierten Videos | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/de.md)

---
**Source fingerprint (SHA-256):** `314fc23940225eb4559ecc74f333bb23e9a4939bbb884c93341f4d6f6e7b64df`
