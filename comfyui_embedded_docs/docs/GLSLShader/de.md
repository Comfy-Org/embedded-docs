# GLSLShader

Der **GLSL Shader**-Node ermöglicht es Ihnen, benutzerdefinierte Fragment-Shader in **GLSL ES 3.00** (WebGL-2.0-kompatibel) zu schreiben, um Bilder direkt auf der GPU zu verarbeiten. Sie können Bildeffekte wie Weichzeichnen, Farbkorrektur, Filmkorn, Glow und vieles mehr erstellen – alles mit GPU-Geschwindigkeit.

<Note>
Der GLSL Shader-Node ist derzeit als **experimentell** gekennzeichnet, daher kann der Node in zukünftigen Versionen aktualisiert und erweitert werden.
</Note>

## Minimaler Shader

Der einfachste mögliche Shader – ein Passthrough, der das Eingabebild unverändert ausgibt:

```glsl
#version 300 es
precision highp float;

uniform sampler2D u_image0;

in vec2 v_texCoord;
layout(location = 0) out vec4 fragColor0;

void main() {
    fragColor0 = texture(u_image0, v_texCoord);
}
```

<Note>
**Warum GLSL ES 3.00?** Shader müssen in zwei Umgebungen laufen: im **Browser** (über WebGL 2.0, das nur GLSL ES 3.00 unterstützt) für die Live-Vorschau im ComfyUI-Frontend und im **Python-Backend** (über Desktop-OpenGL), wenn der Workflow ausgeführt wird. GLSL ES 3.00 ist der kleinste gemeinsame Nenner, der an beiden Stellen funktioniert.
</Note>

## Verfügbare Uniforms

Diese Uniforms werden automatisch von ComfyUI gesetzt. Sie müssen nicht alle davon deklarieren – deklarieren Sie nur die, die Sie verwenden.

### Bilder

| Uniform | Beschreibung | Typ |
| --- | --- | --- |
| `u_image0` – `u_image4` | Eingabebilder (bis zu 5). Werden mit `texture(u_image0, v_texCoord)` abgetastet. Bilder sind RGBA-Float-Texturen mit linearer Filterung und Clamp-to-Edge-Wrapping. | `sampler2D` |

### Gleitkommazahlen

| Uniform | Beschreibung | Typ |
| --- | --- | --- |
| `u_float0` – `u_float19` | Bis zu 20 benutzergesteuerte Float-Werte. Werden aus der Eingabegruppe **floats** am Node zugeordnet. | `float` |

### Ganzzahlen

| Uniform | Beschreibung | Typ |
| --- | --- | --- |
| `u_int0` – `u_int19` | Bis zu 20 benutzergesteuerte Ganzzahlwerte. Werden aus der Eingabegruppe **ints** am Node zugeordnet. | `int` |

<Note>
**Int-Uniforms als Dropdowns verwenden:** Int-Uniforms passen gut zum Index-Ausgang des **Custom Combo**-Nodes – Benutzer wählen eine Option aus einem Dropdown, und der Shader erhält den Index des ausgewählten Elements.

```glsl
const int BLEND_SCREEN  = 0;
const int BLEND_OVERLAY = 1;
const int BLEND_MULTIPLY = 2;

// ...

if (u_int0 == BLEND_SCREEN) {
    // ...
}
```
</Note>

### Boolesche Werte

| Uniform | Beschreibung | Typ |
| --- | --- | --- |
| `u_bool0` – `u_bool9` | Bis zu 10 benutzergesteuerte boolesche Werte. Werden aus der Eingabegruppe **bools** am Node zugeordnet. | `bool` |

### Kurven (1D-LUTs)

| Uniform | Beschreibung | Typ |
| --- | --- | --- |
| `u_curve0` – `u_curve3` | Bis zu 4 benutzereditierbare Kurven-LUTs aus der Eingabegruppe **curves**. Jede Kurve ist eine 1D-Lookup-Tabelle, die als einzeilige Textur gespeichert wird. | `sampler2D` |

