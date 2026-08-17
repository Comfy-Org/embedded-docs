# FreeU

Le nœud FreeU applique des modifications dans le domaine fréquentiel aux blocs de sortie d'un modèle afin d'améliorer la qualité de génération d'images. Il fonctionne en mettant à l'échelle différents groupes de canaux et en appliquant un filtrage de Fourier à des cartes de caractéristiques spécifiques, ce qui permet un contrôle fin du comportement du modèle pendant le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer les modifications FreeU | MODEL | Oui | - |
| `b1` | Facteur de mise à l'échelle du backbone pour les cartes de caractéristiques model_channels × 4 (défaut : 1.1) | FLOAT | Oui | 0.0 - 10.0 |
| `b2` | Facteur de mise à l'échelle du backbone pour les cartes de caractéristiques model_channels × 2 (défaut : 1.2) | FLOAT | Oui | 0.0 - 10.0 |
| `s1` | Facteur de mise à l'échelle de la connexion de saut pour les cartes de caractéristiques model_channels × 4 (défaut : 0.9) | FLOAT | Oui | 0.0 - 10.0 |
| `s2` | Facteur de mise à l'échelle de la connexion de saut pour les cartes de caractéristiques model_channels × 2 (défaut : 0.2) | FLOAT | Oui | 0.0 - 10.0 |

Remarque : Les modifications sont appliquées uniquement aux cartes de caractéristiques ayant model_channels × 4 et model_channels × 2 canaux ; `b1`/`s1` affectent les premières et `b2`/`s2` affectent les secondes. Les autres cartes de caractéristiques restent inchangées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec les patchs FreeU appliqués | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/fr.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
