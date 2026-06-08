Génère des images de manière synchrone en fonction du prompt et de la résolution. Ce nœud crée des images à l'aide du modèle Flux 1.1 Pro en envoyant des requêtes à un point de terminaison API et en attendant la réponse complète avant de renvoyer l'image générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt pour la génération d'image (par défaut : chaîne vide) | STRING | Oui | - |
| `prompt_upsampling` | Indique s'il faut effectuer un suréchantillonnage du prompt. Si activé, modifie automatiquement le prompt pour une génération plus créative, mais les résultats sont non déterministes (la même graine ne produira pas exactement le même résultat). (par défaut : False) | BOOLEAN | Oui | - |
| `width` | Largeur de l'image en pixels (par défaut : 1024, pas : 32) | INT | Oui | 256-1440 |
| `height` | Hauteur de l'image en pixels (par défaut : 768, pas : 32) | INT | Oui | 256-1440 |
| `seed` | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) | INT | Oui | 0-18446744073709551615 |
| `image_prompt` | Image de référence facultative pour guider la génération | IMAGE | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | L'image générée renvoyée par l'API | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `89316d84f364854541157b5b60bae3d4e25024bd4af61a47a1748c6671b463c1`
