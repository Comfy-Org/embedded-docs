# sync.so Sprechendes Bild

Animieren Sie ein Standporträt zu einem sprechenden Video, das durch Sprachaudio gesteuert wird, mithilfe des sync-3-Modells von sync.so. Die Ausgabedauer entspricht der Audiodauer, und die Kosten skalieren mit der Ausgabedauer.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Ein einzelnes Bild mit einem klar sichtbaren Gesicht, bis zu 4K (4096x2160). | IMAGE | Ja | Genau ein Bild erforderlich |
| `audio` | Sprachaudio, das das sprechende Video steuert; die Ausgabedauer entspricht ihm. Verknüpfen Sie hier einen beliebigen TTS-Node, um die Animation aus Text zu steuern. | AUDIO | Ja | Maximale Dauer: 600 Sekunden |
| `prompt` | Optionale Anleitung, wie das Porträt zum Leben erweckt wird, z. B. 'Lassen Sie die Person lächeln und in die Kamera schauen'. Leer lassen für natürliche Sprechbewegung. (Standard: "") | STRING | Nein | Mehrzeiliger Text |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Nein | 0 bis 2147483647 |
| `model` | Generierungsmodell von sync.so. Bildeingabe ist exklusiv für sync-3. | COMBO | Ja | `"sync-3"` |
| `speaker_selection` | Welches Gesicht animiert werden soll, wenn mehrere Personen sichtbar sind. `default`: das Modell entscheiden lassen. `coordinates`: das Gesicht am Pixel (`speaker_x`, `speaker_y`) im Bild anvisieren. Die automatische Erkennung wird für Bilder nicht unterstützt. (Standard: "default") | COMBO | Nein | `"default"`<br>`"coordinates"` |
| `speaker_x` | X-Pixelkoordinate des Gesichts der sprechenden Person. Wird nur verwendet, wenn `speaker_selection` auf `"coordinates"` gesetzt ist. (Standard: 0) | INT | Nein | 0 bis 4096 |
| `speaker_y` | Y-Pixelkoordinate des Gesichts der sprechenden Person. Wird nur verwendet, wenn `speaker_selection` auf `"coordinates"` gesetzt ist. (Standard: 0) | INT | Nein | 0 bis 4096 |
| `auto_downscale` | Das Bild automatisch herunterskalieren, wenn es das 4K-Eingabelimit (4096x2160) überschreitet; die Sprecherkoordinaten werden entsprechend skaliert. Wenn deaktiviert, löst ein übergroßes Bild stattdessen einen Fehler aus. (Standard: True) | BOOLEAN | Nein | True<br>False |

**Hinweis:** Die Parameter `speaker_x` und `speaker_y` werden nur verwendet, wenn `speaker_selection` auf `"coordinates"` gesetzt ist. Wenn `auto_downscale` aktiviert ist, werden die Sprecherkoordinaten automatisch an die Abmessungen des herunterskalierten Bildes angepasst.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte sprechende Video mit dem animierten Porträt, synchronisiert mit dem Eingabeaudio. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncTalkingImageNode/de.md)

---
**Source fingerprint (SHA-256):** `21f722cdcc5ff017949887ed2252854feebb9b913034dc6a6c3ce196ad089468`
