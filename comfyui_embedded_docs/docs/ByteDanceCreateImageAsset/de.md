# ByteDanceCreateImageAsset

Dieser Node erstellt ein persönliches Bild-Asset für den Seedance 2.0-Dienst von ByteDance. Er lädt ein Eingabebild hoch und registriert es in einer angegebenen Asset-Gruppe. Wenn keine Gruppen-ID angegeben wird, startet er einen Prozess zur Authentifizierung als reale Person in Ihrem Browser, um eine neue Gruppe zu erstellen, bevor das Asset hinzugefügt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Bild, das als persönliches Asset registriert werden soll. | IMAGE | Ja |  |
| `group_id` | Wiederverwenden Sie eine vorhandene Seedance-Asset-Gruppen-ID, um die erneute Überprüfung derselben realen Person zu überspringen. Leer lassen, um die Authentifizierung als reale Person im Browser durchzuführen und eine neue Gruppe zu erstellen (Standard: leer). | STRING | Nein |  |

**Bildbeschränkungen:**
- Die Bildbreite muss zwischen 300 und 6000 Pixeln liegen.
- Die Bildhöhe muss zwischen 300 und 6000 Pixeln liegen.
- Das Seitenverhältnis des Bildes muss zwischen 0,4:1 und 2,5:1 liegen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `asset_id` | Die eindeutige Kennung für das neu erstellte Bild-Asset. | STRING |
| `group_id` | Die Kennung für die Asset-Gruppe. Dies ist entweder die angegebene `group_id` oder eine neu erstellte. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/de.md)

---
**Source fingerprint (SHA-256):** `44d2bc880cbd8780ce1deb27eee5e41dc43973653751b0022a2631df725b155d`
