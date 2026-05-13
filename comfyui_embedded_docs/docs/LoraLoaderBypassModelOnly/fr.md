> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypassModelOnly/fr.md)

Ce nœud applique un LoRA (Adaptation de Bas Rang) à un modèle pour modifier son comportement, mais n'affecte que la composante modèle elle-même. Il charge un fichier LoRA spécifié et ajuste les poids du modèle selon une force donnée, sans modifier les autres composants comme l'encodeur de texte CLIP.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de base auquel les ajustements LoRA seront appliqués. |
| `lora_name` | STRING | Oui | (Liste des fichiers LoRA disponibles) | Le nom du fichier LoRA à charger et appliquer. Les options sont générées à partir des fichiers présents dans le répertoire `loras`. |
| `strength_model` | FLOAT | Oui | -100.0 à 100.0 | La force de l'effet du LoRA sur les poids du modèle. Une valeur positive applique le LoRA, une valeur négative applique l'inverse, et une valeur de 0 n'a aucun effet (valeur par défaut : 1.0). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle modifié avec les ajustements LoRA appliqués à ses poids. |

---
**Source fingerprint (SHA-256):** `e0e1ad2d6481a1b9771d7eae833ffab0737a967d4af6e57b946d1b2223fe45bf`
