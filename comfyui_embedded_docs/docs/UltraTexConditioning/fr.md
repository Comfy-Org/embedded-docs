# UltraTex Conditioning

Conditionne FLUX.2 Klein 9B avec le LoRA UltraTex pour peindre l'apparence d'une image de référence sur un maillage, sous forme d'une image par vue. Rendez les vues avec Render Mesh en mode `world normal`, à partir d'un Create Camera Orbit de 4, plus les vues du dessus et du dessous, puis effectuez le bake du résultat avec Bake Texture From Views.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditioning` | Conditionnement textuel. UltraTex a été entraîné avec une invite vide. | CONDITIONING | Oui | - |
| `vae` | VAE utilisé pour encoder les normales, les vues et la référence. | VAE | Oui | - |
| `normals` | Images Render Mesh en mode `world normal` : les 6 vues canoniques, ou les 4 vues latérales. | IMAGE | Oui | - |
| `masks` | Masques Render Mesh des mêmes vues, un par vue. | MASK | Oui | - |
| `reference` | L'objet tel qu'il doit apparaître, vu depuis le côté de la caméra avant. | IMAGE | Oui | - |
| `reference_mask` | Masque de l'objet de la référence, blanc pour l'objet. Par défaut : entièrement blanc. | MASK | Non | - |
| `extra_views` | Références supplémentaires : l'objet vu depuis les autres vues, chacune liée à sa vue comme la référence est liée à la vue avant. Par défaut : `"off"`. | DYNAMIC_COMBO | Oui | `"off"`<br>`"on"` |

### Entrées des vues supplémentaires "on"

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `right` | L'objet vu depuis la vue de droite. | IMAGE | Non | - |
| `back` | L'objet vu depuis la vue arrière. | IMAGE | Non | - |
| `left` | L'objet vu depuis la vue de gauche. | IMAGE | Non | - |
| `top` | L'objet vu depuis la vue du dessus. | IMAGE | Non | - |
| `bottom` | L'objet vu depuis la vue du dessous. | IMAGE | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | Conditionnement transportant la grille de vues, les latents de référence et les masques de jetons dont UltraTex a besoin. | CONDITIONING |

Remarque : `normals` doit contenir soit les 6 vues canoniques (Create Camera Orbit avec `count` 4 et `poles` réglé sur dessus et dessous), soit les 4 vues latérales, et `masks` doit correspondre à son nombre de vues.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UltraTexConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `5b05f5151d4c12394ef893db69538adaef86e9cbdbb118a37c20919758520b6f`
