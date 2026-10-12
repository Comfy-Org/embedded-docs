# RecraftStyleV3DigitalIllustration

Dieser Node konfiguriert einen Stil für die Verwendung mit der Recraft API und wählt dabei speziell den Stil „digital_illustration“ aus. Er ermöglicht die Auswahl eines optionalen Substils, um die künstlerische Ausrichtung des generierten Bildes weiter zu verfeinern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `substyle` | Ein optionaler Substil, um einen bestimmten Typ digitaler Illustration festzulegen. Wenn nicht ausgewählt, wird der Basisstil „digital_illustration“ verwendet. | STRING | Nein | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `recraft_style` | Ein konfiguriertes Stilobjekt, das den ausgewählten Stil „digital_illustration“ und den optionalen Substil enthält und bereit ist, an andere Recraft-API-Nodes übergeben zu werden. | STYLEV3 |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/de.md)

---
**Source fingerprint (SHA-256):** `b6901d81bc11c3226d847ed61386b9bcf4ece90f6a95b6ad9888f102ef355594`
