# GLSLShader

Il nodo **GLSL Shader** ti consente di scrivere fragment shader personalizzati in **GLSL ES 3.00** (compatibile con WebGL 2.0) per elaborare immagini direttamente sulla GPU. Puoi creare effetti immagine come sfocature, color grading, grana cinematografica, glow e molto altro - il tutto alla velocità della GPU.

<Note>
Il nodo GLSL Shader è attualmente contrassegnato come **sperimentale**, quindi il nodo potrebbe essere aggiornato ed esteso in versioni future.
</Note>

## Shader minimale

Lo shader più semplice possibile: un passthrough che restituisce l'immagine di input invariata:

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
**Perché GLSL ES 3.00?** Gli shader devono essere eseguiti in due ambienti: il **browser** (tramite WebGL 2.0, che supporta solo GLSL ES 3.00) per l'anteprima live nel frontend di ComfyUI, e il **backend Python** (tramite OpenGL desktop) quando il workflow viene eseguito. GLSL ES 3.00 è il denominatore comune che funziona in entrambi i contesti.
</Note>

## Uniform disponibili

Questi uniform vengono impostati automaticamente da ComfyUI. Non è necessario dichiararli tutti: dichiara solo quelli che usi.

### Immagini

| Uniform | Descrizione | Tipo |
| --- | --- | --- |
| `u_image0` – `u_image4` | Immagini di input (fino a 5). Campionate con `texture(u_image0, v_texCoord)`. Le immagini sono texture RGBA float con filtraggio lineare e wrapping clamp-to-edge. | `sampler2D` |

### Float

| Uniform | Descrizione | Tipo |
| --- | --- | --- |
| `u_float0` – `u_float19` | Fino a 20 valori float controllati dall'utente. Mappati dal gruppo di input **floats** sul nodo. | `float` |

### Interi

| Uniform | Descrizione | Tipo |
| --- | --- | --- |
| `u_int0` – `u_int19` | Fino a 20 valori interi controllati dall'utente. Mappati dal gruppo di input **ints** sul nodo. | `int` |

<Note>
**Usare uniform int come menu a tendina:** Gli uniform int si abbinano bene all'output index del nodo **Custom Combo**: gli utenti scelgono un'opzione da un menu a tendina e lo shader riceve l'indice dell'elemento selezionato.

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

### Booleani

| Uniform | Descrizione | Tipo |
| --- | --- | --- |
| `u_bool0` – `u_bool9` | Fino a 10 valori booleani controllati dall'utente. Mappati dal gruppo di input **bools** sul nodo. | `bool` |

### Curve (LUT 1D)

| Uniform | Descrizione | Tipo |
| --- | --- | --- |
| `u_curve0` – `u_curve3` | Fino a 4 LUT di curve modificabili dall'utente dal gruppo di input **curves**. Ogni curva è una tabella di lookup 1D memorizzata come texture a riga singola. | `sampler2D` |

<Note>
**Usare gli uniform delle curve:** Le curve consentono agli utenti di disegnare grafici arbitrari di tone mapping nell'interfaccia (ad es. per contrasto, gamma, color grading per canale o qualsiasi rimappatura personalizzata `input → output`). Campiona la curva usando il valore di input come coordinata X - ricorda di limitarlo prima a `[0, 1]`:

```glsl
float applyCurve(sampler2D curve, float value) {
    return texture(curve, vec2(clamp(value, 0.0, 1.0), 0.5)).r;
}

// Usage: remap each RGB channel through a master curve
color.r = applyCurve(u_curve0, color.r);
color.g = applyCurve(u_curve0, color.g);
color.b = applyCurve(u_curve0, color.b);
```

Usi comuni: curve RGB master, curve R/G/B per canale, rimappature basate sulla luminanza, gamma personalizzata e qualsiasi effetto in cui vuoi che l'utente modelli visivamente una curva di risposta.
</Note>

### Risoluzione

| Uniform | Descrizione | Tipo |
| --- | --- | --- |
| `u_resolution` | Dimensioni in pixel del framebuffer di **output** (`width, height`). Questa è la dimensione in cui stai scrivendo, che può differire dalla dimensione di qualsiasi immagine di input quando `size_mode` è `"custom"`. | `vec2` |

<Note>
**Calcolo della dimensione del texel per il campionamento:** Non usare `1.0 / u_resolution` per avanzare di un pixel in una texture di input. `u_resolution` è la dimensione di *output*, che potrebbe non corrispondere alla dimensione dell'input. Usa invece `textureSize()` sulla texture effettiva che stai campionando:

```glsl
vec2 texel = 1.0 / vec2(textureSize(u_image0, 0));
```

Usa `u_resolution` solo quando hai bisogno delle dimensioni stesse del framebuffer di output (ad es. per calcolare `gl_FragCoord.xy / u_resolution` per ottenere UV in screen-space).
</Note>

### Multi-Pass

