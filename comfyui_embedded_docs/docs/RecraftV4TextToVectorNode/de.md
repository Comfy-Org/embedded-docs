# RecraftV4TextToVectorNode

Der Node Recraft V4 Text to Vector erzeugt Scalable Vector Graphics (SVG)-Illustrationen aus einer Textbeschreibung unter Verwendung der Modelle Recraft V4 und V4.1. Er verbindet sich mit der Recraft API, um basierend auf Ihrem Prompt eine oder mehrere SVG-Dateien zu erzeugen, und kann einen vorhandenen Vektorstil anwenden oder aus Referenzbildern einen neuen erstellen – wenn Referenzbilder verwendet werden, wird der erstellte Stil als `style_id` zur Wiederverwendung zurückgegeben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Generierung zu verwendende Modell. Die recraftv4_styles-Modelle sind für stilkonforme Generierung ausgelegt und erfordern immer eine `style_id` oder `style_references`. Die Auswahl eines Modells ändert die verfügbaren `size`-Optionen. | DYNAMIC_COMBO | Ja | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"`<br>`"recraftv4_styles_vector"`<br>`"recraftv4_styles_pro_vector"` |
| `prompt` | Prompt für die Bildgenerierung. Maximal 10.000 Zeichen. | STRING | Ja | N/A |
| `negative_prompt` | Diese Eingabe wird ignoriert: negative Prompts werden von den Modellen Recraft V4 und V4.1 nicht unterstützt. | STRING | Ja | N/A |
| `n` | Die Anzahl der zu generierenden Bilder (Standard: 1). | INT | Ja | 1 bis 6 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 bis 18446744073709551615 |
| `recraft_controls` | Optionale zusätzliche Steuerelemente für die Generierung über den Node Recraft Controls. | CUSTOM | Nein | N/A |
| `style_id` | UUID eines anzuwendenden Recraft V4 Vektorstils, z. B. vom Node Recraft V4 Create Style oder von der `style_id`-Ausgabe eines vorherigen Laufs. Kann nicht mit `style_references` kombiniert werden. | STRING | Nein | N/A |
| `style_match` | Wie genau der Stil befolgt werden soll: precise reproduziert ihn im Detail, flexible entspricht dem allgemeinen Erscheinungsbild. Wird nur verwendet, wenn ein Stil bereitgestellt wird (Standard: "precise"). | COMBO | Nein | `"precise"`<br>`"flexible"` |

### recraftv4_1_vector, recraftv4_1_utility_vector, recraftv4 und recraftv4_styles_vector Eingaben

Diese Modelle verwenden dieselben `size`-Optionen.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size` | Die Größe des generierten Bildes. Standard ist `"1024x1024"`. | COMBO | Ja | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector, recraftv4_pro und recraftv4_styles_pro_vector Eingaben

Diese Modelle verwenden dieselben `size`-Optionen.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size` | Die Größe des generierten Bildes. Standard ist `"2048x2048"`. | COMBO | Ja | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `style_references` | Referenzbilder, aus denen unterwegs ein Vektorstil erstellt wird, zusätzlich zur Generierung abgerechnet. Der erstellte Stil wird als `style_id` zur Wiederverwendung zurückgegeben. Kann nicht mit `style_id` kombiniert werden. | IMAGE | Nein | Erweiterbarer Slot: 1..N Referenzbilder verbinden (bis zum Maximum des Nodes) |

**Hinweis:** Der Parameter `size` ist eine dynamische Eingabe, deren verfügbare Optionen sich je nach ausgewähltem `model` ändern. Der `seed`-Wert garantiert keine reproduzierbaren Ergebnisse von der externen API. Die Modelle `recraftv4_styles_vector` und `recraftv4_styles_pro_vector` erfordern immer einen Stil: Geben Sie eine `style_id` an oder verbinden Sie mindestens ein `style_references`-Bild. `style_id` und `style_references` können nicht zusammen verwendet werden – die Angabe beider löst einen Fehler aus, und `style_id` muss eine gültige UUID sein. Stilreferenzbilder sind in ihrer Anzahl begrenzt, und ihre gesamte kodierte Größe darf 10 MB nicht überschreiten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierten Scalable Vector Graphics (SVG)-Bilder. | SVG |
| `style_id` | Die von der Recraft API zurückgegebene Stil-UUID. Wenn Referenzbilder bereitgestellt werden, wird der erstellte Stil hier zur Wiederverwendung zurückgegeben; andernfalls eine leere Zeichenkette. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/de.md)

---
**Source fingerprint (SHA-256):** `182a40b206b164cf2e96c7344d23e4906b7d61b90e3000743a3fd31941e08539`
