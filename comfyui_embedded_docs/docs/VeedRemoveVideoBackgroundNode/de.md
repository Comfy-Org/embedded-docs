# VEED Remove Video Background

Schneiden Sie das Motiv mit VEED aus einem Video aus und geben Sie die Frames zusammen mit einer Alpha-Maske zurück. Verwenden Sie die beiden Ausgaben für das Compositing oder leiten Sie sie durch Join Image with Alpha und Save WEBM, um ein transparentes Video zu schreiben. Wählen Sie `"standard"` für die besten Kanten auf jedem Hintergrund, `"fast"`, wenn Geschwindigkeit zählt, oder `"green screen"` für Aufnahmen vor einem grünen Hintergrund.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Segmentierungsmodell: `"standard"` für jeden Hintergrund mit den besten Kanten und Ausgabe bis zu 3840x2160, `"fast"` für ein schnelleres Ergebnis bis zu 1920x1080 oder `"green screen"`, um einen grünen Hintergrund bis zu 3840x2160 per Keying zu entfernen. Größere Videos werden herunterskaliert. Die Auswahl einer Option zeigt deren Parameter an. | DYNAMIC_COMBO | Ja | `"standard"`<br>`"fast"`<br>`"green screen"` |
| `video` | Das Video, aus dem das Motiv freigestellt werden soll. Bis zu 60 Sekunden. | VIDEO | Ja | Bis zu 60 Sekunden |
| `refine_foreground_edges` | Sauberere Kanten bei Haaren, Fell und feinen Details. Das Deaktivieren senkt den Preis. Verfügbar für `"standard"` und `"fast"` (Standard: True). | BOOLEAN | Ja | false<br>true |
| `subject_is_person` | Deaktivieren, wenn das Motiv ein Objekt oder ein Tier ist. Verfügbar für `"standard"` und `"fast"` (Standard: True). | BOOLEAN | Ja | false<br>true |
| `spill_suppression_strength` | Wie stark ein Grünstich vom Motiv entfernt wird. Erhöhen Sie den Wert, wenn grüne Flecken bleiben; verringern Sie ihn, wenn sich die Farben des Motivs verschieben. Verfügbar für `"green screen"` (Standard: 0.8). | FLOAT | Ja | 0.0 bis 1.0 (Schritt 0.01) |

Der Clip ist auf 60 Sekunden begrenzt; längere Videos werden mit einem Fehler abgelehnt. Die Maske ist 1, wo der Hintergrund entfernt wurde; verwenden Sie daher Invert Mask vor Image Composite Masked, wenn Sie stattdessen das Motiv behalten möchten.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Die Video-Frames mit entferntem Hintergrund. | IMAGE |
| `mask` | 1, wo der Hintergrund entfernt wurde, pro Frame. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedRemoveVideoBackgroundNode/de.md)

---
**Source fingerprint (SHA-256):** `1bf52a380ab09437a5a57f70215856d4ea0055f78ce8b42fe2a2b87d686e8d26`
