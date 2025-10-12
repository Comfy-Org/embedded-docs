> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/fr.md)

Le nœud Differential Diffusion modifie le processus de débruitage en appliquant un masque binaire basé sur des seuils d'étape temporelle. Il crée un masque qui mélange le masque de débruitage original avec un masque binaire basé sur un seuil, permettant un ajustement contrôlé de la force du processus de diffusion.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle de diffusion à modifier |
| `strength` | FLOAT | Non | 0.0 - 1.0 | Contrôle la force de mélange entre le masque de débruitage original et le masque de seuil binaire (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle de diffusion modifié avec la fonction de masque de débruitage mise à jour |