<Note>
**Kurven-Uniforms verwenden:** Kurven ermöglichen es Benutzern, beliebige Tonwertabbildungsgraphen in der UI zu zeichnen (z. B. für Kontrast, Gamma, Grading pro Kanal oder jede benutzerdefinierte `input → output`-Neuzuordnung). Abtastung der Kurve mit Ihrem Eingabewert als X-Koordinate – denken Sie daran, ihn zuerst auf `[0, 1]` zu begrenzen:

```glsl
float applyCurve(sampler2D curve, float value) {
    return texture(curve, vec2(clamp(value, 0.0, 1.0), 0.5)).r;
}

// Usage: remap each RGB channel through a master curve
color.r = applyCurve(u_curve0, color.r);
color.g = applyCurve(u_curve0, color.g);
color.b = applyCurve(u_curve0, color.b);
```

Häufige Verwendungen: Master-RGB-Kurven, R/G/B-Kurven pro Kanal, luminanzgesteuerte Neuzuordnungen, benutzerdefiniertes Gamma und jeder Effekt, bei dem der Benutzer eine Antwortkurve visuell formen soll.
</Note>

### Auflösung

| Uniform | Beschreibung | Typ |
| --- | --- | --- |
| `u_resolution` | **Ausgabe**-Framebuffer-Abmessungen in Pixeln (`width, height`). Dies ist die Größe, in die Sie schreiben; sie kann von der Größe jedes Eingabebilds abweichen, wenn `size_mode` auf `"custom"` gesetzt ist. | `vec2` |

<Note>
**Texelgröße für die Abtastung berechnen:** Verwenden Sie nicht `1.0 / u_resolution`, um in einer Eingabetextur um ein Pixel zu schreiten. `u_resolution` ist die *Ausgabe*-Größe, die nicht mit der Größe der Eingabe übereinstimmen muss. Verwenden Sie stattdessen `textureSize()` auf der tatsächlichen Textur, die Sie abtasten:

```glsl
vec2 texel = 1.0 / vec2(textureSize(u_image0, 0));
```

Verwenden Sie `u_resolution` nur, wenn Sie die Ausgabe-Framebuffer-Abmessungen selbst benötigen (z. B. Berechnung von `gl_FragCoord.xy / u_resolution`, um Screen-Space-UVs zu erhalten).
</Note>

### Multi-Pass

