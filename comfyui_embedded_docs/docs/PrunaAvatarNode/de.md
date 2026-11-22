# Pruna P-Video-2 Pro Avatar

Verwandeln Sie ein Porträt in ein sprechendes Video mit Pruna P-Video-2 Pro Avatar. Sprechen Sie ein Skript per Text-to-Speech ein oder verbinden Sie Ihr eigenes Audio – die Person wird dann lippensynchron dazu.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `Bild` | Porträt, von dem das Video ausgeht. Seitenverhältnisse von 1:2 bis 4:1 bleiben erhalten; extremere Bilder wie 1:5 werden auf 9:16 oder 16:9 zugeschnitten. | IMAGE | Ja | - |
| `Sprache` | Steuert das Video über ein Text-to-Speech-Skript oder über eigenes Audio. Bei Auswahl einer Option werden die zugehörigen Eingaben darunter eingeblendet. | DYNAMIC_COMBO | Ja | `"script"`<br>`"audio"` |
| `Prompt` | Beschreibt, was das Video zeigt (Standard: "The person is talking."). Bis zu 5000 Zeichen. | STRING | Ja | Bis zu 5000 Zeichen |
| `Auflösung` | Ausgabauflösung (Standard: `"768p"`). 1080p, 2k und 4k skalieren das generierte 768p-Video hoch. | COMBO | Ja | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `enhance_prompt` | Fügt die im Porträt erkennbare Bewegung wie Hintergrund, Licht und Körperbewegung zum Prompt hinzu (Standard: True). Erweiterte Einstellung. | BOOLEAN | Ja | `True`<br>`False` |
| `Seed` | Seed für die Generierung (Standard: 42). Derselbe Seed reproduziert ein Ergebnis nur dann exakt, wenn `enhance_prompt` deaktiviert ist. | INT | Ja | 0 bis 2147483647<br>Schritt: 1 |

### `"script"` Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `Skript` | Worte, die die Person spricht. Das Video entspricht der Länge der Sprache; Sprache, die länger als 3 Minuten ist, wird bei 3 Minuten abgeschnitten. | STRING | Ja | Beliebiger Text |
| `Stimme` | Stimme für die Sprache (Standard: `"Zephyr (Female)"`). | COMBO | Ja | 30 voreingestellte Stimmen |
| `Sprache` | Sprache, in der das Skript gesprochen wird (Standard: `"English (US)"`). | COMBO | Ja | `"English (US)"`<br>`"English (UK)"`<br>`"Spanish"`<br>`"French"`<br>`"German"`<br>`"Italian"`<br>`"Portuguese (Brazil)"`<br>`"Japanese"`<br>`"Korean"`<br>`"Hindi"` |
| `voice_prompt` | Wie das Skript gesprochen wird: Tonfall, Tempo, Akzent, Emotion (Standard: "Say the following."). Wird selbst nicht gesprochen. | STRING | Ja | Beliebiger Text |

### `"audio"` Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `speech.audio` | Sprache, zu der die Person lippensynchron ist. Das Video entspricht ihrer Länge. | AUDIO | Ja | Mindestens 1 Sekunde |

**Hinweise:**

- Eine längere Ausgabe begrenzt die Audiolänge: 2k akzeptiert bis zu 150 Sekunden Audio und 4k bis zu 60 Sekunden. Längeres Audio bei diesen Auflösungen bricht den Node mit einem Fehler ab; verwenden Sie daher eine niedrigere Auflösung oder einen kürzeren Clip.
- Das Seitenverhältnis des Porträts bestimmt die Form der Ausgabe. Sehr hohe oder sehr breite Porträts werden zugeschnitten statt aufgefüllt; halten Sie das Motiv daher von den Rändern frei.
- Bei deaktiviertem `enhance_prompt` wird der Prompt unverändert verwendet – genau das ermöglicht es, mit demselben Seed ein Ergebnis exakt zu reproduzieren.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das aus dem Porträt generierte sprechende Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaAvatarNode/de.md)

---
**Source fingerprint (SHA-256):** `58efc7a110734f8da0a771371c5230908bf8226a946d69c5315e51e259630043`
