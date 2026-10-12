# GLSL Shader

הצומת **GLSL Shader** מאפשר לכתוב שיידרים מותאמים אישית מסוג fragment ב-**GLSL ES 3.00** (תואם WebGL 2.0) כדי לעבד תמונות ישירות על ה-GPU. ניתן ליצור אפקטים חזותיים כמו טשטושים, תיקון צבע, גרעיניות סרט, זוהר ועוד רבים - הכול במהירות GPU.

<Note>
הצומת GLSL Shader מסומן כעת כ-**ניסיוני**, כך שהצומת עשוי להתעדכן ולהתרחב בגרסאות עתידיות.
</Note>

## שיידר מינימלי

השיידר הפשוט ביותר האפשרי - העברה ישירה (passthrough) שמפיקה את תמונת הקלט ללא שינוי:

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
**למה GLSL ES 3.00?** שיידרים צריכים לפעול בשני סביבות: ה**דפדפן** (דרך WebGL 2.0, שתומך רק ב-GLSL ES 3.00) לתצוגה חיה ב-frontend של ComfyUI, וה**בקאנד של Python** (דרך OpenGL שולחני) כאשר תהליך העבודה מופעל. GLSL ES 3.00 הוא המכנה המשותף שעובד בשני המקומות.
</Note>

## Uniforms זמינים

ה-Uniforms האלה מוגדרים אוטומטית על ידי ComfyUI. אין צורך להצהיר על כולם - הצהר רק על אלה שבהם אתה משתמש.

### תמונות

| Uniform | תיאור | סוג |
| --- | --- | --- |
| `u_image0` – `u_image4` | תמונות קלט (עד 5). נדגמות באמצעות `texture(u_image0, v_texCoord)`. התמונות הן טקסטורות RGBA float עם סינון ליניארי ועטיפת clamp-to-edge. | `sampler2D` |

### מספרי float

| Uniform | תיאור | סוג |
| --- | --- | --- |
| `u_float0` – `u_float19` | עד 20 ערכי float הנשלטים על ידי המשתמש. ממופים מקבוצת הקלט **floats** בצומת. | `float` |

### מספרים שלמים

| Uniform | תיאור | סוג |
| --- | --- | --- |
| `u_int0` – `u_int19` | עד 20 ערכי מספרים שלמים הנשלטים על ידי המשתמש. ממופים מקבוצת הקלט **ints** בצומת. | `int` |

<Note>
**שימוש ב-Uniforms של int כרשימות נפתחות:** Uniforms מסוג int משתלבים היטב עם פלט האינדקס של הצומת **Custom Combo** - המשתמשים בוחרים אפשרות מרשימה נפתחת והשיידר מקבל את האינדקס של הפריט הנבחר.

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

### ערכים בוליאניים

| Uniform | תיאור | סוג |
| --- | --- | --- |
| `u_bool0` – `u_bool9` | עד 10 ערכים בוליאניים הנשלטים על ידי המשתמש. ממופים מקבוצת הקלט **bools** בצומת. | `bool` |

### עקומות (1D LUTs)

| Uniform | תיאור | סוג |
| --- | --- | --- |
| `u_curve0` – `u_curve3` | עד 4 עקומות LUT הניתנות לעריכה על ידי המשתמש מקבוצת הקלט **curves**. כל עקומה היא טבלת חיפוש חד-ממדית המאוחסנת כטקסטורה של שורה אחת. | `sampler2D` |

<Note>
**שימוש ב-Uniforms של עקומות:** עקומות מאפשרות למשתמשים לצייר גרפי מיפוי גוונים שרירותיים בממשק (למשל עבור ניגודיות, גמא, תיקון צבע לפי ערוץ, או כל מיפוי מחדש מותאם של `input → output`). דגום את העקומה תוך שימוש בערך הקלט שלך כקואורדינטת X - זכור להגביל אותו ל-`[0, 1]` תחילה:

```glsl
float applyCurve(sampler2D curve, float value) {
    return texture(curve, vec2(clamp(value, 0.0, 1.0), 0.5)).r;
}

// Usage: remap each RGB channel through a master curve
color.r = applyCurve(u_curve0, color.r);
color.g = applyCurve(u_curve0, color.g);
color.b = applyCurve(u_curve0, color.b);
```

שימושים נפוצים: עקומות RGB ראשיות, עקומות R/G/B לפי ערוץ, מיפויים מחדש מבוססי בהירות, גמא מותאמת, וכל אפקט שבו אתה רוצה שהמשתמש יעצב עקומת תגובה חזותית.
</Note>

### רזולוציה

| Uniform | תיאור | סוג |
| --- | --- | --- |
| `u_resolution` | מידות ה-framebuffer של **הפלט** בפיקסלים (`width, height`). זהו הגודל שאליו אתה כותב, והוא עשוי להיות שונה מהגודל של כל תמונת קלט כאשר `size_mode` הוא `"custom"`. | `vec2` |

<Note>
**חישוב גודל טקסל לדגימה:** אל תשתמש ב-`1.0 / u_resolution` כדי להתקדם בפיקסל אחד בטקסטורת קלט. `u_resolution` הוא הגודל של ה*פלט*, שעשוי שלא להתאים לגודל הקלט. במקום זאת השתמש ב-`textureSize()` על הטקסטורה שאתה דוגם ממנה בפועל:

```glsl
vec2 texel = 1.0 / vec2(textureSize(u_image0, 0));
```

השתמש ב-`u_resolution` רק כאשר אתה צריך את מידות ה-framebuffer של הפלט עצמן (למשל חישוב `gl_FragCoord.xy / u_resolution` כדי לקבל UV במרחב המסך).
</Note>

### ריבוי מעברים

