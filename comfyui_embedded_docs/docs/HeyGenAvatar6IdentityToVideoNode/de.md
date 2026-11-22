# HeyGen Avatar 6 Identity to Video

Erzeugen Sie ein sprechendes Video eines HeyGen-Avatars mit Avatar 6. Wählen Sie einen der integrierten Looks, die Avatar 6 unterstützen, oder fügen Sie Ihre eigene HeyGen-Avatar-ID ein, und steuern Sie ihn anschließend mit einem Textskript oder Ihrem eigenen Audio.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Modell` | Modellauswahl. `"heygen-avatar-6-turbo"` ist die günstigere, schnellere Stufe; beide Modelle akzeptieren dieselben Eingaben und Auflösungen. | COMBO | Ja | `"heygen-avatar-6"`<br>`"heygen-avatar-6-turbo"` |
| `Avatar` | Der Avatar-Look, der präsentiert werden soll. Die 19 integrierten Looks, die Avatar 6 unterstützen, werden direkt aufgelistet; `custom avatar` blendet `custom_avatar_id` für einen Look ein, den Sie in HeyGen erstellt haben. | DYNAMIC_COMBO | Ja | 19 integrierte Looks<br>`custom avatar` |
| `Sprache` | Steuern Sie den Avatar mit einem Textskript (HeyGen Text-to-Speech) oder Ihrem eigenen Audio. Anzeigename: Sprachquelle. | DYNAMIC_COMBO | Ja | `"script"`<br>`"audio"` |
| `Auflösung` | Auflösung des Ausgabevideos. Standard: `"1080p"`. | COMBO | Ja | `"1080p"`<br>`"2k"` |
| `Seitenverhältnis` | Seitenverhältnis des Ausgabevideos. `"auto"` folgt dem eigenen Filmmaterial des Avatar-Looks. Standard: `"auto"`. | COMBO | Ja | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `Bewegungs-Prompt` | Optionale Anweisung für Gesten, Ausdruck, Körperhaltung und Kamerabewegung. Standard: leerer String. | STRING | Ja | Mehrzeiliger Text |
| `Bewegungsausdrucksstärke` | `"less"` ergibt weniger und kleinere Gesten. Der Motion-Prompt hat Vorrang, wo sich beide überschneiden. Standard: `"default"`. | COMBO | Ja | `"less"`<br>`"default"` |
| `Seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Ja | 0 bis 2147483647 |

### `custom avatar` Eingaben

Diese Eingaben erscheinen, wenn `avatar` auf `custom avatar` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `custom_avatar_id` | HeyGen-Avatar-Look-ID, die Avatar 6 unterstützt, zum Beispiel eine, die mit HeyGen Create Avatar erstellt wurde. Standard: leerer String. | STRING | Ja | - |

### `script` Spracheingaben

Diese Eingaben erscheinen, wenn `speech` auf `"script"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `text` | Text, den der Avatar sprechen soll. Standard: leerer String. | STRING | Ja | Bis zu 5000 Zeichen |
| `voice` | Stimme für das Skript. Die Standardoption verwendet die Stimme, die HeyGen dem Avatar zugewiesen hat; Avatare, die mit HeyGen Create Avatar erstellt wurden, haben keine, wählen Sie daher eine Stimme für sie. | COMBO | Ja | `"(avatar's default voice)"` plus HeyGens allgemeine Stimmenliste |
| `custom_voice_id` | Optionale HeyGen-Stimmen-ID. Wenn festgelegt, überschreibt sie die oben ausgewählte Stimme. Standard: leerer String. | STRING | Nein | - |
| `voice_speed` | Multiplikator für die Sprachgeschwindigkeit. Standard: 1.0. | FLOAT | Nein | 0.5 bis 1.5 (Schritt: 0.05) |

### `audio` Spracheingaben

Diese Eingaben erscheinen, wenn `speech` auf `"audio"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `audio` | Sprache für den Avatar. Die Videolänge richtet sich nach dem Audio. | AUDIO | Ja | 0.5 Sekunden bis 10 Minuten |

**Einschränkungen und Verhalten:**

* `custom avatar` benötigt eine nicht leere Avatar-ID, andernfalls löst der Node einen Fehler aus.
* Ein Skript ist auf 5000 Zeichen und Audio auf 10 Minuten begrenzt.
* Die Preisgestaltung erfolgt pro Sekunde des Ausgabevideos und hängt vom Modell und der Auflösung ab.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte sprechende Video, das von HeyGen heruntergeladen wird, sobald das Rendering abgeschlossen ist. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatar6IdentityToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `952146c3790333883ad08b7031853eb7021c8d18c59e58389b5d57b548820944`
