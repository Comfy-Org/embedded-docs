# LTX Video Reframe

Rahmt ein Video auf eine neue Auflösung und ein neues Seitenverhältnis um. Der Bereich außerhalb des ursprünglichen Videos wird passend zu dessen Inhalt generiert, sodass ein Hochformat-Clip zu einem Querformat-Clip werden kann oder umgekehrt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Video, das neu gerahmt werden soll, bis zu 60 Sekunden und 1800 Frames, wobei jede Seite zwischen 64 und 4096 Pixel groß ist. | VIDEO | Ja | - |
| `resolution` | Ausgabegröße und Seitenverhältnis, bei 720p oder 1080p. Standard: `"(1080p) 1080x1920 (9:16)"`. | COMBO | Ja | `"(720p) 720x720 (1:1)"`<br>`"(720p) 720x900 (4:5)"`<br>`"(720p) 900x720 (5:4)"`<br>`"(720p) 720x1280 (9:16)"`<br>`"(720p) 1280x720 (16:9)"`<br>`"(1080p) 1080x1080 (1:1)"`<br>`"(1080p) 1080x1350 (4:5)"`<br>`"(1080p) 1350x1080 (5:4)"`<br>`"(1080p) 1080x1920 (9:16)"`<br>`"(1080p) 1920x1080 (16:9)"` |
| `placement` | Wo sich das Originalvideo im neuen Frame befindet. Das Video füllt immer eine Seite des Frames aus, sodass ein Anker es nur entlang der anderen Seite verschiebt. Standard: `"center"`. | DYNAMIC_COMBO | Ja | `"center"`<br>`"top"`<br>`"bottom"`<br>`"left"`<br>`"right"`<br>`"custom"` |
| `seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Nein | 0 bis 4294967295 |

### Eingaben für Platzierung „custom“

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `x` | Linke Kante des Videos als Bruchteil der Ausgabebreite. Standard: 0.25. | FLOAT | Nein | 0.0 bis 0.99 (Schritt: 0.01) |
| `y` | Obere Kante des Videos als Bruchteil der Ausgabebreite. Standard: 0.25. | FLOAT | Nein | 0.0 bis 0.99 (Schritt: 0.01) |
| `width` | Breite des Videos als Bruchteil der Ausgabebreite; die Höhe folgt dem Seitenverhältnis des Videos. Das Video muss innerhalb des Frames bleiben und kann höchstens um das 2-Fache vergrößert werden. Standard: 0.5. | FLOAT | Nein | 0.01 bis 1.0 (Schritt: 0.01) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das neu gerahmte Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoReframe/de.md)

---
**Source fingerprint (SHA-256):** `85fcce4a8054fa8faf0085a55510ee09bce89afd1cf9f19d6ea45105549f2656`