| Uniform | Descrizione | Tipo |
| --- | --- | --- |
| `u_pass` | Indice del pass corrente (basato su 0). Significativo solo quando si usa `#pragma passes` - vedi [Rendering ping-pong multi-pass](#rendering-ping-pong-multi-pass) per i dettagli. | `int` |

### Output del vertex shader

| Varying | Descrizione | Tipo |
| --- | --- | --- |
| `v_texCoord` | Coordinate texture che vanno da (0,0) in basso a sinistra a (1,1) in alto a destra. | `vec2` |

## Output multipli (MRT)

Il nodo supporta fino a **4 output simultanei** usando Multiple Render Targets. Dichiara output aggiuntivi con location esplicite:

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

Ogni `fragColor` corrisponde all'output `IMAGE` corrispondente sul nodo. ComfyUI rileva automaticamente quali output usi - gli output inutilizzati saranno neri.

## Rendering ping-pong multi-pass

Alcuni effetti (come il blur separabile) richiedono più passaggi sull'immagine. Usa la direttiva `#pragma passes N` per abilitarlo:

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

### Come funziona il ping-pong

1. **Pass 0**: legge dall'input originale `u_image0`, scrive su una texture ping-pong interna.
2. **Pass 1–N**: legge dall'*output del pass precedente* tramite `u_image0` (il binding viene scambiato automaticamente), scrive sull'altra texture ping-pong.
3. **Pass finale**: scrive sul framebuffer di output effettivo (`fragColor0`).

<Note>
Quando si usa multi-pass con MRT (output multipli), solo il primo output (`fragColor0`) partecipa al ping-pong. Il pass finale scrive tutti gli output.
</Note>

## Esempi

### Conversione in scala di grigi

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

### Blending di immagini

Combina due immagini di input usando un parametro float come fattore di mix:

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

## Usare un LLM per generare shader

Puoi usare qualsiasi LLM (Claude, ChatGPT, ecc.) per scrivere shader GLSL al posto tuo. Copia il seguente prompt e inserisci l'effetto desiderato:

````markdown
Scrivi un fragment shader GLSL ES 3.00 per il nodo GLSLShader di ComfyUI.

**Effetto che voglio:** [DESCRIVI QUI L'EFFETTO DESIDERATO]

**Requisiti:**
- Deve iniziare con `#version 300 es`
- Usa `precision highp float;`
- Il vertex shader fornisce `in vec2 v_texCoord` (coordinate UV 0–1, origine in basso a sinistra)
- Output su `layout(location = 0) out vec4 fragColor0` (RGBA)
- Output aggiuntivi disponibili: `fragColor1`, `fragColor2`, `fragColor3` alle location 1–3

**Template da seguire (shader minimale di passthrough - usa esattamente questa struttura):**

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

**Uniform disponibili (dichiara solo quelli che usi):**
- `uniform sampler2D u_image0;` fino a `u_image4` - fino a 5 immagini di input (RGBA float, filtraggio lineare, clamp-to-edge)
- `uniform vec2 u_resolution;` - larghezza e altezza in pixel del **framebuffer di output**. Questa NON è la dimensione della texture di input (possono differire quando l'utente imposta una dimensione di output personalizzata). **Per avanzare di un pixel in una texture di input, usa `vec2 texel = 1.0 / vec2(textureSize(u_image0, 0));` - NON usare `1.0 / u_resolution` per questo.**
- `uniform float u_float0;` fino a `u_float19;` - fino a 20 parametri float controllati dall'utente
- `uniform int u_int0;` fino a `u_int19;` - fino a 20 parametri interi controllati dall'utente. Suggerimento: gli uniform int possono essere collegati dall'output index di un nodo **Custom Combo**, così gli utenti selezionano da un menu a tendina e lo shader riceve l'indice. Usalo per la selezione della modalità (ad es. modalità di blend, tipo di blur). Definisci costanti con nome per ogni opzione e fai branching su quelle - NON confrontare con letterali interi grezzi. Per esempio: `const int BLUR_GAUSSIAN = 0; const int BLUR_BOX = 1; ... if (u_int0 == BLUR_GAUSSIAN) { ... }`.
- `uniform bool u_bool0;` fino a `u_bool9;` - fino a 10 parametri booleani controllati dall'utente (usa per interruttori di funzionalità)
- `uniform sampler2D u_curve0;` fino a `u_curve3;` - fino a 4 curve LUT 1D modificabili dall'utente. Campiona con `texture(u_curve0, vec2(clamp(x, 0.0, 1.0), 0.5)).r` dove `x` è 0–1. Usa per curve tonali, rimappatura, ecc.
- `uniform int u_pass;` - indice del pass corrente (quando si usa multi-pass)

**Rendering multi-pass:**
- Aggiungi `#pragma passes N` sulla seconda riga per abilitare N pass
- Al pass 0, `u_image0` è l'input originale; nei pass successivi contiene l'output del pass precedente
- Usa `u_pass` per variare il comportamento per pass (ad es. blur orizzontale vs. verticale)

**Vincoli importanti:**
- Solo GLSL ES 3.00 - niente `varying`/`attribute` di GLSL 1.x, niente `gl_FragColor`
- Niente `#include`, niente texture esterne, niente vertex shader personalizzato
- Documenta ogni uniform con un commento che ne mostri lo scopo e l'intervallo previsto
````

### Esempio di compilazione del prompt

> **Effetto che voglio:** Un effetto di aberrazione cromatica che separa i canali RGB verso l'esterno dal centro dell'immagine. u_float0 controlla la forza dell'offset (0 = nessun effetto, 10 = estremamente forte). L'offset dovrebbe scalare con la distanza dal centro.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/it.md)

---
**Source fingerprint (SHA-256):** `ded589d5b0cb5413ecc42c7177e3076427ceac1d3218a20cfec6f2e005fe7e27`
