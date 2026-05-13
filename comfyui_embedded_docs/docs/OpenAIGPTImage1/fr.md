> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI :

Génère des images de manière synchrone via le point de terminaison GPT Image d'OpenAI. Ce nœud peut créer de nouvelles images à partir de descriptions textuelles ou modifier des images existantes lorsqu'une image d'entrée et un masque optionnel sont fournis. Il prend en charge plusieurs modèles GPT Image, notamment gpt-image-1, gpt-image-1.5 et gpt-image-2.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Description textuelle pour GPT Image (par défaut : "") |
| `seed` | INT | Non | 0 à 2147483647 | Graine aléatoire pour la génération (par défaut : 0) - pas encore implémentée dans le backend |
| `quality` | COMBO | Non | "low"<br>"medium"<br>"high" | Qualité de l'image, affecte le coût et le temps de génération (par défaut : "low") |
| `background` | COMBO | Non | "auto"<br>"opaque"<br>"transparent" | Renvoie une image avec ou sans arrière-plan (par défaut : "auto") |
| `size` | COMBO | Non | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" | Taille de l'image. Sélectionnez "Custom" pour utiliser la largeur et la hauteur personnalisées (GPT Image 2 uniquement) (par défaut : "auto") |
| `n` | INT | Non | 1 à 8 | Nombre d'images à générer (par défaut : 1) |
| `image` | IMAGE | Non | - | Image de référence optionnelle pour la modification d'image |
| `mask` | MASK | Non | - | Masque optionnel pour l'incrustation (les zones blanches seront remplacées) |
| `model` | COMBO | Non | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" | Modèle GPT Image à utiliser (par défaut : "gpt-image-2") |
| `custom_width` | INT | Non | 1024 à 3840 | Utilisé uniquement lorsque `size` est "Custom". Doit être un multiple de 16 (GPT Image 2 uniquement) (par défaut : 1024) |
| `custom_height` | INT | Non | 1024 à 3840 | Utilisé uniquement lorsque `size` est "Custom". Doit être un multiple de 16 (GPT Image 2 uniquement) (par défaut : 1024) |

**Contraintes des paramètres :**

- Lorsque `image` est fourni, le nœud passe en mode édition d'image
- `mask` ne peut être utilisé que lorsque `image` est fourni
- Lors de l'utilisation de `mask`, seules les images uniques sont prises en charge (la taille du lot doit être de 1)
- `mask` et `image` doivent avoir la même taille
- La résolution personnalisée (`size` = "Custom") n'est prise en charge que par le modèle gpt-image-2
- La largeur et la hauteur personnalisées doivent être des multiples de 16
- Le rapport hauteur/largeur de la résolution personnalisée ne doit pas dépasser 3:1
- Le nombre total de pixels de la résolution personnalisée doit être compris entre 655 360 et 8 294 400
- L'arrière-plan transparent n'est pas pris en charge pour le modèle gpt-image-2
- Les tailles supérieures à 1536x1024 (par exemple, 2048x2048, 3840x2160) ne sont prises en charge que par le modèle gpt-image-2

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `IMAGE` | IMAGE | Image(s) générée(s) ou modifiée(s) |

---
**Source fingerprint (SHA-256):** `44b258d6afcb388db3836427abdd5a7cb5c09a0328efceef7e114dd61a38eae1`
