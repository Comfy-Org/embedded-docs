> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/fr.md)

Le nœud Kling Video Extend vous permet d'étendre des vidéos créées par d'autres nœuds Kling. Il prend une vidéo existante identifiée par son ID vidéo et génère un contenu supplémentaire basé sur vos invites textuelles. Le nœud fonctionne en envoyant votre demande d'extension à l'API Kling et renvoie la vidéo étendue avec son nouvel ID et sa durée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Non | - | Invite textuelle positive pour guider l'extension de la vidéo |
| `negative_prompt` | STRING | Non | - | Invite textuelle négative pour les éléments à éviter dans la vidéo étendue |
| `cfg_scale` | FLOAT | Non | 0.0 - 1.0 | Contrôle l'intensité de la guidance par l'invite (par défaut : 0.5) |
| `video_id` | STRING | Oui | - | L'ID de la vidéo à étendre. Prend en charge les vidéos générées par texte-vers-vidéo, image-vers-vidéo et les opérations d'extension vidéo précédentes. Ne peut pas dépasser 3 minutes de durée totale après extension. |

**Note :** Le `video_id` doit référencer une vidéo créée par d'autres nœuds Kling, et la durée totale après extension ne peut pas dépasser 3 minutes.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo étendue générée par l'API Kling |
| `video_id` | STRING | L'identifiant unique de la vidéo étendue |
| `duration` | STRING | La durée de la vidéo étendue |