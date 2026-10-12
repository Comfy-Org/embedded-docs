# HitPawGeneralImageEnhance

Dieser Node verbessert niedrig aufgelöste Bilder, indem er sie auf Superauflösung hochskaliert und dabei Artefakte und Rauschen entfernt. Er sendet das Bild zur Verarbeitung an eine externe API und kann die Eingabegröße automatisch anpassen, um innerhalb des zulässigen Ausgabelimits zu bleiben. Die maximal zulässige Ausgabegröße beträgt 32 Megapixel.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das zu verwendende Verbesserungsmodell. Das Modell `generative_portrait` ist für Porträts optimiert, während `generative` ein Allzweckmodell ist. | COMBO | Ja | `"generative_portrait"`<br>`"generative"` |
| `image` | Das zu verbessernde Eingabebild. | IMAGE | Ja | - |
| `upscale_factor` | Der Faktor, um den die Abmessungen des Bildes hochskaliert werden. Ein Faktor von 1 bedeutet keine Hochskalierung, 2 verdoppelt die Abmessungen und 4 vervierfacht sie. | COMBO | Ja | `1`<br>`2`<br>`4` |
| `auto_downscale` | Das Eingabebild automatisch herunterskalieren, wenn die Ausgabe das Limit überschreiten würde. (Standard: `False`) | BOOLEAN | Nein | - |

**Hinweis:** Der Node löst einen Fehler aus, wenn die berechnete Ausgabegröße (Eingabebreite × upscale_factor × Eingabehöhe × upscale_factor) 32.000.000 Pixel (32 MP) überschreitet und `auto_downscale` deaktiviert ist. Wenn `auto_downscale` aktiviert ist, reduziert der Node automatisch die Größe des Eingabebilds oder den Hochskalierungsfaktor (oder beides), damit die Ausgabe in das 32-MP-Limit passt. Die ausgewählten Werte für `model` und `upscale_factor` werden zu dem Modellnamen kombiniert, der an den Dienst gesendet wird.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das verbesserte und hochskalierte Ausgabebild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/de.md)

---
**Source fingerprint (SHA-256):** `eb9adc1ac94c5fb943e3dd8f6617b21c5d3203f0d9ddb93ba1c9d4b4e63bd421`
