> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/fr.md)

Ce nœud génère des vidéos en utilisant le modèle Kling V3. Il prend en charge deux modes principaux : le texte-à-vidéo, où une vidéo est créée à partir d'une description textuelle, et l'image-à-vidéo, où une image existante est animée. Il offre également des fonctionnalités avancées comme la création de vidéos multi-segments avec des prompts différents pour chaque partie (storyboards) et la génération optionnelle d'un audio d'accompagnement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `multi_shot` | COMBO | Oui | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | Contrôle s'il faut générer une vidéo unique ou une série de segments avec des prompts et durées individuelles. Lorsqu'il n'est pas sur "disabled", des entrées supplémentaires pour le prompt et la durée de chaque storyboard apparaissent. |
| `generate_audio` | BOOLEAN | Oui | `True` / `False` | Lorsqu'activé, le nœud générera un audio pour la vidéo. La valeur par défaut est `True`. |
| `model` | COMBO | Oui | `"kling-v3"` | Le modèle et ses paramètres associés. Sélectionner cette option révèle les sous-paramètres `resolution` et `aspect_ratio`. |
| `model.resolution` | COMBO | Oui | `"1080p"`<br>`"720p"` | La résolution pour la vidéo générée. Ce paramètre est disponible lorsque `model` est défini sur "kling-v3". |
| `model.aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Le format d'image pour la vidéo générée. Ce paramètre est ignoré lorsqu'une image est fournie pour `start_frame` (mode image-à-vidéo). Disponible lorsque `model` est défini sur "kling-v3". |
| `seed` | INT | Oui | 0 à 2147483647 | Une valeur de seed pour la génération. Changer cette valeur forcera le nœud à s'exécuter à nouveau, mais les résultats ne sont pas déterministes. La valeur par défaut est `0`. |
| `start_frame` | IMAGE | Non | - | Une image de départ optionnelle. Lorsqu'elle est connectée, le nœud passe du mode texte-à-vidéo au mode image-à-vidéo, animant l'image fournie. |

**Entrées pour le mode `multi_shot` :**
*   Lorsque `multi_shot` est défini sur **"disabled"**, les entrées suivantes apparaissent :
    *   `prompt` (STRING) : La description textuelle principale pour la vidéo. Requise. Doit contenir entre 1 et 2500 caractères.
    *   `negative_prompt` (STRING) : Texte décrivant ce qui ne doit pas apparaître dans la vidéo. Optionnel.
    *   `duration` (INT) : La longueur de la vidéo en secondes. Doit être comprise entre 3 et 15. La valeur par défaut est `5`.
*   Lorsque `multi_shot` est défini sur une option de storyboard (par ex., `"3 storyboards"`), des entrées pour chaque segment de storyboard apparaissent (par ex., `storyboard_1_prompt`, `storyboard_1_duration`). Chaque prompt doit contenir entre 1 et 512 caractères. **La somme totale de toutes les durées des storyboards** doit être comprise entre 3 et 15 secondes.

**Contraintes :**
*   Le nœud fonctionne en mode **texte-à-vidéo** lorsque `start_frame` n'est pas connecté. Il utilise le paramètre `model.aspect_ratio` dans ce mode.
*   Le nœud fonctionne en mode **image-à-vidéo** lorsque `start_frame` est connecté. Le paramètre `model.aspect_ratio` est ignoré. L'image d'entrée doit mesurer au moins 300x300 pixels et avoir un format d'image compris entre 1:2.5 et 2.5:1.
*   En mode storyboard (`multi_shot` différent de "disabled"), les entrées principales `prompt` et `negative_prompt` sont masquées et non utilisées.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | Le fichier vidéo généré. |