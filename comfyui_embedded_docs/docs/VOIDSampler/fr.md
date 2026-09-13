# VOIDSampler

VOIDSampler est un échantillonneur DDIM spécialisé conçu pour les modèles d’inpainting VOID. Il reproduit exactement le processus de débruitage avec lequel VOID a été entraîné, en ignorant la mise à l’échelle du bruit appliquée par les KSamplers standards. Utilisez ce nœud avec SamplerCustom ou SamplerCustomAdvanced, associé à RandomNoise ou VOIDWarpedNoiseSource.

## Entrées

Ce nœud ne possède aucun paramètre d’entrée configurable. Il s’agit d’un échantillonneur autonome qui applique un algorithme d’échantillonnage DDIM fixe.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| *Aucune entrée* | Ce nœud n’accepte aucun paramètre d’entrée. | - | - | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `SAMPLER` | Un objet échantillonneur implémentant l’algorithme VOID DDIM, prêt à être connecté aux nœuds SamplerCustom ou SamplerCustomAdvanced. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/fr.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
