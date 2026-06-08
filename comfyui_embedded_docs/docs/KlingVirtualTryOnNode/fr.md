Nœud d'essayage virtuel Kling. Saisissez une image d'une personne et une image d'un vêtement pour essayer le vêtement sur la personne. Vous pouvez fusionner plusieurs images d'articles vestimentaires en une seule image sur fond blanc.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `human_image` | L'image de la personne sur laquelle essayer les vêtements | IMAGE | Oui | - |
| `cloth_image` | L'image du vêtement à essayer sur la personne | IMAGE | Oui | - |
| `model_name` | Le modèle d'essayage virtuel à utiliser (par défaut : "kolors-virtual-try-on-v1") | STRING | Oui | `"kolors-virtual-try-on-v1"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | L'image résultante montrant la personne avec le vêtement essayé | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/fr.md)

---
**Source fingerprint (SHA-256):** `bfd0da440d3ad85e15ce16851313f2e75421a8a3eb5e4c651350432955afc731`
