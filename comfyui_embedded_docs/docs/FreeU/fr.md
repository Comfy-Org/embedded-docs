# FreeU

Le nœud FreeU applique des modifications dans le domaine fréquentiel aux blocs de sortie d'un modèle afin d'améliorer la qualité de génération d'images. Il fonctionne en mettant à l'échelle différents groupes de canaux et en appliquant un filtrage de Fourier à des cartes de caractéristiques spécifiques, ce qui permet un contrôle fin du comportement du modèle pendant le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Modèle auquel appliquer les modifications FreeU | MODEL | Oui | - |
| `b1` | Facteur d'échelle du backbone pour les caractéristiques de model_channels × 4 (par défaut : 1.1) | FLOAT | Oui | 0.0 - 10.0 |
| `b2` | Facteur d'échelle du backbone pour les caractéristiques de model_channels × 2 (par défaut : 1.2) | FLOAT | Oui | 0.0 - 10.0 |
| `s1` | Facteur d'échelle de la connexion de saut pour les caractéristiques de model_channels × 4 (par défaut : 0.9) | FLOAT | Oui | 0.0 - 10.0 |
| `s2` | Facteur d'échelle de la connexion de saut pour les caractéristiques de model_channels × 2 (par défaut : 0.2) | FLOAT | Oui | 0.0 - 10.0 |

Remarque : les ajustements FreeU sont appliqués uniquement aux cartes de caractéristiques dont le nombre de canaux est égal à model_channels × 4 (utilisant `b1` et `s1`) ou model_channels × 2 (utilisant `b2` et `s2`). Le filtre de Fourier ne met à l'échelle que la région centrale basse fréquence des cartes de caractéristiques de la connexion de saut ; toutes les autres composantes de fréquence restent inchangées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec les correctifs FreeU appliqués | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/fr.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
