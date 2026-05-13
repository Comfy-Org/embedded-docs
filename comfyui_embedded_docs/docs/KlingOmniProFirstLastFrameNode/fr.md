> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/fr.md)

Ce nœud utilise le dernier modèle d'IA Kling pour générer une vidéo à partir d'une image de début, d'une image de fin optionnelle ou d'images de référence. Il peut créer une vidéo unique ou un storyboard multi-plans avec des prompts et des durées individuels pour chaque segment. Le nœud traite ces entrées pour produire une vidéo d'une longueur et d'une résolution spécifiées, avec une génération audio optionnelle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-v3-omni"`<br>`"kling-video-o1"` | Le modèle d'IA Kling spécifique à utiliser pour la génération vidéo. |
| `prompt` | STRING | Oui | - | Un prompt textuel décrivant le contenu de la vidéo. Peut inclure des descriptions positives et négatives. Ignoré lorsque les storyboards sont activés. |
| `duration` | INT | Oui | 3 à 15 | La durée souhaitée de la vidéo générée en secondes (par défaut : 5). |
| `first_frame` | IMAGE | Oui | - | L'image de départ pour la séquence vidéo. |
| `end_frame` | IMAGE | Non | - | Une image de fin optionnelle pour la vidéo. Ne peut pas être utilisée simultanément avec `reference_images`. Ne fonctionne pas avec les storyboards. |
| `reference_images` | IMAGE | Non | - | Jusqu'à 6 images de référence supplémentaires. |
| `resolution` | COMBO | Non | `"4k"`<br>`"1080p"`<br>`"720p"` | La résolution de sortie pour la vidéo générée (par défaut : "1080p"). |
| `storyboards` | DYNAMIC_COMBO | Non | `"désactivé"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | Génère une série de segments vidéo avec des prompts et des durées individuels. Uniquement pris en charge pour `kling-v3-omni`. Lorsque cette option est activée, chaque storyboard nécessite un prompt et une durée. |
| `générer l'audio` | BOOLEAN | Non | Vrai / Faux | Génère l'audio pour la vidéo (par défaut : Faux). Uniquement pris en charge pour `kling-v3-omni`. |
| `seed` | INT | Non | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0). |

**Contraintes importantes :**

* L'entrée `end_frame` ne peut pas être utilisée en même temps que l'entrée `reference_images`.
* L'entrée `end_frame` ne peut pas être utilisée simultanément avec les storyboards.
* Le modèle `kling-video-o1` ne prend pas en charge les durées supérieures à 10 secondes, la génération audio, la résolution 4k ou les storyboards.
* Si vous ne fournissez pas de `end_frame` ou de `reference_images` avec le modèle `kling-video-o1`, la `duration` ne peut être définie que sur 5 ou 10 secondes.
* Toutes les images d'entrée (`first_frame`, `end_frame` et toutes les `reference_images`) doivent avoir une dimension minimale de 300 pixels en largeur et en hauteur.
* Le rapport hauteur/largeur de toutes les images d'entrée doit être compris entre 1:2,5 et 2,5:1.
* Un maximum de 6 images peut être fourni via l'entrée `reference_images`.
* Le texte du `prompt` doit avoir une longueur comprise entre 1 et 2500 caractères (0 caractères autorisés lorsque les storyboards sont activés).
* Lorsque les storyboards sont activés, la durée totale de tous les segments du storyboard doit être égale à la valeur globale de `duration`.
* Chaque prompt de storyboard doit avoir une longueur comprise entre 1 et 512 caractères.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `bd0fb11242b7f79062079b1aa48c3524abf59ecf06a90f013e57b6910cd8e224`
