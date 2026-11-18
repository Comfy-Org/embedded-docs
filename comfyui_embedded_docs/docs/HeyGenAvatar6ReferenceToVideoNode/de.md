# HeyGen Avatar 6 Reference to Video

Erzeugen Sie mit HeyGen Avatar 6 ein Video, in dem eine Person die angeschlossene Audiodatei spricht, und verwenden Sie dabei ein Foto oder ein Video als Referenz. Avatar 6 rekonstruiert das Gesicht und die Szene aus dieser Referenz, sodass dieselbe Audiodatei ein Standbild, einen vorhandenen Clip oder beides antreiben kann.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modellauswahl; die Auswahl eines Modells blendet dessen Eingaben unten ein. `"heygen-avatar-6-turbo"` ist die günstigere, schnellere Stufe. | DYNAMIC_COMBO | Ja | `"heygen-avatar-6"`<br>`"heygen-avatar-6-turbo"` |

### `heygen-avatar-6` Eingaben

`"heygen-avatar-6-turbo"` bietet dieselben Eingaben mit denselben Grenzwerten.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Optionales Foto der zu animierenden Person oder Figur. Es legt das Aussehen und die Szene fest und wird nicht als erstes Frame verwendet. | IMAGE | Nein | Einzelbild |
| `video` | Optionales Video einer animierten oder stilisierten Figur, das zeigt, wie sie spricht und sich bewegt. Längere Videos werden auf die ersten 30 Sekunden gekürzt. | VIDEO | Nein | 2 bis 30 Sekunden |
| `audio` | Sprache für den Avatar. Die Videolänge richtet sich nach der Audiodatei. | AUDIO | Ja | 1.5 Sekunden bis 10 Minuten |
| `resolution` | Auflösung des Ausgabevideos. Standard: `"1080p"`. | COMBO | Ja | `"1080p"`<br>`"2k"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"auto"` behält die Form des Bildes bzw. des Videos bei, wenn kein Bild angeschlossen ist; andere Werte rahmen die Szene neu ein. Standard: `"auto"`. | COMBO | Ja | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `motion_prompt` | Optionale Anweisung für Gesten, Mimik, Körperhaltung und Kamerabewegung. Standard: leerer String. | STRING | Ja | Mehrzeiliger Text, bis zu 1200 Zeichen |
| `motion_expressiveness` | `"less"` erzeugt weniger und kleinere Gesten. Der Motion-Prompt hat Vorrang, wo sich beide überschneiden. Standard: `"default"`. | COMBO | Ja | `"less"`<br>`"default"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen und Verhalten:**

* Verbinden Sie ein Bild, ein Video oder beides; ohne eines davon löst der Node einen Fehler aus.
* Der Bild-Eingang muss genau ein Bild enthalten, keinen Batch.
* Referenzvideos realistischer Personen werden abgelehnt. Verwenden Sie ein Video einer animierten oder stilisierten Figur oder verbinden Sie stattdessen ein Foto der Person.
* Ein Referenzvideo muss mindestens 2 Sekunden lang und höchstens 50 MB groß sein.
* Die Preisgestaltung erfolgt pro Sekunde Ausgabevideo und hängt vom Modell und der Auflösung ab.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte sprechende Video, das nach Abschluss des Renderings von HeyGen heruntergeladen wird. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatar6ReferenceToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `1a50342827511e355a1d857c34e8bbfc0b74ca7b003dca783b76fcd151413ff8`
