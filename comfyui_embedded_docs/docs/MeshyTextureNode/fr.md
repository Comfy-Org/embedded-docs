# Meshy : Modèle de texture

Le nœud Meshy: Texture Model applique des textures générées par IA à un modèle 3D existant. Il utilise un ID de tâche provenant d'une précédente tâche Meshy de génération ou de conversion 3D et guide le processus de texturation avec soit un prompt de style textuel, soit une image de référence. Le nœud renvoie le modèle texturé aux formats de fichier GLB et FBX.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Version du modèle IA à utiliser pour la texturation. | COMBO | Oui | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | Identifiant unique (ID de tâche) provenant d'une précédente tâche Meshy de génération ou de conversion 3D. Fournit le modèle 3D de base à texturer. | MESHY_TASK_ID | Oui | - |
| `activer_uv_original` | Utiliser l'UV d'origine du modèle au lieu de générer de nouveaux UV. Lorsque cette option est activée (valeur par défaut : `True`), Meshy préserve les textures existantes du modèle téléversé. Si le modèle n'a pas d'UV d'origine, la qualité de la sortie risque de ne pas être aussi bonne. Il s'agit d'une option avancée. | BOOLEAN | Oui | true / false |
| `pbr` | Active la sortie de matériau PBR (rendu basé sur la physique) pour le modèle texturé (valeur par défaut : `False`). Il s'agit d'une option avancée. | BOOLEAN | Oui | true / false |
| `invite_style_texte` | Décrivez le style de texture souhaité pour l'objet à l'aide de texte (valeur par défaut : chaîne vide). Maximum 600 caractères. Ce paramètre ne peut pas être utilisé en même temps que `image_style`. | STRING | Oui | - |
| `style_image` | Une image 2D pour guider le processus de texturation. Ne peut pas être utilisée en même temps que `text_style_prompt`. | IMAGE | Non | - |
| `texture_resolution` | Résolution de la texture de couleur de base. Des résolutions plus élevées capturent davantage de détails de surface. | COMBO | Oui | `"2k"`<br>`"4k"`<br>`"8k"` |

**Contraintes des paramètres :**

* Vous devez fournir soit un `text_style_prompt`, soit un `image_style`, mais vous ne pouvez pas fournir les deux en même temps.
* Le `text_style_prompt` est limité à un maximum de 600 caractères.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model_file` | Nom du fichier du modèle GLB généré. Cette sortie est fournie uniquement pour des raisons de compatibilité ascendante. | STRING |
| `meshy_task_id` | Identifiant unique de tâche pour cette tâche de texturation, qui peut être utilisé pour référencer le résultat. | MESHY_TASK_ID |
| `GLB` | Le modèle 3D texturé enregistré au format de fichier GLB. | FILE3DGLB |
| `FBX` | Le modèle 3D texturé enregistré au format de fichier FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/fr.md)

---
**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`
