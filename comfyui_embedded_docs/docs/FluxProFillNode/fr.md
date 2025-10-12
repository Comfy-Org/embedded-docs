> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/fr.md)

Restaure l'image basée sur un masque et une instruction. Ce nœud utilise le modèle Flux.1 pour remplir les zones masquées d'une image selon la description textuelle fournie, en générant un nouveau contenu qui s'harmonise avec l'image environnante.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à restaurer |
| `mask` | MASK | Oui | - | Le masque définissant les zones de l'image à remplir |
| `prompt` | STRING | Non | - | Instruction pour la génération d'image (par défaut : chaîne vide) |
| `suréchantillonnage du prompt` | BOOLEAN | Non | - | Détermine si un suréchantillonnage doit être appliqué à l'instruction. Si actif, modifie automatiquement l'instruction pour une génération plus créative, mais les résultats sont non déterministes (la même graîne ne produira pas exactement le même résultat). (par défaut : false) |
| `guidage` | FLOAT | Non | 1.5-100 | Intensité de guidage pour le processus de génération d'image (par défaut : 60) |
| `étapes` | INT | Non | 15-50 | Nombre d'étapes pour le processus de génération d'image (par défaut : 50) |
| `seed` | INT | Non | 0-18446744073709551615 | La graîne aléatoire utilisée pour créer le bruit. (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output_image` | IMAGE | L'image générée avec les zones masquées remplies selon l'instruction |
