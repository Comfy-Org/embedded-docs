# SamplerLMS

Le nœud SamplerLMS crée un échantillonneur LMS (Least Mean Squares) destiné aux modèles de diffusion. Il génère un objet échantillonneur utilisable dans le processus d'échantillonnage, vous permettant de contrôler l'ordre de l'algorithme LMS pour la stabilité numérique et la précision.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ordre` | Le paramètre d'ordre pour l'algorithme de l'échantillonneur LMS, qui contrôle la précision et la stabilité de la méthode numérique (défaut : 4). Ce paramètre est affiché dans la section avancée de l'interface du nœud. | INT | Oui | 1 à 100 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet échantillonneur LMS configuré pouvant être utilisé dans le pipeline d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/fr.md)

---
**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`
