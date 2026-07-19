# SyncTalkingImageNode

Animez un portrait fixe en une vidéo parlante pilotée par un fichier audio vocal, en utilisant le modèle sync-3 de sync.so. La durée de sortie correspond à la durée audio, et le coût évolue en fonction de la durée de sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Une seule image avec un visage clairement visible, jusqu'à 4K (4096x2160). | IMAGE | Oui | Une seule image requise |
| `audio` | Audio vocal pilotant la vidéo parlante ; la durée de sortie lui correspond. Enchaînez n'importe quel nœud TTS ici pour piloter l'animation à partir d'un texte. | AUDIO | Oui | Durée maximale : 600 secondes |
| `prompt` | Indication facultative sur la façon dont le portrait prend vie, par exemple « faire sourire le sujet et regarder la caméra ». Laissez vide pour un mouvement de parole naturel. (par défaut : "") | STRING | Non | Texte multiligne |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) | INT | Non | 0 à 2147483647 |
| `model` | Modèle de génération sync.so. L'entrée d'image est exclusive à sync-3. | COMBO | Oui | `"sync-3"` |
| `speaker_selection` | Quel visage animer lorsque plusieurs personnes sont visibles. `default` : laisser le modèle décider. `coordinates` : cibler le visage au pixel (speaker_x, speaker_y) dans l'image. La détection automatique n'est pas prise en charge pour les images. (par défaut : "default") | COMBO | Non | `"default"`<br>`"coordinates"` |
| `speaker_x` | Coordonnée X en pixels du visage de l'orateur. Utilisé uniquement lorsque speaker_selection est 'coordinates'. (par défaut : 0) | INT | Non | 0 à 4096 |
| `speaker_y` | Coordonnée Y en pixels du visage de l'orateur. Utilisé uniquement lorsque speaker_selection est 'coordinates'. (par défaut : 0) | INT | Non | 0 à 4096 |
| `auto_downscale` | Réduire automatiquement l'image si elle dépasse la limite d'entrée 4K (4096x2160) ; les coordonnées de l'orateur sont mises à l'échelle pour correspondre. Lorsque désactivé, une image surdimensionnée génère une erreur à la place. (par défaut : True) | BOOLEAN | Non | True<br>False |

**Remarque :** Les paramètres `speaker_x` et `speaker_y` sont utilisés uniquement lorsque `speaker_selection` est défini sur `"coordinates"`. Lorsque `auto_downscale` est activé, les coordonnées de l'orateur sont automatiquement mises à l'échelle pour correspondre aux dimensions de l'image réduite.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo parlante générée avec le portrait animé synchronisé sur l'audio d'entrée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncTalkingImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `21f722cdcc5ff017949887ed2252854feebb9b913034dc6a6c3ce196ad089468`
