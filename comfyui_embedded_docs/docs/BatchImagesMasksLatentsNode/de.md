# BatchImagesMasksLatentsNode

Der Node Batch Images/Masks/Latents kombiniert mehrere Eingaben desselben Typs zu einem einzigen Batch. Er erkennt automatisch, ob es sich bei den Eingaben um Bilder, Masken oder latente Repräsentationen handelt, und verwendet die passende Batch-Methode. Dies ist nützlich, um mehrere Elemente für die Verarbeitung durch Nodes vorzubereiten, die gebatchte Eingaben akzeptieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `inputs` | Eine dynamische Liste von Eingaben, die zu einem Batch kombiniert werden sollen. Sie können zwischen 1 und 50 Elemente hinzufügen. Alle Elemente müssen denselben Typ haben (alle Bilder, alle Masken oder alle Latents). | IMAGE, MASK oder LATENT | Ja | 1 bis 50 Eingaben |

**Hinweis:** Der Node bestimmt den Datentyp (IMAGE, MASK oder LATENT) automatisch anhand des ersten Elements in der `inputs`-Liste. Alle nachfolgenden Elemente müssen diesem Typ entsprechen. Der Node schlägt fehl, wenn Sie versuchen, verschiedene Datentypen zu mischen.

**Zusätzliches Verhalten je nach Eingabetyp:**
- **Bilder**: Beim Batching von Bildern füllt der Node Bilder mit weniger Farbkanälen auf, um die maximale Kanalanzahl aller Eingaben zu erreichen (Auffüllwert ist 1.0). Außerdem skaliert er alle Bilder mit bilinearer Interpolation auf die Abmessungen des ersten Bildes.
- **Masken**: Beim Batching von Masken skaliert der Node alle Masken mit bilinearer Interpolation auf die Abmessungen der ersten Maske.
- **Latents**: Beim Batching von Latents formt der Node alle latenten Tensoren so um, dass sie den Abmessungen der Samples des ersten Latents entsprechen. Außerdem kombiniert er die `batch_index`-Werte jedes Latents und erweitert die Liste mit fortlaufenden Indizes, wenn einem Latent ein `batch_index` fehlt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Eine einzelne gebatchte Ausgabe. Der Datentyp entspricht dem Eingabetyp (gebatchtes IMAGE, gebatchtes MASK oder gebatchtes LATENT). | IMAGE, MASK oder LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesMasksLatentsNode/de.md)

---
**Source fingerprint (SHA-256):** `9f82b036c99577ebcda6de647c662def572ae1f01bd78dca1a0ab32f4698e09e`
