# CLIPTextEncodeFlux

Voici la traduction en français de la documentation du nœud `CLIPTextEncodeFlux`, en respectant vos règles :

`CLIPTextEncodeFlux` est un nœud d'encodage de texte avancé conçu pour l'architecture Flux. Il traite deux entrées de texte distinctes via différents encodeurs — CLIP-L et T5XXL — et les combine avec une échelle de guidage pour produire un conditionnement unifié destiné à la génération d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Un modèle CLIP prenant en charge l'architecture Flux, incluant les encodeurs CLIP-L et T5XXL. | CLIP | Oui | - |
| `clip_l` | Texte d'entrée traité par l'encodeur CLIP-L. Adapté aux descriptions concises par mots-clés, comme le style ou le thème. Prend en charge les entrées multilignes et les invites dynamiques. | STRING | Oui | - |
| `t5xxl` | Texte d'entrée traité par l'encodeur T5XXL. Adapté aux descriptions détaillées en langage naturel, exprimant des scènes et des détails complexes. Prend en charge les entrées multilignes et les invites dynamiques. | STRING | Oui | - |
| `guidance` | Contrôle l'influence des conditions textuelles sur le processus de génération. Des valeurs plus élevées signifient une adhérence plus stricte au texte. Valeur par défaut : 3.5. | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Contient les embeddings fusionnés des deux encodeurs et le paramètre de guidage, utilisés pour la génération conditionnelle d'images. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/fr.md)

---
**Source fingerprint (SHA-256):** `f168610123410a44f9c5c5c18773603bd47bc7b44b21e65910a6026f86d7eb04`
