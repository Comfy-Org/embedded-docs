# OpenAI GPT Image 2

Génère des images de manière synchrone via le endpoint GPT Image d'OpenAI. Ce nœud peut créer de nouvelles images à partir d'invites texte ou modifier des images existantes lorsqu'une image d'entrée et un masque optionnel sont fournis. Il prend en charge plusieurs modèles GPT Image, notamment gpt-image-1, gpt-image-1.5 et gpt-image-2. Ce nœud est obsolète.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite texte pour GPT Image (par défaut : "") | STRING | Oui | - |
| `seed` | Graine aléatoire pour la génération (par défaut : 0) - pas encore implémentée dans le backend | INT | Non | 0 à 2147483647 |
| `quality` | Qualité de l'image, affecte le coût et le temps de génération (par défaut : "low") | COMBO | Non | "low"<br>"medium"<br>"high" |
| `background` | Renvoie l'image avec ou sans arrière-plan (par défaut : "auto") | COMBO | Non | "auto"<br>"opaque"<br>"transparent" |
| `size` | Taille de l'image. Sélectionnez « Custom » pour utiliser la largeur et la hauteur personnalisées (GPT Image 2 uniquement) (par défaut : "auto") | COMBO | Non | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | Nombre d'images à générer (par défaut : 1) | INT | Non | 1 à 8 |
| `image` | Image de référence optionnelle pour l'édition d'image | IMAGE | Non | - |
| `mask` | Masque optionnel pour l'inpainting (les zones blanches seront remplacées) | MASK | Non | - |
| `model` | Modèle GPT Image à utiliser (par défaut : "gpt-image-2") | COMBO | Non | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | Utilisé uniquement lorsque `size` est « Custom ». Doit être un multiple de 16 (GPT Image 2 uniquement) (par défaut : 1024) | INT | Non | 1024 à 3840 |
| `custom_height` | Utilisé uniquement lorsque `size` est « Custom ». Doit être un multiple de 16 (GPT Image 2 uniquement) (par défaut : 1024) | INT | Non | 1024 à 3840 |

**Contraintes des paramètres :**

- Lorsque `image` est fourni, le nœud passe en mode édition d'image
- `mask` ne peut être utilisé que lorsque `image` est fourni
- Lors de l'utilisation de `mask`, seules les images uniques sont prises en charge (la taille du lot doit être 1)
- `mask` et `image` doivent avoir la même taille
- La résolution personnalisée (`size` = « Custom ») n'est prise en charge que par le modèle gpt-image-2
- La largeur et la hauteur personnalisées doivent être des multiples de 16
- Le rapport hauteur/largeur de la résolution personnalisée ne doit pas dépasser 3:1
- Le nombre total de pixels de la résolution personnalisée doit être compris entre 655 360 et 8 294 400
- L'arrière-plan transparent n'est pas pris en charge pour le modèle gpt-image-2
- Les tailles supérieures à 1536x1024 (par exemple, 2048x2048, 3840x2160) ne sont prises en charge que par le modèle gpt-image-2

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | Image(s) générée(s) ou éditée(s) | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/fr.md)

---
**Source fingerprint (SHA-256):** `bf588bffced6e66536b4cb54655ef6ebb9cf988d9739e3c379a8ebda1486e20a`
