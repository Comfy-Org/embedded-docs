# ModèleÉchantillonnageFlux

Le nœud ModelSamplingFlux applique un échantillonnage Flux à un modèle donné en calculant un paramètre de décalage basé sur les dimensions de l'image. Il crée une configuration d'échantillonnage spécialisée qui ajuste le comportement du modèle en fonction des paramètres de largeur, hauteur et décalage spécifiés, puis renvoie le modèle modifié avec les nouveaux paramètres d'échantillonnage appliqués.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer l'échantillonnage Flux | MODEL | Oui | - |
| `décalage_max` | Valeur de décalage maximale pour le calcul d'échantillonnage (par défaut : 1,15) | FLOAT | Oui | 0,0 - 100,0 |
| `décalage_base` | Valeur de décalage de base pour le calcul d'échantillonnage (par défaut : 0,5) | FLOAT | Oui | 0,0 - 100,0 |
| `largeur` | Largeur de l'image cible en pixels (par défaut : 1024) | INT | Oui | 16 - MAX_RESOLUTION |
| `hauteur` | Hauteur de l'image cible en pixels (par défaut : 1024) | INT | Oui | 16 - MAX_RESOLUTION |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec la configuration d'échantillonnage Flux appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/fr.md)

---
**Source fingerprint (SHA-256):** `35733ab0cd032884ceada13715cf51e626586844e8e575471a5ba7cf8a1e5e49`
