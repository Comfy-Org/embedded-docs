# ByteDance Video-Asset erstellen

Dieser Node erstellt ein persönliches Video-Asset für Seedance 2.0. Er lädt Ihr Eingabevideo hoch und registriert es in einer angegebenen Asset-Gruppe. Wenn Sie keine Gruppen-ID angeben, führt er Sie durch einen Echtpersonen-Verifizierungsprozess in Ihrem Browser, um zuerst eine neue Gruppe zu erstellen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Video, das als persönliches Asset registriert werden soll. | VIDEO | Ja | - |
| `group_id` | Verwenden Sie eine vorhandene Seedance-Asset-Gruppen-ID erneut, um die wiederholte menschliche Verifizierung für dieselbe Person zu überspringen. Leer lassen, um die Echtpersonen-Authentifizierung im Browser auszuführen und eine neue Gruppe zu erstellen. (Standard: leere Zeichenkette) | STRING | Nein | - |

**Video-Einschränkungen:**
- **Dauer:** Muss zwischen 2 und 15 Sekunden liegen.
- **Abmessungen:** Breite und Höhe müssen jeweils zwischen 300 und 6000 Pixeln liegen.
- **Seitenverhältnis:** Das Breite-zu-Höhe-Verhältnis muss zwischen 0,4 und 2,5 liegen.
- **Gesamtpixel:** Die Gesamtzahl der Pixel (Breite × Höhe) muss zwischen 409.600 und 927.408 liegen.
- **Bildrate:** Muss zwischen 24 und 60 Bildern pro Sekunde (FPS) liegen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `asset_id` | Die eindeutige Kennung für das neu erstellte Video-Asset. | STRING |
| `group_id` | Die Kennung der Asset-Gruppe, die das neue Video enthält. Dies ist entweder die angegebene `group_id` oder eine neu erstellte. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateVideoAsset/de.md)

---
**Source fingerprint (SHA-256):** `2c7376185f3273a80c763c2c9bd41305575b58e7902200ff77bebb609aea58b8`
