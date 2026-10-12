# RecraftV4TextToImageNode

Erzeugt Bilder aus Text-Prompts mit den Modellen Recraft V4 und V4.1. Es sendet den Prompt und die ausgewählten Einstellungen an die Recraft API und gibt das generierte Bild oder die generierten Bilder zurück. Wenn Stilreferenzbilder verwendet werden, wird auch die erzeugte Stil-ID zurückgegeben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Generierung zu verwendende Modell. Die recraftv4_styles-Modelle sind für stilkonsistente Generierung ausgelegt und erfordern immer eine style_id oder style_references. `recraftv4_1_flash` ist das schnellste und günstigste Modell und unterstützt überhaupt keine Stile. | DYNAMIC_COMBO | Ja | "recraftv4_1"<br>"recraftv4_1_flash"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | Prompt für die Bildgenerierung. Maximal 10.000 Zeichen. | STRING | Ja | 1 bis 10000 Zeichen |
| `negative_prompt` | Dieser Eingabewert wird ignoriert: Negative Prompts werden von den Modellen Recraft V4 und V4.1 nicht unterstützt. | STRING | Ja | N/A |
| `n` | Die Anzahl der zu generierenden Bilder (Standard: 1). | INT | Ja | 1 bis 6 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 bis 18446744073709551615 |
| `recraft_controls` | Optionale zusätzliche Steuerungen für die Generierung über den Recraft Controls Node. | CUSTOM | Nein | N/A |
| `style_id` | UUID eines Recraft-V4-Stils, der angewendet werden soll, z. B. aus dem Recraft V4 Create Style Node oder der style_id-Ausgabe eines vorherigen Laufs. Kann nicht mit style_references kombiniert werden (Standard: leer). | STRING | Nein | Gültige UUID-Zeichenfolge |
| `style_match` | Wie eng der Stil befolgt wird: precise reproduziert ihn im Detail, flexible entspricht dem allgemeinen Erscheinungsbild. Wird nur verwendet, wenn ein Stil bereitgestellt wird (Standard: "precise"). | COMBO | Nein | "precise"<br>"flexible" |

### recraftv4_1, recraftv4_1_flash, recraftv4_1_utility, recraftv4 und recraftv4_styles Eingaben

Diese Modelle verwenden denselben Parameter `size`.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size` | Die Größe des generierten Bildes (Standard: "1024x1024"). | COMBO | Ja | Mehrere Optionen verfügbar (standardmäßige Recraft-V4-Größen; enthält "1024x1024") |

### recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_pro und recraftv4_styles_pro Eingaben

Diese Modelle verwenden denselben Parameter `size`.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size` | Die Größe des generierten Bildes (Standard: "2048x2048"). | COMBO | Ja | Mehrere Optionen verfügbar (Recraft V4 Pro-Größen; enthält "2048x2048") |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `style_references` | Referenzbilder, um spontan einen Stil zu erstellen; werden zusätzlich zur Generierung abgerechnet. Der erstellte Stil wird als style_id zur Wiederverwendung zurückgegeben. Kann nicht mit style_id kombiniert werden. Erweiterbarer Slot: 1..N Bilder verbinden (style_reference_1, style_reference_2, ...). | IMAGE | Nein | 0 bis zur maximalen Anzahl von Referenzbildern, die die Recraft API zulässt; die gesamte kodierte Größe darf 10 MB nicht überschreiten |

**Hinweis:** Der Parameter `size` ist eine dynamische Eingabe, deren verfügbare Optionen sich je nach ausgewähltem `model` ändern. Die Modelle `recraftv4_styles` und `recraftv4_styles_pro` erfordern immer einen Stil: Verbinden Sie Stilreferenzbilder oder geben Sie eine `style_id` an. Die Eingaben `style_id` und `style_references` schließen sich gegenseitig aus — geben Sie nur eine davon an. Eine `style_id` muss eine gültige UUID sein. Die Eingabe `style_match` wird nur verwendet, wenn ein Stil bereitgestellt wird. Stilreferenzbilder werden zusätzlich zur Generierung abgerechnet, und ihre gesamte kodierte Größe darf 10 MB nicht überschreiten. Der Wert `seed` garantiert keine reproduzierbaren Bildausgaben. Wenn Sie eine Stil-ID aus der Infinite Style Library verwenden, stellen Sie sicher, dass es sich nicht um einen Vector-Art-Stil handelt, da dies SVG-Daten anstelle eines Bildes zurückgeben kann.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das generierte Bild oder der Batch von Bildern. | IMAGE |
| `style_id` | Die von dieser Generierung verwendete oder erstellte Stil-ID. Wenn Stilreferenzbilder bereitgestellt werden, wird der erstellte Stil hier zur Wiederverwendung zurückgegeben; leerer String, wenn kein Stil verwendet wird. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/de.md)

---
**Source fingerprint (SHA-256):** `690286e663f27b525e58f81a7f883e490dacd48c1a34ee7b8e9ad4efd9935ff1`
