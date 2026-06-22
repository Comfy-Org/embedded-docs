# FreeU

Voici la traduction de la documentation du nœud FreeU :

Le nœud FreeU applique des modifications dans le domaine fréquentiel aux blocs de sortie d'un modèle afin d'améliorer la qualité de génération d'images. Il fonctionne en mettant à l'échelle différents groupes de canaux et en appliquant un filtrage de Fourier à des cartes de caractéristiques spécifiques, permettant un contrôle fin du comportement du modèle pendant le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer les modifications FreeU | MODEL | Oui | - |
| `b1` | Facteur d'échelle du backbone pour les caractéristiques model_channels × 4 (par défaut : 1.1) | FLOAT | Oui | 0.0 - 10.0 |
| `b2` | Facteur d'échelle du backbone pour les caractéristiques model_channels × 2 (par défaut : 1.2) | FLOAT | Oui | 0.0 - 10.0 |
| `s1` | Facteur d'échelle de la connexion de saut pour les caractéristiques model_channels × 4 (par défaut : 0.9) | FLOAT | Oui | 0.0 - 10.0 |
| `s2` | Facteur d'échelle de la connexion de saut pour les caractéristiques model_channels × 2 (par défaut : 0.2) | FLOAT | Oui | 0.0 - 10.0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec les correctifs FreeU appliqués | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/fr.md)

---
**Source fingerprint (SHA-256):** `449a02a4bb5b42eb37fab394bcdc6375e08e369961d633618211ebc5f737ab51`
