> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/fr.md)

Voici la traduction en français de la documentation du nœud Wan2VideoContinuation :

Le nœud Wan 2.7 Video Continuation génère un nouveau segment vidéo qui se poursuit de manière transparente à partir de la fin d'un clip vidéo d'entrée. Il utilise le modèle Wan 2.7 pour synthétiser la suite en fonction d'une invite textuelle et peut éventuellement guider la fin vers une image cible spécifique.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
| :--- | :--- | :--- | :--- | :--- |
| `model` | COMBO | Oui | `"wan2.7-i2v"` | Le modèle de génération vidéo à utiliser. |
| `model.prompt` | STRING | Oui | - | Invite décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois. (par défaut : chaîne vide) |
| `model.negative_prompt` | STRING | Oui | - | Invite négative décrivant ce qu'il faut éviter. (par défaut : chaîne vide) |
| `model.resolution` | COMBO | Oui | `"720P"`<br>`"1080P"` | La résolution de la vidéo de sortie. |
| `model.duration` | INT | Oui | 2 à 15 | Durée totale de sortie en secondes. Le modèle génère la suite pour combler le temps restant après le clip d'entrée. (par défaut : 5) |
| `first_clip` | VIDEO | Oui | - | Vidéo d'entrée à partir de laquelle continuer. Durée : 2s-10s. Le rapport hauteur/largeur de sortie est dérivé de cette vidéo. |
| `last_frame` | IMAGE | Non | - | Image de la dernière image. La suite effectuera une transition vers cette image. |
| `seed` | INT | Oui | 0 à 2147483647 | Graine à utiliser pour la génération. (par défaut : 0) |
| `prompt_extend` | BOOLEAN | Oui | - | Indique s'il faut améliorer l'invite avec l'assistance de l'IA. (par défaut : True) |
| `watermark` | BOOLEAN | Oui | - | Indique s'il faut ajouter un filigrane généré par l'IA au résultat. (par défaut : False) |

**Remarque :** La vidéo d'entrée `first_clip` doit avoir une durée comprise entre 2 et 10 secondes.

## Sorties

| Nom de la sortie | Type de données | Description |
| :--- | :--- | :--- |
| `output` | VIDEO | La suite vidéo générée. |

---
**Source fingerprint (SHA-256):** `5e9d2c7800603660f5f994d125e1e32f2b310234c4b6a24d502c764d91be49e8`
