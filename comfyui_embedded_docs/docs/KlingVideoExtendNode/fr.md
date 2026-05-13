> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/fr.md)

Voici la traduction de la documentation du nœud Kling Video Extend Node :

Le nœud Kling Video Extend vous permet de prolonger des vidéos créées par d'autres nœuds Kling. Il prend une vidéo existante identifiée par son ID vidéo et génère du contenu supplémentaire basé sur vos invites textuelles. Le nœud fonctionne en envoyant votre demande de prolongation à l'API Kling et renvoie la vidéo prolongée avec son nouvel ID et sa durée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Non | - | Invite textuelle positive pour guider la prolongation de la vidéo |
| `negative_prompt` | STRING | Non | - | Invite textuelle négative pour les éléments à éviter dans la vidéo prolongée |
| `cfg_scale` | FLOAT | Non | 0.0 - 1.0 | Contrôle la force du guidage par l'invite (par défaut : 0.5) |
| `video_id` | STRING | Oui | - | L'ID de la vidéo à prolonger. Prend en charge les vidéos générées par texte-vers-vidéo, image-vers-vidéo et les opérations de prolongation vidéo précédentes. La durée totale après prolongation ne peut pas dépasser 3 minutes. |

**Remarque :** Le `video_id` doit faire référence à une vidéo créée par d'autres nœuds Kling, et la durée totale après prolongation ne peut pas dépasser 3 minutes.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `video_id` | VIDEO | La vidéo prolongée générée par l'API Kling |
| `duration` | STRING | L'identifiant unique de la vidéo prolongée |
| `duration` | STRING | La durée de la vidéo prolongée |

---
**Source fingerprint (SHA-256):** `ecef4aedffe83bf384f2f9c3d8840f3fcab4b8c21e6e9afb36e177abb6f069fd`
