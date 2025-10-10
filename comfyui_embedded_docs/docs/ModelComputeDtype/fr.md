> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/fr.md)

Le nœud ModelComputeDtype permet de modifier le type de données de calcul utilisé par un modèle lors de l'inférence. Il crée une copie du modèle d'entrée et applique le paramètre de type de données spécifié, ce qui peut aider à optimiser l'utilisation de la mémoire et les performances en fonction des capacités de votre matériel. Cela est particulièrement utile pour le débogage et les tests de différents paramètres de précision.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle d'entrée à modifier avec un nouveau type de données de calcul |
| `dtype` | STRING | Oui | "default"<br>"fp32"<br>"fp16"<br>"bf16" | Le type de données de calcul à appliquer au modèle |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec le nouveau type de données de calcul appliqué |