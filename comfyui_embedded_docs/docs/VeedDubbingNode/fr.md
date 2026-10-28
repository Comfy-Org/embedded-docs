# VEED Dubbing

VEED Dubbing traduit la parole d’une vidéo dans une autre langue avec VEED, en clonant la voix de chaque locuteur et en synchronisant ses lèvres avec la traduction. Le clip est téléversé, la tâche VEED est interrogée, et la vidéo doublée revient à 25 ips, d’une durée égale à celle de sa nouvelle piste audio. Utilisez-le pour localiser un clip terminé sans avoir à retourner ni à réenregistrer la voix.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle de doublage. `"standard"` est moins cher et renvoie de l’audio mono, avec l’espagnol d’Amérique latine et le portugais brésilien ; `"pro"` ajoute des accents régionaux et de l’audio stéréo. La sélection d’un modèle affiche `video`, `target_language`, `source_language` et `seed`. | DYNAMIC_COMBO | Oui | `"standard"`<br>`"pro"` |

### Entrées standard

Ces entrées apparaissent lorsque `model` est défini sur `"standard"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Vidéo avec un visage et une parole visibles, jusqu’à 599 secondes. La sortie a la même durée que sa piste audio et est lue à 25 ips. | VIDEO | Oui | Jusqu’à 599 secondes |
| `target_language` | Langue de doublage, parmi 85 langues. (par défaut : `"English"`) | COMBO | Oui | 85 langues |
| `source_language` | Langue parlée dans la vidéo, ou `"auto"` pour la détecter. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>85 langues |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

### Entrées pro

Ces entrées apparaissent lorsque `model` est défini sur `"pro"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Vidéo avec un visage et une parole visibles, jusqu’à 599 secondes. La sortie a la même durée que sa piste audio et est lue à 25 ips. | VIDEO | Oui | Jusqu’à 599 secondes |
| `target_language` | Langue ou accent régional de doublage : 87 langues plus 14 accents tels que `"English (UK)"`, `"Spanish (Mexico)"` et `"Portuguese (Brazil)"`. (par défaut : `"English (US)"`) | COMBO | Oui | 101 options |
| `source_language` | Langue parlée dans la vidéo, ou `"auto"` pour la détecter. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>91 langues |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

Le nœud s’arrête avec une erreur lorsque la vidéo n’a pas de piste audio, lorsque le clip dure plus de 599 secondes ou lorsque la tâche VEED échoue.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo doublée : les images d’origine avec la parole traduite et un mouvement des lèvres synchronisé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedDubbingNode/fr.md)

---
**Source fingerprint (SHA-256):** `fb818ca510e20bccffde61dca98c457984b8a110976e56f2a513f6c7f4d80c80`
