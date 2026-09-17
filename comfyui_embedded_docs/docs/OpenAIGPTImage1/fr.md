# OpenAI GPT Image 2

Génère des images de manière synchrone via le point de terminaison GPT Image d'OpenAI. Il peut créer de nouvelles images à partir d'un prompt textuel ou modifier des images existantes lorsqu'une image d'entrée et un masque facultatif sont fournis. Le nœud prend en charge les modèles `gpt-image-1`, `gpt-image-1.5` et `gpt-image-2` et est marqué comme déprécié.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour GPT Image (par défaut : "") | STRING | Oui | - |
| `seed` | Graine aléatoire pour la génération ; pas encore implémentée dans le backend (par défaut : 0) | INT | Non | 0 à 2147483647 |
| `qualité` | Qualité de l'image, affecte le coût et le temps de génération (par défaut : "low") | COMBO | Non | "low"<br>"medium"<br>"high" |
| `arrière-plan` | Renvoie l'image avec ou sans arrière-plan (par défaut : "auto") | COMBO | Non | "auto"<br>"opaque"<br>"transparent" |
| `taille` | Taille de l'image. Sélectionnez "Custom" pour utiliser la largeur et la hauteur personnalisées (GPT Image 2 uniquement) (par défaut : "auto") | COMBO | Non | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | Nombre d'images à générer (par défaut : 1) | INT | Non | 1 à 8 |
| `image` | Image de référence facultative pour la modification d'image | IMAGE | Non | - |
| `mask` | Masque facultatif pour l'inpainting (les zones blanches seront remplacées) | MASK | Non | - |
| `model` | Modèle GPT Image à utiliser (par défaut : "gpt-image-2") | COMBO | Non | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `largeur_personnalisée` | Utilisé uniquement lorsque `size` vaut "Custom". Doit être un multiple de 16 (GPT Image 2 uniquement) (par défaut : 1024) | INT | Non | 1024 à 3840, pas de 16 |
| `hauteur_personnalisée` | Utilisé uniquement lorsque `size` vaut "Custom". Doit être un multiple de 16 (GPT Image 2 uniquement) (par défaut : 1024) | INT | Non | 1024 à 3840, pas de 16 |

**Contraintes sur les paramètres :**

- Lorsque `image` est fourni, le nœud utilise le point de terminaison de modification d'image.
- `mask` ne peut être utilisé que lorsque `image` est fourni.
- Lors de l'utilisation de `mask`, une seule image à la fois est prise en charge (la taille du lot doit être 1).
- `mask` et `image` doivent avoir la même taille.
- La résolution personnalisée (`size` = "Custom") n'est prise en charge que par le modèle `gpt-image-2`.
- La largeur et la hauteur personnalisées doivent être des multiples de 16.
- Le bord le plus long d'une résolution personnalisée ne doit pas dépasser 3840.
- Le rapport d'aspect d'une résolution personnalisée ne doit pas dépasser 3:1.
- Le nombre total de pixels d'une résolution personnalisée doit être compris entre 655 360 et 8 294 400.
- Les modèles `gpt-image-1` et `gpt-image-1.5` ne prennent en charge que les tailles `auto`, `1024x1024`, `1024x1536` et `1536x1024`. Les autres tailles ne sont prises en charge que par le modèle `gpt-image-2`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | Image(s) générée(s) ou modifiée(s). Plusieurs images sont renvoyées sous forme de lot ; si les images renvoyées ont des dimensions différentes, elles sont redimensionnées pour correspondre à la première image. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/fr.md)

---
**Source fingerprint (SHA-256):** `f0f0db7fd2cdf8efd2155522b289aa8f3f939fa79a6e9060b0ffbb2dd20efa1e`
