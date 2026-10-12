# LTXV Generierte Keyframes trennen

## Überblick

Der Node LTXV Separate Generated Keyframes trennt die durch LTXV Add Generated Keyframes hinzugefügten generierten Keyframes wieder aus einem gesampelten Latent heraus und entfernt sie aus dem Conditioning. Verwenden Sie ihn, bevor Sie das Video-Latent räumlich hochskalieren. Führen Sie nicht zuerst LTXV Crop Guides aus — dieser behandelt generierte Keyframes als entbehrliche Guides und verwirft sie.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Positives Conditioning, das die Metadaten der generierten Keyframes enthält. Die Metadaten werden bei der Ausgabe daraus entfernt. | CONDITIONING | Ja | N/A |
| `negative` | Negatives Conditioning, das die Metadaten der generierten Keyframes enthält. Die Metadaten werden bei der Ausgabe daraus entfernt. | CONDITIONING | Ja | N/A |
| `latent` | Video-Latent, das die generierten Keyframes enthält. Die Keyframes werden bei der Ausgabe daraus entfernt. | LATENT | Ja | N/A |
| `keyframes_to_batch` | Die Keyframes als Batch aus Einzelbild-Latents zurückgeben. Ausschalten, um sie als ein Multi-Frame-Latent zu erhalten, was der Latent-Upsampler und ein späteres Add Generated Keyframes erwarten. | BOOLEAN | Nein | default: False |

### Hinweise zu Eingaben

- `positive` muss Metadaten für generierte Keyframes enthalten, andernfalls löst der Node einen Fehler aus und weist darauf hin, sie zuerst mit LTXV Add Generated Keyframes hinzuzufügen.
- `latent` muss ein einfaches Video-Latent sein (ein 5D-Tensor). Wenn Video- und Audio-Latents noch kombiniert sind, trennen Sie sie zuerst mit Separate AV Latent.
- Die beim Hinzufügen der Keyframes aufgezeichnete Anzahl von Token pro Latent-Frame muss mit den Token pro Frame des übergebenen `latent` übereinstimmen. Wenn das Latent nach dem Hinzufügen der Keyframes neu skaliert wurde, passen sie nicht mehr zusammen und der Node löst einen Fehler aus — trennen Sie sie, bevor Sie das Latent hochskalieren.
- Der aufgezeichnete Keyframe-Frame-Bereich muss in das übergebene `latent` passen, andernfalls löst der Node einen Fehler aus, dass die Keyframes gegen ein anderes Latent aufgezeichnet wurden.
- Der aufgezeichnete Guide-Attention-Eintragsindex muss noch im Conditioning vorhanden sein. Wenn das Conditioning nach dem Hinzufügen der Keyframes neu aufgebaut wurde, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Positives Conditioning mit entfernten Metadaten der generierten Keyframes. | CONDITIONING |
| `negative` | Negatives Conditioning mit entfernten Metadaten der generierten Keyframes. | CONDITIONING |
| `latent` | Video-Latent mit entfernten generierten Keyframes. | LATENT |
| `keyframes` | Die abgetrennten Keyframes, gekennzeichnet mit generated_keyframe_indices und generated_keyframe_num_frames. Übergeben Sie diese an ein späteres Add Generated Keyframes, um neue Slots zu initialisieren, oder an Generated Keyframes To Guides, um sie als eingefrorene Bild-Guides zu fixieren (Indizes werden neu zugeordnet, wenn sich die Canvas-Länge geändert hat). | LATENT |

## Hinweise

- Der Parameter `keyframes_to_batch` bestimmt, ob die Keyframes als Batch aus Einzelbild-Latents oder als ein Multi-Frame-Latent zurückgegeben werden.
- Der Node stellt sicher, dass die generierten Keyframes aus dem Conditioning und dem Latent entfernt werden, bevor eine weitere Verarbeitung erfolgt.
- Die Ausgabe `keyframes` kann verwendet werden, um neue Slots für generierte Keyframes zu initialisieren oder sie als eingefrorene Bild-Guides zu fixieren.
- Der Node löst einen `ValueError` aus, wenn das Latent keine generierten Keyframes enthält oder wenn die Keyframes nicht dem erwarteten Format entsprechen.
- Der Node geht davon aus, dass die generierten Keyframes mit dem Node LTXV Add Generated Keyframes hinzugefügt wurden und dass sie mit dem aktuellen Latent kompatibel sind.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/de.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
