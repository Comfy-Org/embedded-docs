# Meshy: Texture Model (N1)

Ce nœud applique une texture à un modèle 3D créé précédemment avec le modèle de texturation Meshy N1, en utilisant 1 à 4 vues de référence du même objet. Connectez l’ID de tâche du modèle d’origine ainsi que les vues ; le nœud les envoie à Meshy, attend la fin de la tâche et renvoie le modèle texturé sous forme de fichiers GLB et FBX, accompagné du nouvel ID de tâche.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle d’IA utilisé pour la tâche de texturation. Seul `"meshy-n1"` est actuellement disponible. | COMBO | Oui | `"meshy-n1"` |
| `meshy_task_id` | ID de tâche du modèle 3D créé précédemment qui doit être texturé. | MESHY_TASK_ID | Oui | N/A |
| `front_view` | Vue que Meshy considère comme l’avant. Une seule image applique une texture à l’avant et laisse l’arrière uni ; ajoutez des vues arrière et latérales dans `extra_views` pour un arrière fidèle. | IMAGE | Oui | Image unique |
| `extra_views` | Vues supplémentaires du même objet, dans n’importe quel ordre. Emplacement extensible : connectez 0 à 3 images (`view_1` ... `view_3`). Avec `front_view`, 4 images au maximum au total. | IMAGE | Non | 0 à 3 images |
| `enable_original_uv` | Utiliser l’UV d’origine du modèle au lieu de générer de nouvelles UV. Lorsque cette option est activée, Meshy conserve les textures existantes du modèle téléversé. Si le modèle ne possède pas d’UV d’origine, la qualité de la sortie risque d’être moins bonne. (par défaut : True ; option avancée) | BOOLEAN | Non | True ou False |

**Remarque :** `front_view` et `extra_views` peuvent contenir ensemble au maximum 4 images ; le nœud génère une erreur lorsque davantage d’images sont connectées. Si une image connectée contient un lot, chaque image du lot compte dans cette limite. La résolution de texture est fixée à 2K et aucune carte PBR n’est générée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `meshy_task_id` | ID de tâche de la tâche de texturation, utilisable par les nœuds Meshy ultérieurs. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D texturé téléchargé au format GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D texturé téléchargé au format FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureN1Node/fr.md)

---
**Source fingerprint (SHA-256):** `808df4f5a32b2d9ca6e74668051409836f2fcbc078d4ee3e85c07121d7a81f76`
