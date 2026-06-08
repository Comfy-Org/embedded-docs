Voici la traduction en français de la documentation du nœud Wan2VideoContinuation :

Le nœud Wan 2.7 Video Continuation génère un nouveau segment vidéo qui se poursuit de manière transparente à partir de la fin d'un clip vidéo d'entrée. Il utilise le modèle Wan 2.7 pour synthétiser la suite en fonction d'une invite textuelle et peut éventuellement guider la fin vers une image cible spécifique.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de génération vidéo à utiliser. | COMBO | Oui | `"wan2.7-i2v"` |
| `model.prompt` | Invite décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois. (par défaut : chaîne vide) | STRING | Oui | - |
| `model.negative_prompt` | Invite négative décrivant ce qu'il faut éviter. (par défaut : chaîne vide) | STRING | Oui | - |
| `model.resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `model.duration` | Durée totale de sortie en secondes. Le modèle génère la suite pour combler le temps restant après le clip d'entrée. (par défaut : 5) | INT | Oui | 2 à 15 |
| `premier clip` | Vidéo d'entrée à partir de laquelle continuer. Durée : 2s-10s. Le rapport hauteur/largeur de sortie est dérivé de cette vidéo. | VIDEO | Oui | - |
| `dernière image` | Image de la dernière image. La suite effectuera une transition vers cette image. | IMAGE | Non | - |
| `graine` | Graine à utiliser pour la génération. (par défaut : 0) | INT | Oui | 0 à 2147483647 |
| `extension d'invite` | Indique s'il faut améliorer l'invite avec l'assistance de l'IA. (par défaut : True) | BOOLEAN | Oui | - |
| `filigrane` | Indique s'il faut ajouter un filigrane généré par l'IA au résultat. (par défaut : False) | BOOLEAN | Oui | - |

**Remarque :** La vidéo d'entrée `first_clip` doit avoir une durée comprise entre 2 et 10 secondes.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La suite vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/fr.md)

---
**Source fingerprint (SHA-256):** `5e9d2c7800603660f5f994d125e1e32f2b310234c4b6a24d502c764d91be49e8`
