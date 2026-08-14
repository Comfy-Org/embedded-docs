# Kling Omni Première-Dernière-Image vers Vidéo (Pro)

Ce nœud utilise le dernier modèle Kling AI pour générer une vidéo à partir d'une image de départ, d'une image de fin facultative ou d'images de référence. Il peut créer une vidéo unique ou un storyboard multi-plans avec des prompts et des durées individuels pour chaque segment. Le nœud traite ces entrées pour produire une vidéo d'une longueur et d'une résolution spécifiées, avec une génération audio facultative.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_name` | Le modèle Kling AI spécifique à utiliser pour la génération de vidéo. | COMBO | Oui | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Un prompt textuel décrivant le contenu de la vidéo. Il peut inclure des descriptions à la fois positives et négatives. Ignoré lorsque les storyboards sont activés. | STRING | Oui | - |
| `duration` | La durée souhaitée de la vidéo générée en secondes (par défaut : 5). | INT | Oui | 3 à 15 |
| `first_frame` | L'image de départ pour la séquence vidéo. | IMAGE | Oui | - |
| `end_frame` | Une image de fin facultative pour la vidéo. Elle ne peut pas être utilisée simultanément avec `reference_images`. Ne fonctionne pas avec les storyboards. | IMAGE | Non | - |
| `reference_images` | Jusqu'à 6 images de référence supplémentaires. | IMAGE | Non | - |
| `resolution` | La résolution de sortie de la vidéo générée (par défaut : « 1080p »). | COMBO | Non | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Génère une série de segments vidéo avec des prompts et des durées individuels. Uniquement pris en charge pour `kling-v3-omni`. Lorsqu'il est activé, chaque storyboard nécessite une entrée de prompt et de durée. | DYNAMIC_COMBO | Non | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Génère l'audio de la vidéo (par défaut : False). Uniquement pris en charge pour `kling-v3-omni`. | BOOLEAN | Non | True / False |
| `seed` | Le paramètre `seed` contrôle si le nœud doit se réexécuter ; les résultats sont non déterministes quelle que soit la valeur de `seed` (par défaut : 0). | INT | Non | 0 à 2147483647 |

### Entrées du storyboard

Lorsque `storyboards` est défini sur une valeur autre que « disabled », les entrées suivantes sont ajoutées pour chaque segment sélectionné (N varie de 1 au nombre de storyboards sélectionné) :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `storyboard_N_prompt` | Prompt pour le segment de storyboard N. 512 caractères maximum. (par défaut : "") | STRING | Oui | - |
| `storyboard_N_duration` | Durée pour le segment de storyboard N en secondes (par défaut : 4). | INT | Oui | 1 à 15 |

**Contraintes importantes :**

* L'entrée `end_frame` ne peut pas être utilisée en même temps que l'entrée `reference_images`.
* L'entrée `end_frame` ne peut pas être utilisée simultanément avec les storyboards.
* Le modèle `kling-video-o1` ne prend pas en charge les durées supérieures à 10 secondes, la génération audio, la résolution 4k ou les storyboards.
* Si vous ne fournissez pas de `end_frame` ni de `reference_images` avec le modèle `kling-video-o1`, la `duration` ne peut être définie que sur 5 ou 10 secondes.
* Toutes les images d'entrée (`first_frame`, `end_frame` et les éventuelles `reference_images`) doivent avoir une dimension minimale de 300 pixels en largeur et en hauteur.
* Le rapport hauteur/largeur de toutes les images d'entrée doit être compris entre 1:2.5 et 2.5:1.
* Un maximum de 6 images peut être fourni via l'entrée `reference_images`.
* Le texte du `prompt` doit avoir une longueur comprise entre 1 et 2500 caractères (0 caractère autorisé lorsque les storyboards sont activés).
* Le prompt peut faire référence aux images d'entrée à l'aide des espaces réservés `@image`, `@image1`, `@image2`, etc. ; ceux-ci sont automatiquement convertis au format de référence d'image compatible avec l'API.
* Lorsque les storyboards sont activés, la durée totale de tous les segments du storyboard doit être égale à la valeur globale `duration`.
* Chaque prompt de storyboard doit avoir une longueur comprise entre 1 et 512 caractères.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `2b26914ba29c3d877a981e41acb44d15dfacc604d86d7cc232ebfa7fda0ae3b8`
