# VOIDSampler

## Aperçu

Le nœud VOIDSampler fournit une méthode d'échantillonnage DDIM spécialisée, conçue spécifiquement pour les modèles d'inpainting VOID. Il implémente le même processus de débruitage que celui utilisé lors de l'entraînement des modèles VOID, sans la mise à l'échelle du bruit que les KSamplers standard appliquent. Ce nœud est destiné à être utilisé avec les nœuds SamplerCustom ou SamplerCustomAdvanced, et doit être associé à RandomNoise ou VOIDWarpedNoiseSource.

## Entrées

Ce nœud n'a aucun paramètre d'entrée configurable. Il s'agit d'un échantillonneur autonome qui applique un algorithme d'échantillonnage DDIM fixe.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| *Aucune entrée* | Ce nœud n'accepte aucun paramètre d'entrée. | - | - | - |

Remarque : Les modèles VOID ont été entraînés avec le diffusers CogVideoXDDIMScheduler, qui opère dans l'espace alpha où l'écart type d'entrée est d'environ 1. Le KSampler standard applique une mise à l'échelle du bruit qui multiplie par environ 4500x, ce qui est incompatible avec cet entraînement. Le VOIDSampler ignore cette mise à l'échelle et implémente directement la règle de mise à jour DDIM en utilisant la conversion sigma-alpha.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `SAMPLER` | Un objet échantillonneur implémentant l'algorithme VOID DDIM, prêt à être connecté aux nœuds SamplerCustom ou SamplerCustomAdvanced. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/fr.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
