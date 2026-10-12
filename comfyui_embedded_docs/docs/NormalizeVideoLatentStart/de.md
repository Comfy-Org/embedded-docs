# NormalizeVideoLatentStart

Dieser Node passt die ersten wenigen Frames eines Video-Latents an, damit sie den darauffolgenden Frames ähnlicher sehen. Er berechnet den Durchschnitt und die Variation aus einer Reihe von Referenz-Frames weiter hinten im Video und wendet dieselben Eigenschaften auf die Start-Frames an. Dies hilft, Unterschiede zwischen den Start-Frames und dem Rest des Videos zu verringern, wodurch ein glatterer und konsistenterer Übergang entsteht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `latent` | Die zu verarbeitende Video-Latent-Repräsentation. | LATENT | Ja | - |
| `start_frame_count` | Anzahl der zu normalisierenden Latent-Frames, vom Anfang an gezählt (Standard: 4). | INT | Ja | 1 bis 16384 (maximale Auflösung) |
| `reference_frame_count` | Anzahl der Latent-Frames nach den Start-Frames, die als Referenz verwendet werden (Standard: 5). | INT | Ja | 1 bis 16384 (maximale Auflösung) |

**Hinweis:** Die Referenz-Frames werden direkt nach den `start_frame_count` Frames entnommen. Wenn weniger Frames verfügbar sind, als `reference_frame_count` anfordert, verwendet der Node so viele, wie verfügbar sind (höchstens einen weniger als die Gesamtzahl der Frames des Latents). Wenn das Video-Latent nur 1 Frame hat, wird keine Normalisierung durchgeführt und das ursprüngliche Latent unverändert zurückgegeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Das verarbeitete Video-Latent mit normalisierten Start-Frames. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/de.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
