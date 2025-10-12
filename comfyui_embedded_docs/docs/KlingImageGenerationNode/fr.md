> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/fr.md)

Le nœud Kling Image Generation génère des images à partir de prompts texte avec la possibilité d'utiliser une image de référence comme guide. Il crée une ou plusieurs images basées sur votre description texte et les paramètres de référence, puis retourne les images générées en sortie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Prompt texte positif |
| `negative_prompt` | STRING | Oui | - | Prompt texte négatif |
| `image_type` | COMBO | Oui | Options de KlingImageGenImageReferenceType<br>(extraites du code source) | Sélection du type de référence d'image |
| `image_fidelity` | FLOAT | Oui | 0.0 - 1.0 | Intensité de référence pour les images téléchargées par l'utilisateur (par défaut : 0.5) |
| `human_fidelity` | FLOAT | Oui | 0.0 - 1.0 | Similarité de référence du sujet (par défaut : 0.45) |
| `model_name` | COMBO | Oui | "kling-v1"<br>(et autres options de KlingImageGenModelName) | Sélection du modèle pour la génération d'images (par défaut : "kling-v1") |
| `aspect_ratio` | COMBO | Oui | "16:9"<br>(et autres options de KlingImageGenAspectRatio) | Ratio d'aspect pour les images générées (par défaut : "16:9") |
| `n` | INT | Oui | 1 - 9 | Nombre d'images générées (par défaut : 1) |
| `image` | IMAGE | Non | - | Image de référence optionnelle |

**Contraintes des paramètres :**

- Le paramètre `image` est optionnel, mais lorsqu'il est fourni, le modèle kling-v1 ne prend pas en charge les images de référence
- Les prompts positif et négatif ont des limitations de longueur maximale (MAX_PROMPT_LENGTH_IMAGE_GEN)
- Lorsqu'aucune image de référence n'est fournie, le paramètre `image_type` est automatiquement défini sur None

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | Image(s) générée(s) basée(s) sur les paramètres d'entrée |
