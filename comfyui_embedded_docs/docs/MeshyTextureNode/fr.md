# Meshy : Modèle de texture

Le nœud Meshy : Texture applique des textures générées par IA à un modèle 3D. Il prend un identifiant de tâche (task ID) provenant d’un nœud précédent de génération ou de conversion 3D Meshy et utilise soit une description textuelle, soit une image de référence pour créer de nouvelles textures pour le modèle. Le nœud produit le modèle texturé aux formats de fichier GLB et FBX.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | La version du modèle IA à utiliser pour la texturation. | COMBO | Oui | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | L’identifiant unique (ID de tâche) d’une tâche précédente de génération ou de conversion 3D Meshy. Cela fournit le modèle 3D de base à texturer. | MESHY_TASK_ID | Oui | - |
| `activer_uv_original` | Utilisez les UV d’origine du modèle au lieu de générer de nouveaux UV. Lorsque cette option est activée (par défaut : `True`), Meshy conserve les textures existantes du modèle téléchargé. Si le modèle n’a pas d’UV d’origine, la qualité de la sortie pourrait être moindre. Il s’agit d’une option avancée. | BOOLEAN | Non | true / false |
| `pbr` | Active la sortie de matériaux à rendu physiquement réaliste (PBR) pour le modèle texturé (par défaut : `False`). Il s’agit d’une option avancée. | BOOLEAN | Non | true / false |
| `invite_style_texte` | Décrivez le style de texture souhaité pour l’objet à l’aide de texte. 600 caractères maximum. Ne peut pas être utilisé en même temps que `image_style`. | STRING | Non | - |
| `style_image` | Une image 2D pour guider le processus de texturation. Ne peut pas être utilisée en même temps que `text_style_prompt`. | IMAGE | Non | - |
| `texture_resolution` | Résolution de la texture de couleur de base. Les résolutions plus élevées capturent plus de détails de surface. | COMBO | Oui | `"2k"`<br>`"4k"`<br>`"8k"` |

**Contraintes des paramètres :**

* Vous devez fournir soit un `text_style_prompt`, soit une `image_style`, mais vous ne pouvez pas fournir les deux en même temps.
* Le `text_style_prompt` est limité à un maximum de 600 caractères.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `fichier_modèle` | Le nom de fichier du modèle GLB généré. Cette sortie est fournie uniquement pour la rétrocompatibilité. | STRING |
| `meshy_task_id` | L’identifiant de tâche unique pour ce travail de texturation, qui peut être utilisé pour référencer le résultat. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D texturé enregistré au format de fichier GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D texturé enregistré au format de fichier FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/fr.md)

---
**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`