| Uniform | תיאור | סוג |
| --- | --- | --- |
| `u_pass` | אינדקס המעבר הנוכחי (מתחיל מ-0). משמעותי רק כאשר משתמשים ב-`#pragma passes` - ראו [רינדור פינג-פונג רב-מעברי](#multi-pass-ping-pong-rendering) לפרטים. | `int` |

### פלט ה-Vertex Shader

| Varying | תיאור | סוג |
| --- | --- | --- |
| `v_texCoord` | קואורדינטות טקסטורה הנעות בין (0,0) בצד שמאל-תחתון ל-(1,1) בצד ימין-עליון. | `vec2` |

## פלטים מרובים (MRT)

הצומת מאפשר עד **4 פלטים בו-זמנית** באמצעות Multiple Render Targets. הצהר על פלטים נוספים עם locations מפורשים:

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

כל `fragColor` ממופה לפלט ה-`IMAGE` המתאים בצומת. ComfyUI מזהה אוטומטית באילו פלטים אתה משתמש - פלטים שאינם בשימוש יהיו שחורים.

## רינדור פינג-פונג רב-מעברי

אפקטים מסוימים (כמו טשטוש פריק) זקוקים למעברים מרובים על התמונה. השתמש בהנחיית `#pragma passes N` כדי לאפשר זאת:

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

### איך פינג-פונג עובד

1. **מעבר 0**: קורא מקלט `u_image0` המקורי, וכותב לטקסטורת פינג-פונג פנימית.
2. **מעבר 1–N**: קורא מ*פלט המעבר הקודם* דרך `u_image0` (הכריכה מוחלפת אוטומטית), וכותב לטקסטורת הפינג-פונג האחרת.
3. **מעבר סופי**: כותב ל-framebuffer הפלט בפועל (`fragColor0`).

<Note>
כאשר משתמשים בריבוי מעברים עם MRT (פלטים מרובים), רק הפלט הראשון (`fragColor0`) משתתף בפינג-פונג. המעבר הסופי כותב את כל הפלטים.
</Note>

## דוגמאות

### המרה לגווני אפור

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

### מיזוג תמונות

מזג שתי תמונות קלט תוך שימוש בפרמטר float כגורם המיזוג:

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

## שימוש ב-LLM ליצירת שיידרים

אתה יכול להשתמש בכל LLM (Claude, ChatGPT וכו') כדי שיכתוב עבורך שיידרים ב-GLSL. העתק את הפרומפט הבא ומלא את האפקט הרצוי:

````markdown
Write a GLSL ES 3.00 fragment shader for ComfyUI's GLSLShader node.

**Effect I want:** [DESCRIBE YOUR DESIRED EFFECT HERE]

**Requirements:**
- Must start with `#version 300 es`
- Use `precision highp float;`
- The vertex shader provides `in vec2 v_texCoord` (0–1 UV coordinates, bottom-left origin)
- Output to `layout(location = 0) out vec4 fragColor0` (RGBA)
- Additional outputs available: `fragColor1`, `fragColor2`, `fragColor3` at locations 1–3

**Template to follow (minimal passthrough shader - use this exact structure):**

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

**Available uniforms (declare only what you use):**
- `uniform sampler2D u_image0;` through `u_image4` - up to 5 input images (RGBA float, linear filtering, clamp-to-edge)
- `uniform vec2 u_resolution;` - **output framebuffer** width and height in pixels. This is NOT the input texture size (they can differ when the user sets a custom output size). **To step one pixel in an input texture, use `vec2 texel = 1.0 / vec2(textureSize(u_image0, 0));` - do NOT use `1.0 / u_resolution` for this.**
- `uniform float u_float0;` through `u_float19;` - up to 20 user-controlled float parameters
- `uniform int u_int0;` through `u_int19;` - up to 20 user-controlled integer parameters. Tip: int uniforms can be wired from a **Custom Combo** node's index output, so users select from a dropdown and the shader receives the index. Use this for mode selection (e.g. blend mode, blur type). Define named constants for each option and branch on those - do NOT compare against raw integer literals. For example: `const int BLUR_GAUSSIAN = 0; const int BLUR_BOX = 1; ... if (u_int0 == BLUR_GAUSSIAN) { ... }`.
- `uniform bool u_bool0;` through `u_bool9;` - up to 10 user-controlled boolean parameters (use for feature toggles)
- `uniform sampler2D u_curve0;` through `u_curve3;` - up to 4 user-editable 1D LUT curves. Sample with `texture(u_curve0, vec2(clamp(x, 0.0, 1.0), 0.5)).r` where `x` is 0–1. Use for tone curves, remapping, etc.
- `uniform int u_pass;` - current pass index (when using multi-pass)

**Multi-pass rendering:**
- Add `#pragma passes N` on the second line to enable N passes
- On pass 0, `u_image0` is the original input; on subsequent passes it contains the previous pass output
- Use `u_pass` to vary behavior per pass (e.g., horizontal vs. vertical blur)

**Important constraints:**
- GLSL ES 3.00 only - no GLSL 1.x `varying`/`attribute`, no `gl_FragColor`
- No `#include`, no external textures, no custom vertex shader
- Document each uniform with a comment showing its purpose and expected range
````

### דוגמה למילוי הפרומפט

> **האפקט שאני רוצה:** אפקט אברציה כרומטית שמפצל את ערוצי ה-RGB כלפי חוץ ממרכז התמונה. u_float0 שולט בעוצמת ההיסט (0 = ללא אפקט, 10 = חזק במיוחד). ההיסט צריך להתאים את עצמו לפי המרחק מהמרכז.

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/he.md)

---
**Source fingerprint (SHA-256):** `ded589d5b0cb5413ecc42c7177e3076427ceac1d3218a20cfec6f2e005fe7e27`