| Uniform | Beschreibung | Typ |
| --- | --- | --- |
| `u_pass` | Aktueller Pass-Index (0-basiert). Nur sinnvoll bei Verwendung von `#pragma passes` – siehe [Multi-Pass-Ping-Pong-Rendering](#multi-pass-ping-pong-rendering) für Details. | `int` |

### Vertex-Shader-Ausgabe

| Varying | Beschreibung | Typ |
| --- | --- | --- |
| `v_texCoord` | Texturkoordinaten von (0,0) unten links bis (1,1) oben rechts. | `vec2` |

## Mehrere Ausgaben (MRT)

Der Node unterstützt bis zu **4 gleichzeitige Ausgaben** mithilfe von Multiple Render Targets. Deklarieren Sie zusätzliche Ausgaben mit expliziten Locations:

```glsl
#version 300 es
precision highp float;

uniform sampler2D u_image0;

in vec2 v_texCoord;
layout(location = 0) out vec4 fragColor0;
layout(location = 1) out vec4 fragColor1;
layout(location = 2) out vec4 fragColor2;
layout(location = 3) out vec4 fragColor3;

void main() {
    vec4 color = texture(u_image0, v_texCoord);
    fragColor0 = vec4(vec3(color.r), 1.0);  // Red channel
    fragColor1 = vec4(vec3(color.g), 1.0);  // Green channel
    fragColor2 = vec4(vec3(color.b), 1.0);  // Blue channel
    fragColor3 = vec4(vec3(color.a), 1.0);  // Alpha channel
}
```

Jeder `fragColor` wird der entsprechenden `IMAGE`-Ausgabe am Node zugeordnet. ComfyUI erkennt automatisch, welche Ausgaben Sie verwenden – ungenutzte Ausgaben sind schwarz.

## Multi-Pass-Ping-Pong-Rendering

Einige Effekte (wie separierbarer Weichzeichner) benötigen mehrere Durchläufe über das Bild. Verwenden Sie die Direktive `#pragma passes N`, um dies zu aktivieren:

```glsl
#version 300 es
#pragma passes 2
precision highp float;

uniform sampler2D u_image0;
uniform float u_float0;  // Blur radius
uniform int u_pass;

in vec2 v_texCoord;
layout(location = 0) out vec4 fragColor0;

void main() {
    vec2 texel = 1.0 / vec2(textureSize(u_image0, 0));
    int radius = int(ceil(u_float0));

    // Pass 0 = horizontal blur, Pass 1 = vertical blur
    vec2 dir = (u_pass == 0) ? vec2(1.0, 0.0) : vec2(0.0, 1.0);

    vec4 color = vec4(0.0);
    float total = 0.0;

    for (int i = -radius; i <= radius; i++) {
        vec2 offset = dir * float(i) * texel;
        float w = 1.0;  // box blur weight
        color += texture(u_image0, v_texCoord + offset) * w;
        total += w;
    }

    fragColor0 = color / total;
}
```

### So funktioniert Ping-Pong

1. **Pass 0**: Liest aus der ursprünglichen Eingabe `u_image0`, schreibt in eine interne Ping-Pong-Textur.
2. **Pass 1–N**: Liest über `u_image0` aus der *Ausgabe des vorherigen Passes* (die Bindung wird automatisch getauscht), schreibt in die andere Ping-Pong-Textur.
3. **Letzter Pass**: Schreibt in den tatsächlichen Ausgabe-Framebuffer (`fragColor0`).

<Note>
Bei Verwendung von Multi-Pass mit MRT (mehrere Ausgaben) nimmt nur die erste Ausgabe (`fragColor0`) am Ping-Pong teil. Der letzte Pass schreibt alle Ausgaben.
</Note>

## Beispiele

### Graustufenkonvertierung

```glsl
#version 300 es
precision highp float;

uniform sampler2D u_image0;
in vec2 v_texCoord;
layout(location = 0) out vec4 fragColor0;

void main() {
    vec4 color = texture(u_image0, v_texCoord);
    float gray = dot(color.rgb, vec3(0.2126, 0.7152, 0.0722));
    fragColor0 = vec4(vec3(gray), color.a);
}
```

### Bildüberblendung

Überblenden Sie zwei Eingabebilder mit einem Float-Parameter als Mischfaktor:

```glsl
#version 300 es
precision highp float;

uniform sampler2D u_image0;
uniform sampler2D u_image1;
uniform float u_float0;  // mix factor [0.0 – 1.0]

in vec2 v_texCoord;
layout(location = 0) out vec4 fragColor0;

void main() {
    vec4 a = texture(u_image0, v_texCoord);
    vec4 b = texture(u_image1, v_texCoord);
    fragColor0 = mix(a, b, clamp(u_float0, 0.0, 1.0));
}
```

## Verwenden eines LLM zum Generieren von Shadern

Sie können jedes LLM (Claude, ChatGPT usw.) verwenden, um GLSL-Shader für sich schreiben zu lassen. Kopieren Sie den folgenden Prompt und geben Sie Ihren gewünschten Effekt ein:

````markdown
Schreibe einen GLSL-ES-3.00-Fragment-Shader für den GLSLShader-Node von ComfyUI.

**Effekt, den ich möchte:** [BESCHREIBEN SIE HIER IHREN GEWÜNSCHTEN EFFEKT]

**Anforderungen:**
- Muss mit `#version 300 es` beginnen
- Verwende `precision highp float;`
- Der Vertex-Shader stellt `in vec2 v_texCoord` bereit (0–1-UV-Koordinaten, Ursprung unten links)
- Ausgabe an `layout(location = 0) out vec4 fragColor0` (RGBA)
- Zusätzliche Ausgaben verfügbar: `fragColor1`, `fragColor2`, `fragColor3` an Locations 1–3

**Vorlage, der gefolgt werden soll (minimaler Passthrough-Shader – verwenden Sie exakt diese Struktur):**

```glsl
#version 300 es
precision highp float;

uniform sampler2D u_image0;

in vec2 v_texCoord;
layout(location = 0) out vec4 fragColor0;

void main() {
    fragColor0 = texture(u_image0, v_texCoord);
}
```

**Verfügbare Uniforms (deklarieren Sie nur, was Sie verwenden):**
- `uniform sampler2D u_image0;` bis `u_image4` – bis zu 5 Eingabebilder (RGBA-Float, lineare Filterung, Clamp-to-Edge)
- `uniform vec2 u_resolution;` – Breite und Höhe des **Ausgabe-Framebuffers** in Pixeln. Dies ist NICHT die Größe der Eingabetextur (sie können abweichen, wenn der Benutzer eine benutzerdefinierte Ausgabegröße festlegt). **Um in einer Eingabetextur um ein Pixel zu schreiten, verwenden Sie `vec2 texel = 1.0 / vec2(textureSize(u_image0, 0));` – verwenden Sie dafür NICHT `1.0 / u_resolution`.**
- `uniform float u_float0;` bis `u_float19;` – bis zu 20 benutzergesteuerte Float-Parameter
- `uniform int u_int0;` bis `u_int19;` – bis zu 20 benutzergesteuerte Ganzzahlparameter. Tipp: Int-Uniforms können vom Index-Ausgang eines **Custom Combo**-Nodes verdrahtet werden, sodass Benutzer aus einem Dropdown auswählen und der Shader den Index empfängt. Verwenden Sie dies zur Modusauswahl (z. B. Blend-Modus, Weichzeichnertyp). Definieren Sie benannte Konstanten für jede Option und verzweigen Sie darauf – vergleichen Sie NICHT mit rohen Ganzzahlliteralen. Zum Beispiel: `const int BLUR_GAUSSIAN = 0; const int BLUR_BOX = 1; ... if (u_int0 == BLUR_GAUSSIAN) { ... }`.
- `uniform bool u_bool0;` bis `u_bool9;` – bis zu 10 benutzergesteuerte boolesche Parameter (für Feature-Toggles verwenden)
- `uniform sampler2D u_curve0;` bis `u_curve3;` – bis zu 4 benutzereditierbare 1D-LUT-Kurven. Abtastung mit `texture(u_curve0, vec2(clamp(x, 0.0, 1.0), 0.5)).r`, wobei `x` 0–1 ist. Verwendung für Tonwertkurven, Neuzuordnung usw.
- `uniform int u_pass;` – aktueller Pass-Index (bei Verwendung von Multi-Pass)

**Multi-Pass-Rendering:**
- Fügen Sie `#pragma passes N` in der zweiten Zeile hinzu, um N Durchläufe zu aktivieren
- In Pass 0 ist `u_image0` die ursprüngliche Eingabe; in nachfolgenden Passes enthält es die Ausgabe des vorherigen Passes
- Verwenden Sie `u_pass`, um das Verhalten pro Pass zu variieren (z. B. horizontaler vs. vertikaler Weichzeichner)

**Wichtige Einschränkungen:**
- Nur GLSL ES 3.00 – kein `varying`/`attribute` aus GLSL 1.x, kein `gl_FragColor`
- Kein `#include`, keine externen Texturen, kein benutzerdefinierter Vertex-Shader
- Dokumentieren Sie jedes Uniform mit einem Kommentar, der seinen Zweck und den erwarteten Bereich angibt
````

### Beispiel für ausgefüllten Prompt

> **Effekt, den ich möchte:** Ein chromatischer Aberrationseffekt, der die RGB-Kanäle vom Bildzentrum nach außen aufspaltet. u_float0 steuert die Stärke des Versatzes (0 = kein Effekt, 10 = extrem stark). Der Versatz sollte mit dem Abstand vom Zentrum skalieren.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/de.md)

---
**Source fingerprint (SHA-256):** `ded589d5b0cb5413ecc42c7177e3076427ceac1d3218a20cfec6f2e005fe7e27`
