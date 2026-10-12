# MiniMax H3 Erstes/letztes Frame zu Video

Dieser Node generiert ein Video aus einem Bild für das erste Frame und optional einem Bild für das letzte Frame unter Verwendung der MiniMax H3-Modelle. Der `model`-Selektor ändert, welche Generierungseinstellungen und Einschränkungen gelten, und das Seitenverhältnis des generierten Videos folgt den bereitgestellten Bildern.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell, das für die Videogenerierung verwendet werden soll. Bei Auswahl eines Modells werden unten die modellspezifischen Einstellungen angezeigt. | DYNAMIC_COMBO | Ja | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `first_frame` | Bild des ersten Frames für das Video. Das generierte Video folgt dem Seitenverhältnis dieses Bildes. | IMAGE | Ja | - |
| `last_frame` | Optionales Bild des letzten Frames für das Video. Wenn angegeben, wird das Video vom ersten Frame in Richtung dieses letzten Frames generiert. | IMAGE | Nein | - |
| `seed` | Zufälliger Seed. Dieselbe Anfrage mit demselben Seed liefert ähnliche, aber nicht garantiert identische Ergebnisse. Enthält eine Option für „Steuerung nach Generierung“. Standard: 42. | INT | Ja | 0 bis 4294967295 |
| `watermark` | Ob dem Video ein AIGC-Wasserzeichen hinzugefügt werden soll. Dies ist ein erweiterter Parameter. Wird nur vom `MiniMax H3`-Modell unterstützt. Standard: False. | BOOLEAN | Ja | True<br>False |

### MiniMax H3 Eingaben

Diese Einstellungen werden angezeigt, wenn `MiniMax H3` im `model`-Selektor ausgewählt wird.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. Muss mindestens ein Nicht-Leerzeichen-Zeichen enthalten. | STRING | Ja | Mehrzeiliger Text |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | "768P"<br>"2K" |
| `duration` | Dauer des Ausgabevideos in Sekunden. Standard: 5. | INT | Ja | 4 bis 15 |

### MiniMax H3 Max und MiniMax H3 Max Turbo Eingaben

Diese Einstellungen werden sowohl von `MiniMax H3 Max` als auch von `MiniMax H3 Max Turbo` gemeinsam verwendet. Bei Auswahl eines der beiden Modelle werden dieselben Einstellungen angezeigt.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. Darf nicht leer oder nur aus Leerzeichen bestehen und ist auf 50.000 Zeichen begrenzt. | STRING | Ja | Mehrzeiliger Text |
| `resolution` | Auflösung des Ausgabevideos. Standard: 768P. | COMBO | Ja | "480P"<br>"768P" |
| `duration` | Dauer des Ausgabevideos in Sekunden. Standard: 5. | INT | Ja | 5 bis 15 |
| `prompt_expansion_mode` | Wie viel Aufwand für das Umschreiben des Prompts vor der Generierung betrieben wird. Standard: balanced. | COMBO | Ja | "balanced"<br>"quality" |

**Hinweise zu Einschränkungen:**

- Der Prompt muss Text enthalten: Leere Prompts oder Prompts, die nur aus Leerzeichen bestehen, werden abgelehnt.
- Jedes bereitgestellte Frame-Bild muss mindestens 256 Pixel breit und 256 Pixel hoch sein, mit einem Breiten-Höhen-Seitenverhältnis zwischen 0,4 und 2,5 (ungefähr 2:5 bis 5:2). Diese Anforderung gilt für `first_frame` und, falls angegeben, für `last_frame`.
- Wenn `last_frame` weggelassen wird, wird das Video nur aus dem ersten Frame generiert.
- Das Ausgabevideo folgt dem Seitenverhältnis der bereitgestellten Bilder.
- `watermark` wird nur von `MiniMax H3` unterstützt. Das Aktivieren mit `MiniMax H3 Max` oder `MiniMax H3 Max Turbo` löst einen Fehler aus.
- Die Dauer reicht von 4 bis 15 Sekunden für `MiniMax H3` und von 5 bis 15 Sekunden für `MiniMax H3 Max` und `MiniMax H3 Max Turbo`.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Video, das aus dem ersten Frame und optional dem letzten Frame unter Verwendung des ausgewählten MiniMax H3-Modells erstellt wurde. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/de.md)

---
**Source fingerprint (SHA-256):** `6eaf895e6e9e46b9a1efb1dd13e951040e12e865cc73d7741ab7546f5f8f9ec0`
