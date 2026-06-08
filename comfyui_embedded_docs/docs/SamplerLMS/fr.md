Le nœud SamplerLMS crée un échantillonneur par moindres carrés moyens (LMS) destiné aux modèles de diffusion. Il génère un objet échantillonneur pouvant être utilisé dans le processus d'échantillonnage, vous permettant de contrôler l'ordre de l'algorithme LMS pour la stabilité numérique et la précision.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ordre` | Le paramètre d'ordre pour l'algorithme de l'échantillonneur LMS, qui contrôle la précision et la stabilité de la méthode numérique (valeur par défaut : 4) | INT | Oui | 1 à 100 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet échantillonneur LMS configuré pouvant être utilisé dans le pipeline d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/fr.md)

---
**Source fingerprint (SHA-256):** `0c045ef15890fe611dc0b9d455bafa313d28373a29c881a0c8bf5d80e69bc114`
