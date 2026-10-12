# Ideogram V4

Erzeugt Bilder mit dem Ideogram 4.0-Modell aus einem Text-Prompt. Dieser Node sendet Ihre Textbeschreibung an die Ideogram-API und gibt das generierte Bild als Ausgabe-Tensor zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Bilderzeugung. | STRING | Ja | Keine Einschränkungen |
| `resolution` | Die Auflösung des generierten Bildes. Standard: "Auto", wodurch das Modell die beste Auflösung wählen kann. | COMBO | Ja | `"Auto"`<br>`"2048x2048 (1:1)"`<br>`"1440x2880 (1:2)"`<br>`"2880x1440 (2:1)"`<br>`"1664x2496 (2:3)"`<br>`"2496x1664 (3:2)"`<br>`"1792x2240 (4:5)"`<br>`"2240x1792 (5:4)"`<br>`"1440x2560 (9:16)"`<br>`"2560x1440 (16:9)"`<br>`"1600x2560 (5:8)"`<br>`"2560x1600 (8:5)"`<br>`"1728x2304 (3:4)"`<br>`"2304x1728 (4:3)"`<br>`"1296x3168 (9:22)"`<br>`"3168x1296 (22:9)"`<br>`"1152x2944 (9:23)"`<br>`"2944x1152 (23:9)"`<br>`"1248x3328 (3:8)"`<br>`"3328x1248 (8:3)"`<br>`"1280x3072 (5:12)"`<br>`"3072x1280 (12:5)"` |
| `rendering_speed` | Steuert die Abwägung zwischen Generierungsgeschwindigkeit und Qualität. Standard: "DEFAULT". | COMBO | Ja | `"DEFAULT"`<br>`"TURBO"`<br>`"QUALITY"` |
| `seed` | Seed für reproduzierbare Generierung. Standard: 0. | INT | Ja | Min: 0<br>Max: 2147483647 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das generierte Bild als Tensor. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV4/de.md)

---
**Source fingerprint (SHA-256):** `47a486824211d34b9109c5038b0b094d192c4e243c0a6c4ceab13af3bdabe6e4`
