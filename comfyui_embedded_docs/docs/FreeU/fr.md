# FreeU

Le nœud FreeU applique des modifications dans le domaine fréquentiel aux blocs de sortie d'un modèle afin d'améliorer la qualité de génération d'images. Il fonctionne en mettant à l'échelle différents groupes de canaux et en appliquant un filtrage de Fourier à des cartes de caractéristiques spécifiques, ce qui permet un contrôle fin du comportement du modèle pendant le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer les modifications FreeU | MODEL | Oui | - |
| `b1` | Facteur de mise à l'échelle du backbone appliqué aux cartes de caractéristiques ayant model_channels × 4 canaux (par défaut : 1.1). Marqué comme paramètre avancé. | FLOAT | Oui | 0.0 - 10.0 |
| `b2` | Facteur de mise à l'échelle du backbone appliqué aux cartes de caractéristiques ayant model_channels × 2 canaux (par défaut : 1.2). Marqué comme paramètre avancé. | FLOAT | Oui | 0.0 - 10.0 |
| `s1` | Facteur de mise à l'échelle de la connexion de saut appliqué aux cartes de caractéristiques ayant model_channels × 4 canaux (par défaut : 0.9). Marqué comme paramètre avancé. | FLOAT | Oui | 0.0 - 10.0 |
| `s2` | Facteur de mise à l'échelle de la connexion de saut appliqué aux cartes de caractéristiques ayant model_channels × 2 canaux (par défaut : 0.2). Marqué comme paramètre avancé. | FLOAT | Oui | 0.0 - 10.0 |

Remarque : les ajustements FreeU sont appliqués uniquement aux cartes de caractéristiques dont le nombre de canaux est égal à model_channels × 4 (en utilisant `b1` et `s1`) ou model_channels × 2 (en utilisant `b2` et `s2`). Le filtre de Fourier ne met à l'échelle que la région centrale des basses fréquences (seuil de 1) des cartes de caractéristiques de connexion de saut ; toutes les autres composantes fréquentielles restent inchangées. Les quatre paramètres de mise à l'échelle acceptent des valeurs entre 0.0 et 10.0 par pas de 0.01.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec les patchs FreeU appliqués | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/fr.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
