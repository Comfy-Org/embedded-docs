> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/fr.md)

Génère des images de manière synchrone via le point de terminaison GPT Image 1 d'OpenAI. Ce nœud peut créer de nouvelles images à partir d'invitations textuelles ou modifier des images existantes lorsqu'une image d'entrée et un masque optionnel sont fournis.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invitation textuelle pour GPT Image 1 (par défaut : "") |
| `seed` | INT | Non | 0 à 2147483647 | Graine aléatoire pour la génération (par défaut : 0) - pas encore implémentée dans le backend |
| `quality` | COMBO | Non | "low"<br>"medium"<br>"high" | Qualité de l'image, affecte le coût et le temps de génération (par défaut : "low") |
| `background` | COMBO | Non | "opaque"<br>"transparent" | Retourne l'image avec ou sans arrière-plan (par défaut : "opaque") |
| `size` | COMBO | Non | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024" | Taille de l'image (par défaut : "auto") |
| `n` | INT | Non | 1 à 8 | Nombre d'images à générer (par défaut : 1) |
| `image` | IMAGE | Non | - | Image de référence optionnelle pour l'édition d'image (par défaut : Aucune) |
| `mask` | MASK | Non | - | Masque optionnel pour l'inpainting (les zones blanches seront remplacées) (par défaut : Aucune) |

**Contraintes des paramètres :**
- Lorsque `image` est fournie, le nœud passe en mode édition d'image
- `mask` ne peut être utilisé que lorsque `image` est fournie
- Lors de l'utilisation de `mask`, seules les images uniques sont prises en charge (la taille du lot doit être de 1)
- `mask` et `image` doivent avoir la même taille

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Image(s) générée(s) ou modifiée(s) |