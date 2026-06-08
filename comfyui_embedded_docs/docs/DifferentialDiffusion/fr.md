Voici la traduction de la documentation du nœud Differential Diffusion :

Le nœud Differential Diffusion modifie le processus de débruitage en appliquant un masque binaire basé sur des seuils de pas de temps. Il crée un masque qui effectue un mélange entre le masque de débruitage d'origine et un masque binaire basé sur un seuil, permettant un réglage contrôlé de l'intensité du processus de diffusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion à modifier | MODEL | Oui | - |
| `intensité` | Contrôle l'intensité du mélange entre le masque de débruitage d'origine et le masque binaire à seuil (valeur par défaut : 1.0) | FLOAT | Non | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle de diffusion modifié avec une fonction de masque de débruitage mise à jour | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/fr.md)

---
**Source fingerprint (SHA-256):** `3b1727baa6c546516f5dfb53e6e39f27fc7429cde2ac7fd7dfbab99eebb39816`
