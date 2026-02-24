> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/fr.md)

Ce nœud configure un style pour utilisation avec l'API Recraft, en sélectionnant spécifiquement le style "digital_illustration". Il vous permet de choisir un sous-style optionnel pour affiner davantage la direction artistique de l'image générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `sous-style` | STRING | Non | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` | Un sous-style optionnel pour spécifier un type particulier d'illustration numérique. Si non sélectionné, le style de base "digital_illustration" est utilisé. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Un objet de style configuré contenant le style "digital_illustration" sélectionné et le sous-style optionnel, prêt à être transmis à d'autres nœuds de l'API Recraft. |
