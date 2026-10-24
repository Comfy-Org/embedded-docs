# Mirelo Video to SFX

Générez des effets sonores qui suivent une vidéo avec Mirelo SFX. Le clip est téléversé, le modèle suit l’action à l’écran et renvoie un mixage d’effets sonores, ainsi qu’une piste de parole séparée contenant le dialogue extrait de la bande-son. Utilisez-le pour ajouter du bruitage, de l’ambiance et des impacts à des clips silencieux ou partiellement silencieux.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser. La sélection d’un modèle révèle les paramètres qui lui sont propres : `video`, `audio`, `prompt`, `negative_prompt`, `preserve_speech` et `seed`. | DYNAMIC_COMBO | Oui | `"sfx-2.0"` |
| `video` | La vidéo pour laquelle générer du son. Le son est généré pour tout le clip, de 1 à 600 secondes. | VIDEO | Oui | 1 à 600 secondes |
| `audio` | Piste de dialogue à utiliser à la place de la bande-son de la vidéo pour `preserve_speech` et pour la sortie `speech`. Laissez-la non connectée pour utiliser le son intégré à la vidéo. | AUDIO | Non | - |
| `prompt` | À quoi le son doit ressembler. Peut être laissé vide (par défaut : vide), car le modèle décrit lui-même la vidéo et ne suit pas toujours le prompt. Maximum 2000 caractères. | STRING | Oui | Jusqu’à 2000 caractères |
| `negative_prompt` | Sons à éviter, sous forme d’une courte liste séparée par des virgules. Peut être laissé vide (par défaut : vide). Maximum 1000 caractères. | STRING | Oui | Jusqu’à 1000 caractères |
| `preserve_speech` | Conserver le dialogue mixé sous le son généré. Désactivé renvoie uniquement les effets sonores. (par défaut : True) | BOOLEAN | Oui | false<br>true |
| `seed` | La graine de la requête. Les résultats sont non déterministes, donc la même graine ne reproduit pas un clip à l’identique. (par défaut : 42) | INT | Oui | 0 à 4294967295 |

Le nœud s’arrête avec une erreur lorsque le clip dure moins de 1 seconde ou plus de 600 secondes. Une piste `audio` connectée définit le dialogue que `preserve_speech` conserve et que la sortie `speech` sépare ; sans piste connectée, le dialogue provient de la bande-son de la vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | Le mixage des effets sonores pour le clip, avec le dialogue mixé en dessous lorsque `preserve_speech` est activé. | AUDIO |
| `speech` | Le dialogue séparé de la bande-son. Silencieux, avec le même taux d’échantillonnage que `audio`, lorsqu’aucune parole n’est détectée ou que la séparation de la parole ne renvoie rien. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloVideoToSFX/fr.md)

---
**Source fingerprint (SHA-256):** `fa09525e6c9b10412823e358652220850fbc7109d81cc207d31ffa8921956495`
