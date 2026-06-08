Ce nœud configure un style destiné à être utilisé avec l'API Recraft, en sélectionnant spécifiquement le style « digital_illustration ». Il permet de choisir un sous-style optionnel pour affiner davantage la direction artistique de l'image générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `sous-style` | Un sous-style optionnel pour spécifier un type particulier d'illustration numérique. S'il n'est pas sélectionné, le style de base « digital_illustration » est utilisé. | STRING | Non | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `recraft_style` | Un objet de style configuré contenant le style « digital_illustration » sélectionné et le sous-style optionnel, prêt à être transmis à d'autres nœuds de l'API Recraft. | STYLEV3 |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/fr.md)

---
**Source fingerprint (SHA-256):** `e52790a670839608ee1cb576e802a54d3bf2ca879ec288a24acd4ac7db27021a`
