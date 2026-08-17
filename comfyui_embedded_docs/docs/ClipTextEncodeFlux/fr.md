# CLIPTextEncodeFlux

`CLIPTextEncodeFlux` est un nœud d'encodage de texte conçu pour l'architecture Flux. Il traite deux entrées de texte distinctes via différents encodeurs—CLIP-L et T5XXL—et les combine avec une échelle de guidage pour produire une sortie de conditionnement unifiée pour la génération d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Un modèle CLIP prenant en charge l'architecture Flux, incluant les encodeurs CLIP-L et T5XXL. | CLIP | Oui | - |
| `clip_l` | Entrée de texte traitée par l'encodeur CLIP-L. Convient aux descriptions concises par mots-clés, telles que le style ou le thème. Prend en charge la saisie multiligne et les invites dynamiques. | STRING | Oui | - |
| `t5xxl` | Entrée de texte traitée par l'encodeur T5XXL. Convient aux descriptions détaillées en langage naturel, exprimant des scènes et des détails complexes. Prend en charge la saisie multiligne et les invites dynamiques. | STRING | Oui | - |
| `guidance` | Contrôle l'influence des conditions de texte sur le processus de génération. Des valeurs plus élevées signifient une adhésion plus stricte au texte. Défaut : 3.5. | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Contient les plongements combinés des deux encodeurs et la valeur de guidage, utilisés pour la génération d'images conditionnelle. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/fr.md)

---
**Source fingerprint (SHA-256):** `022928fa6917102f5dc599364df9541b2451b42eb36a11813931b5fd71990b74`
