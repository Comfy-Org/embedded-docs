# ModèleÉchantillonnageFlux

Le nœud ModelSamplingFlux applique l'échantillonnage de modèle Flux à un modèle donné en calculant un paramètre de décalage basé sur les dimensions de l'image. Il crée une configuration d'échantillonnage spécialisée qui ajuste le comportement du modèle en fonction des paramètres de largeur, hauteur et décalage spécifiés, puis renvoie le modèle modifié avec les nouveaux réglages d'échantillonnage appliqués.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer l'échantillonnage Flux | MODEL | Oui | - |
| `max_shift` | Valeur de décalage maximale pour le calcul de l'échantillonnage (défaut : 1.15) | FLOAT | Oui | 0.0 - 100.0 |
| `base_shift` | Valeur de décalage de base pour le calcul de l'échantillonnage (défaut : 0.5) | FLOAT | Oui | 0.0 - 100.0 |
| `width` | Largeur de l'image cible en pixels (défaut : 1024) | INT | Oui | 16 - MAX_RESOLUTION |
| `height` | Hauteur de l'image cible en pixels (défaut : 1024) | INT | Oui | 16 - MAX_RESOLUTION |

La valeur de décalage effective est interpolée entre `base_shift` et `max_shift` en fonction de la taille latente dérivée de `width` et `height`. La valeur de `step` est de 0.01 pour `max_shift` et `base_shift`, et de 8 pour `width` et `height`. Les paramètres `max_shift` et `base_shift` sont marqués comme options avancées dans l'interface utilisateur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec la configuration d'échantillonnage Flux appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/fr.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
