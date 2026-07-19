# Meshy : Modèle de texture

Le nœud Meshy : Texture applique des textures générées par IA à un modèle 3D. Il prend un identifiant de tâche provenant d'un nœud précédent de génération ou de conversion 3D Meshy et utilise soit une description textuelle, soit une image de référence pour créer de nouvelles textures pour le modèle. Le nœud produit le modèle texturé aux formats de fichier GLB et FBX.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | La version du modèle IA à utiliser pour la texturation. Actuellement, seule la version "latest" est disponible. | COMBO | Oui | `"latest"` |
| `meshy_task_id` | L'identifiant unique (ID de tâche) d'une tâche précédente de génération ou de conversion 3D Meshy. Cela fournit le modèle 3D de base à texturer. | MESHY_TASK_ID | Oui | - |
| `activer_uv_original` | Utiliser l'UV d'origine du modèle au lieu d'en générer de nouveaux. Lorsqu'il est activé (par défaut : `True`), Meshy préserve les textures existantes du modèle téléchargé. Si le modèle n'a pas d'UV d'origine, la qualité du résultat risque d'être moindre. | BOOLEAN | Non | - |
| `pbr` | Active la sortie de matériau basée sur le rendu physiquement réaliste (PBR) pour le modèle texturé (par défaut : `False`). | BOOLEAN | Non | - |
| `invite_style_texte` | Décrivez le style de texture souhaité pour l'objet à l'aide de texte. Maximum 600 caractères. Ne peut pas être utilisé en même temps que `style_image`. | STRING | Non | - |
| `style_image` | Une image 2D pour guider le processus de texturation. Ne peut pas être utilisé en même temps que `invite_style_texte`. | IMAGE | Non | - |

**Contraintes des paramètres :**

* Vous devez fournir soit un `text_style_prompt`, soit un `image_style`, mais vous ne pouvez pas fournir les deux en même temps.
* Le `text_style_prompt` est limité à un maximum de 600 caractères.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `fichier_modèle` | Le nom du fichier du modèle GLB généré. Cette sortie est fournie pour des raisons de compatibilité ascendante. | STRING |
| `meshy_task_id` | L'identifiant unique de la tâche pour ce travail de texturation, qui peut être utilisé pour référencer le résultat. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D texturé enregistré au format de fichier GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D texturé enregistré au format de fichier FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/fr.md)

---
**Source fingerprint (SHA-256):** `380b682a8290c69e71a204c8c3d6c2d4fb2c15f4bc1679b98c7fc4fd9ec9e1b3`
