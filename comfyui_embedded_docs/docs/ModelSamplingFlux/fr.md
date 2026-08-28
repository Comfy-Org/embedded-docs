# ModèleÉchantillonnageFlux

Le nœud ModelSamplingFlux applique l'échantillonnage Flux à un modèle donné en calculant un paramètre de décalage basé sur les dimensions de l'image. Il crée une configuration d'échantillonnage spécialisée qui ajuste le comportement du modèle en fonction de la largeur, de la hauteur et des paramètres de décalage spécifiés, puis renvoie le modèle modifié avec les nouveaux réglages d'échantillonnage appliqués.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer l'échantillonnage Flux | MODEL | Oui | - |
| `décalage_max` | Valeur de décalage maximale pour le calcul d'échantillonnage (défaut : 1.15) | FLOAT | Oui | 0.0 - 100.0 (step 0.01) |
| `décalage_base` | Valeur de décalage de base pour le calcul d'échantillonnage (défaut : 0.5) | FLOAT | Oui | 0.0 - 100.0 (step 0.01) |
| `largeur` | Largeur de l'image cible en pixels (défaut : 1024) | INT | Oui | 16 - MAX_RESOLUTION (step 8) |
| `hauteur` | Hauteur de l'image cible en pixels (défaut : 1024) | INT | Oui | 16 - MAX_RESOLUTION (step 8) |

`max_shift` et `base_shift` sont des paramètres avancés. Le décalage appliqué à la configuration d'échantillonnage est calculé à partir des dimensions de l'image : la résolution latente est calculée comme `width × height / 256`, et la valeur de décalage est interpolée entre `base_shift` à une résolution latente de 256 et `max_shift` à une résolution latente de 4096.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec la configuration d'échantillonnage Flux appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/fr.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
