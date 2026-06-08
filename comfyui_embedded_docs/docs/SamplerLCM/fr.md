Le nœud SamplerLCM fournit un échantillonneur LCM (Modèle de Cohérence Latente) avec des paramètres de bruit par étape réglables. Il permet de contrôler le bruit appliqué à chaque étape d'échantillonnage, offrant un réglage fin du processus d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `s_noise` | Multiplicateur de bruit par étape à la première étape. Une valeur de 1,0 correspond à l'échelle de bruit d'entraînement du modèle. (valeur par défaut : 1,0) | FLOAT | Oui | 0,0 à 64,0 (pas : 0,01) |
| `s_noise_end` | Multiplicateur de bruit par étape à la dernière étape. Définissez-le égal à `s_noise` pour une planification de bruit constante. (valeur par défaut : 1,0) | FLOAT | Oui | 0,0 à 64,0 (pas : 0,01) |
| `noise_clip_std` | Limite le bruit par étape à +/- N écarts types. Une valeur de 0 désactive la limitation. (valeur par défaut : 0,0) | FLOAT | Oui | 0,0 à 10,0 (pas : 0,01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `SAMPLER` | L'objet échantillonneur LCM configuré, prêt à être utilisé dans un workflow d'échantillonnage. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/fr.md)

---
**Source fingerprint (SHA-256):** `e6f9007f66625baeee8850018784187cf45117591c443f117c593eef547ada98`
