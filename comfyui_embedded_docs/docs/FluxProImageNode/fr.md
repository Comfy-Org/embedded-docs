> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/fr.md)

Génère des images de manière synchrone en fonction de l'invite et de la résolution. Ce nœud crée des images en utilisant le modèle Flux 1.1 Pro en envoyant des requêtes à un point de terminaison API et en attendant la réponse complète avant de renvoyer l'image générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite pour la génération d'image (par défaut : chaîne vide) |
| `prompt_upsampling` | BOOLEAN | Oui | - | Indique s'il faut effectuer un suréchantillonnage sur l'invite. Si actif, modifie automatiquement l'invite pour une génération plus créative, mais les résultats sont non déterministes (la même graine ne produira pas exactement le même résultat). (par défaut : False) |
| `width` | INT | Oui | 256-1440 | Largeur de l'image en pixels (par défaut : 1024, pas : 32) |
| `height` | INT | Oui | 256-1440 | Hauteur de l'image en pixels (par défaut : 768, pas : 32) |
| `seed` | INT | Oui | 0-18446744073709551615 | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) |
| `image_prompt` | IMAGE | Non | - | Image de référence optionnelle pour guider la génération |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image générée renvoyée par l'API |