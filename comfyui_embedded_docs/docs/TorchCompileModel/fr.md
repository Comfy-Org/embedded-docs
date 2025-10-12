> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/fr.md)

Le nœud TorchCompileModel applique la compilation PyTorch à un modèle pour optimiser ses performances. Il crée une copie du modèle d'entrée et l'encapsule avec la fonctionnalité de compilation de PyTorch en utilisant le backend spécifié. Cela peut améliorer la vitesse d'exécution du modèle pendant l'inférence.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle à compiler et optimiser |
| `backend` | STRING | Oui | "inductor"<br>"cudagraphs" | Le backend de compilation PyTorch à utiliser pour l'optimisation |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle compilé avec la compilation PyTorch appliquée |