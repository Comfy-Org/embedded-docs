> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/fr.md)

Voici la traduction de la documentation du nœud FreeU :

Le nœud FreeU applique des modifications dans le domaine fréquentiel aux blocs de sortie d'un modèle afin d'améliorer la qualité de génération d'images. Il fonctionne en mettant à l'échelle différents groupes de canaux et en appliquant un filtrage de Fourier à des cartes de caractéristiques spécifiques, permettant un contrôle fin du comportement du modèle pendant le processus de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer les modifications FreeU |
| `b1` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle du backbone pour les caractéristiques model_channels × 4 (par défaut : 1.1) |
| `b2` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle du backbone pour les caractéristiques model_channels × 2 (par défaut : 1.2) |
| `s1` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle de la connexion de saut pour les caractéristiques model_channels × 4 (par défaut : 0.9) |
| `s2` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle de la connexion de saut pour les caractéristiques model_channels × 2 (par défaut : 0.2) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model` | MODEL | Le modèle modifié avec les correctifs FreeU appliqués |

---
**Source fingerprint (SHA-256):** `449a02a4bb5b42eb37fab394bcdc6375e08e369961d633618211ebc5f737ab51`
