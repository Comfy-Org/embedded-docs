# VEED Lipsync 2.0

Resynchronisez la bouche d’un intervenant dans une vidéo sur une nouvelle piste vocale avec VEED Lipsync. Utilisez-le pour doubler un clip ou remplacer ses dialogues tout en conservant la séquence d’origine. La sortie conserve la résolution de la vidéo à 25 fps et a la même durée que l’audio, avec un seul intervenant par vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser. La sélection d’un modèle révèle les paramètres qui lui sont spécifiques : `video`, `audio` et `seed`. | DYNAMIC_COMBO | Oui | `"lipsync-2.0"` |
| `video` | Séquence vidéo d’un seul intervenant face caméra. Si elle est plus courte que l’audio, elle est lue en avant puis en arrière jusqu’à la fin de l’audio. | VIDEO | Oui | - |
| `audio` | Nouvelle parole, jusqu’à 600 secondes. Détermine la durée de la vidéo. | AUDIO | Oui | Jusqu’à 600 secondes |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quel que soit la seed. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

Le nœud s’arrête avec une erreur lorsque la piste vocale dépasse 600 secondes, ou lorsque la tâche VEED échoue.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `VIDEO` | La vidéo resynchronisée : la séquence d’origine avec la bouche alignée sur la nouvelle parole. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedLipsyncNode/fr.md)

---
**Source fingerprint (SHA-256):** `1a1e854b6923b5bad0fd6f3a79e76c70231dee31a12e9cf0b22be6bdcc741168`
