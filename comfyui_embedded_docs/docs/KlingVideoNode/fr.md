Ce nœud génère des vidéos à l'aide du modèle Kling V3. Il prend en charge deux modes principaux : le texte-vers-vidéo, où une vidéo est créée à partir d'une description textuelle, et l'image-vers-vidéo, où une image existante est animée. Il offre également des fonctionnalités avancées comme la création de vidéos multi-segments avec des invites différentes pour chaque partie (storyboards) et la génération facultative d'un son d'accompagnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `multi_shot` | Contrôle s'il faut générer une seule vidéo ou une série de segments avec des invites et des durées individuelles. Lorsqu'il n'est pas réglé sur "disabled", des entrées supplémentaires pour l'invite et la durée de chaque storyboard apparaissent. | COMBO | Oui | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `générer audio` | Lorsqu'il est activé, le nœud génère un son pour la vidéo. La valeur par défaut est `True`. | BOOLEAN | Oui | `True` / `False` |
| `modèle` | Le modèle et ses paramètres associés. La sélection de cette option révèle les sous-paramètres `resolution` et `aspect_ratio`. | COMBO | Oui | `"kling-v3"` |
| `model.resolution` | La résolution de la vidéo générée. Ce paramètre est disponible lorsque le `modèle` est réglé sur "kling-v3". | COMBO | Oui | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | Le rapport hauteur/largeur de la vidéo générée. Ce paramètre est ignoré lorsqu'une image est fournie pour `image de départ` (mode image-vers-vidéo). Disponible lorsque le `modèle` est réglé sur "kling-v3". | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `seed` | Une valeur de graine pour la génération. La modification de cette valeur entraînera la réexécution du nœud, mais les résultats ne sont pas déterministes. La valeur par défaut est `0`. | INT | Oui | 0 à 2147483647 |
| `image de départ` | Une image de départ facultative. Lorsqu'elle est connectée, le nœud passe du mode texte-vers-vidéo au mode image-vers-vidéo, animant l'image fournie. | IMAGE | Non | - |

**Entrées pour le mode `multi_shot` :**

* Lorsque `multi_shot` est réglé sur **"disabled"**, les entrées suivantes apparaissent :
  * `prompt` (STRING) : La description textuelle principale de la vidéo. Requis. Doit contenir entre 1 et 2500 caractères.
  * `negative_prompt` (STRING) : Texte décrivant ce qui ne doit pas apparaître dans la vidéo. Facultatif.
  * `duration` (INT) : La durée de la vidéo en secondes. Doit être comprise entre 3 et 15. La valeur par défaut est `5`.
* Lorsque `multi_shot` est réglé sur une option de storyboard (par exemple, `"3 storyboards"`), des entrées pour chaque segment de storyboard apparaissent (par exemple, `storyboard_1_prompt`, `storyboard_1_duration`). Chaque invite doit contenir entre 1 et 512 caractères. La **somme totale de toutes les durées des storyboards** doit être comprise entre 3 et 15 secondes.

**Contraintes :**

* Le nœud fonctionne en mode **texte-vers-vidéo** lorsque `start_frame` n'est pas connecté. Il utilise le paramètre `model.aspect_ratio` dans ce mode.
* Le nœud fonctionne en mode **image-vers-vidéo** lorsque `start_frame` est connecté. Le paramètre `model.aspect_ratio` est ignoré. L'image d'entrée doit mesurer au moins 300x300 pixels et avoir un rapport hauteur/largeur compris entre 1:2,5 et 2,5:1.
* En mode storyboard (`multi_shot` n'est pas "disabled"), les entrées principales `prompt` et `negative_prompt` sont masquées et non utilisées.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `f7f827d657b1d057d273eba3215ce6848d3ea05c5f348e2f3fccccfdd030dfc3`
