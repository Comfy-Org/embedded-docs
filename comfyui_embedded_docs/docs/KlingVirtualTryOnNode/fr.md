> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/fr.md)

Nœud d'essayage virtuel Kling. Saisissez une image d'une personne et une image d'un vêtement pour essayer le vêtement sur la personne. Vous pouvez fusionner plusieurs images d'articles vestimentaires en une seule image sur fond blanc.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `human_image` | IMAGE | Oui | - | L'image de la personne sur laquelle essayer les vêtements |
| `cloth_image` | IMAGE | Oui | - | L'image du vêtement à essayer sur la personne |
| `model_name` | STRING | Oui | `"kolors-virtual-try-on-v1"` | Le modèle d'essayage virtuel à utiliser (par défaut : "kolors-virtual-try-on-v1") |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | IMAGE | L'image résultante montrant la personne avec le vêtement essayé |

---
**Source fingerprint (SHA-256):** `bfd0da440d3ad85e15ce16851313f2e75421a8a3eb5e4c651350432955afc731`
