# Video erstellen

Der Node „Create Video“ kombiniert eine Sequenz von Bildern zu einem Video. Sie können die Wiedergabegeschwindigkeit in Bildern pro Sekunde festlegen, optional Audio hinzufügen und das Komprimierungsformat, die Bittiefe sowie den Farbraum des resultierenden Videos wählen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `images` | Die Bilder, aus denen ein Video erstellt werden soll. | IMAGE | Ja | - |
| `fps` | Die Bilder pro Sekunde für die Wiedergabegeschwindigkeit des Videos (Standard: 30.0). | FLOAT | Ja | 1.0 - 120.0 |
| `audio` | Das Audio, das dem Video hinzugefügt werden soll. | AUDIO | Nein | - |
| `bit_depth` | Auto verwendet 8-Bit für sRGB und 10-Bit für HDR und HDR PQ. Die expliziten Auswahlmöglichkeiten 8-Bit und 10-Bit sind unabhängig vom Farbraum. (Standard: "auto") | COMBO | Nein | `"auto"`<br>8<br>10 |
| `color_space` | Farbraum der Eingabebilder. HDR wählt BT.2020/HLG und HDR PQ wählt BT.2020/PQ. (Standard: "sRGB") | COMBO | Nein | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `chroma_subsampling` | 444 behält die volle Farbauflösung bei, 422 halbiert die horizontale Farbauflösung und 420 halbiert beide Achsen. Auto verwendet den Standardwert des Codecs. Nicht unterstützte Auswahlmöglichkeiten verwenden den nächstgelegenen unterstützten Modus und geben eine Warnung in der Konsole aus. (Standard: "auto") | COMBO | Nein | `"auto"`<br>`"444"`<br>`"422"`<br>`"420"` |
| `codec` | Kodiert das Video optional sofort. None behält die Bilder in Tensorform; Auto verwendet H.264. (Standard: "none") | COMBO | Nein | `"none"`<br>Verfügbare Videocodec-Optionen aus der Videocodec-Liste (z. B. `"auto"` und andere unterstützte Codecs) |

Hinweis: Wenn `bit_depth` auf `"auto"` gesetzt ist, verwendet der Node automatisch 10-Bit für die Farbräume HDR und HDR PQ und 8-Bit für sRGB.

Hinweis: Der Parameter `codec` ist eine erweiterte Option. Wenn er auf `"none"` belassen wird, bleibt die Ausgabe in Tensorform; die Auswahl eines anderen Codecs kodiert das Video sofort.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Das generierte Video, das die Eingabebilder und optionales Audio enthält. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/de.md)

---
**Source fingerprint (SHA-256):** `614285ac3a38eedb63fd72f8b70f776b441b1b043707f4b21f587f70e2e071fa`
