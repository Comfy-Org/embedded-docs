# Recraft V4 Stil erstellen

Dieser Node erstellt einen wiederverwendbaren Recraft V4-Stil aus 1 bis 10 Referenzbildern. Die zurückgegebene Stil-ID funktioniert mit jedem Recraft V4- und V4.1-Modell desselben Ausgabetyps (Raster oder Vektor) und kann in späteren Bildgenerierungsschritten wiederverwendet werden. Die Gesamtgröße aller Referenzbilder ist auf 10 MB begrenzt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell, für das der Stil erstellt wird. Standard und Pro teilen sich einen Stil-Pool: Rasterstile funktionieren mit jedem Recraft V4- und V4.1-Rastermodell, Vektorstile (*_vector) mit jedem V4- und V4.1-Vektormodell. | COMBO | Ja | "recraftv4_styles"<br>"recraftv4_styles_vector"<br>"recraftv4_styles_pro"<br>"recraftv4_styles_pro_vector" |
| `images` | Referenzbilder, die den Stil definieren. Ähnliche Referenzen schärfen die Übereinstimmung, abwechslungsreiche Referenzen erweitern sie. Erweiterbarer Slot: Verbinden Sie 1 bis 10 Bilder (`image_1` bis `image_10`). | IMAGE | Ja | 1 bis 10 Bilder |

### Hinweise

- Mindestens ein Referenzbild ist erforderlich; der Node löst einen Fehler aus, wenn keines bereitgestellt wird.
- Höchstens 10 Referenzbilder sind zulässig; der Node löst einen Fehler aus, wenn mehr bereitgestellt werden.
- Die gesamte kodierte Größe aller Referenzbilder darf 10 MB nicht überschreiten; der Node löst einen Fehler aus, wenn das Limit überschritten wird.
- Jedes Referenzbild wird auf höchstens 2048×2048 Pixel herunterskaliert und als WebP kodiert, bevor es an die Recraft API gesendet wird.
- Modelle, die auf `_vector` enden, erstellen Vektorstile; die anderen Optionen erstellen Rasterstile. Standard- und Pro-Modelle teilen sich innerhalb jedes Ausgabetyps dieselben Stil-Pools.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `style_id` | Eindeutige Kennung des erstellten Stils, verwendbar mit jedem Recraft V4- und V4.1-Modell desselben Ausgabetyps. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/de.md)

---
**Source fingerprint (SHA-256):** `7b907a975ed88dcca6bf1e0431ef7a9b561852ca7263a4f3298df980fe9431e5`
