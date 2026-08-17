# SamplerLCM

Le nœud SamplerLCM fournit un échantillonneur LCM (Latent Consistency Model) avec des réglages de bruit par étape ajustables. Le paramètre `s_noise` agit comme un multiplicateur sur l'échelle de bruit d'entraînement du modèle, permettant un contrôle fin du bruit appliqué à chaque étape d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `s_noise` | Multiplicateur de bruit par étape à la première étape (1.0 = correspond à l'entraînement). Défaut : 1.0. | FLOAT | Oui | 0.0 à 64.0 (pas : 0.01) |
| `s_noise_end` | Multiplicateur de bruit par étape à la dernière étape. Réglez-le égal à `s_noise` pour un programme constant. Défaut : 1.0. | FLOAT | Oui | 0.0 à 64.0 (pas : 0.01) |
| `noise_clip_std` | Limite le bruit par étape à +/- N*std. 0 désactive. Défaut : 0.0. | FLOAT | Oui | 0.0 à 10.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `SAMPLER` | L'objet échantillonneur LCM configuré, prêt à être utilisé dans un flux de travail d'échantillonnage. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/fr.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
