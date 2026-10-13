# Higgsfield Genjutsu Motion Transfer

Der **Higgsfield Genjutsu Motion Transfer**-Node gestaltet ein Video mit neuen Charakteren, Schauplätzen oder Stilen aus Referenzbildern neu, während Bewegung, Kameraführung, Timing und Audio des Quellclips beibehalten werden. Verbinden Sie den Clip, der neu gestaltet werden soll, und ein oder mehrere Referenzbilder, die das neue Aussehen beschreiben, und beschreiben Sie anschließend das Ergebnis im Prompt. Die Anfrage wird an die Higgsfield-API gesendet und das generierte Video wird zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. Bei Auswahl eines Modells werden die dafür spezifischen Parameter eingeblendet: `video`, `reference_images`, `prompt`, `resolution` und `seed`. | DYNAMIC_COMBO | Ja | `"genjutsu-v1.0"` |
| `video` | Quellvideo, dessen Bewegung, Kameraführung, Timing und Audio beibehalten werden. Mindestens 4 Sekunden; nur die ersten 30 Sekunden werden verwendet. | VIDEO | Ja | 4 bis 30 Sekunden |
| `reference_images` | Erweiterbarer Slot: Verbinden Sie 1 bis 8 Bilder (`image_1`, `image_2`, ...) der zu verwendenden Charaktere, Schauplätze oder Stile. Eine gebündelte Eingabe zählt einmal pro Bild. | IMAGE | Ja | 1 bis 8 Bilder |
| `prompt` | Optional. Beschreiben Sie das Ergebnis, zum Beispiel welche Referenz welche Person ersetzt oder eine neue Umgebung. (Standard: leer) | STRING | Ja | Beliebiger Text |
| `resolution` | Auflösung des Ausgabevideos. (Standard: `"720p"`) | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Dieser Parameter besitzt die Funktionalität „Steuerung nach Generierung“ (Standard: 42). | INT | Ja | 0 bis 2147483647 |

Das Quellvideo wird vor dem Senden der Anfrage validiert: Ein Clip, der kürzer als 4 Sekunden ist, wird abgelehnt, und ein Clip, der länger als 30 Sekunden ist, wird auf seine ersten 30 Sekunden gekürzt. Sein Audio wird in das Ergebnis übernommen. Referenzbilder werden zuerst hochgeladen, und die Gesamtzahl der Bilder über alle verbundenen Slots darf 8 nicht überschreiten, obwohl der Node acht Slots bereitstellt. Die Inhaltsmoderation von Higgsfield kann die Eingabe oder das Ergebnis ablehnen, wodurch ein Fehler ausgelöst wird, anstatt ein Video zurückzugeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Die neu gestaltete Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiggsfieldMotionTransferNode/de.md)

---
**Source fingerprint (SHA-256):** `f0c30fb93dd2af8d564335290fdb6ff61c38e36ab62cef9641fd1aa81cc10cd2`
