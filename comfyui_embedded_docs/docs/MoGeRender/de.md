# MoGe-Geometrie rendern

Dieser Node nimmt ein MOGE_GEOMETRY-Paket (erzeugt von einem MoGe-Node zur Tiefen-/Normalenschätzung) und rendert es in ein Standardbildformat. Sie können eine Tiefenkarte, eine farbige Tiefenkarte, eine Normalenmap oder eine Maske ausgeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Das Geometriedatenpaket von einem MoGe-Schätzungs-Node. | MOGE_GEOMETRY | Ja | N/A |
| `output` | Der Bildtyp, der aus den Geometriedaten gerendert werden soll. `depth` gibt eine Graustufen-Tiefenkarte aus, `depth_colored` gibt eine farbige Tiefenkarte aus, `normal_opengl` und `normal_directx` geben Normalenmaps aus, und `mask` gibt eine Maske aus. DirectX vs. OpenGL steuert die Konvention für den Grünkanal der Normalenmap. DirectX: Grün = -Y nach unten (Unreal). OpenGL: Grün = +Y nach oben (Blender, Substance, Unity, glTF). (Standard: "depth") | COMBO | Ja | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Hinweis:** Das Geometriepaket muss Daten enthalten, die zum gewählten `output`-Modus passen. Die Modi `depth` und `depth_colored` erfordern Tiefendaten im Paket. Die Modi `normal_opengl` und `normal_directx` erfordern Normalendaten oder Punktdaten, aus denen Normalen abgeleitet werden. Der Modus `mask` erfordert Maskendaten. Wenn die erforderlichen Daten fehlen, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Das gerenderte Bild als Batch von RGB-Tensoren. Der Inhalt hängt vom `output`-Modus ab: eine Graustufen-Tiefenkarte, eine farbige Tiefenkarte, eine Normalenmap oder eine in RGB konvertierte Maske. Die Batch-Größe der Ausgabe entspricht der Batch-Größe der Eingabegeometrie. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/de.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
