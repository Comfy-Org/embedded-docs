# MergeSplat

Der Node „Merge Splats“ kombiniert mehrere Gaussian-Splat-Modelle zu einem einzelnen Splat, indem er ihre Daten aneinanderhängt. Dies ist nützlich, um mehrere Decodierungen desselben Latents, die mit unterschiedlichen Seeds erzeugt wurden, zusammenzuführen; dadurch kann die Oberfläche verdichtet und die Qualität bei der Erstellung von 3D-Meshes verbessert werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `splat0` | Erster Gaussian-Splat zum Zusammenführen | SPLAT | Ja | Mindestens 1 Splat erforderlich |
| `splat1` | Zweiter Gaussian-Splat zum Zusammenführen | SPLAT | Ja | Mindestens 1 Splat erforderlich |
| `splat2` | Zusätzlicher Gaussian-Splat zum Zusammenführen (optional) | SPLAT | Nein | Insgesamt bis zu 32 Splats |
| `splat3` | Zusätzlicher Gaussian-Splat zum Zusammenführen (optional) | SPLAT | Nein | Insgesamt bis zu 32 Splats |
| ... | Zusätzliche Splats (bis splat31) | SPLAT | Nein | Insgesamt bis zu 32 Splats |

**Hinweis:** Die Eingabeliste erweitert sich automatisch um neue Slots, wenn Sie Splats verbinden. Sie müssen mindestens einen Splat verbinden. Der Node akzeptiert mindestens 2 und maximal 32 Splats.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `splat` | Der zusammengeführte Gaussian-Splat, der alle Eingabe-Splats verkettet enthält | SPLAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeSplat/de.md)

---
**Source fingerprint (SHA-256):** `597671a3c37d1a4fb7b5a772396e08b7041b3fe8f04120891b1382d42e409d26`
