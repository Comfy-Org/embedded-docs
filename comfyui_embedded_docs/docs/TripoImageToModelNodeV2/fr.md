# TripoImageToModelNodeV2

Le nœud Tripo: Image to Model transforme une seule image de référence en modèle 3D à l’aide du service de conversion image vers modèle de Tripo. Il téléverse l’image, soumet une tâche de génération, attend la fin de la tâche et renvoie le fichier 3D résultant ainsi que l’ID de tâche. Il s’agit d’un nœud API, il nécessite donc une clé d’API Comfy valide.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image de référence utilisée pour générer le modèle 3D. | IMAGE | Oui | — |
| `model_version` | Version du modèle à utiliser pour la génération. Si elle n’est pas définie, le nœud revient à la version v3.1 (20260211) de Tripo. | COMBO | Non | Liste des versions de modèle Tripo |
| `texture` | Générer les cartes de texture. Désactivé renvoie une géométrie nue et ignore `pbr` (par défaut : true). | BOOLEAN | Non | true<br>false |
| `pbr` | Cartes de matériau PBR (couleur de base, métallique, rugosité, normale). Nécessite `texture` (par défaut : true). | BOOLEAN | Non | true<br>false |
| `model_seed` | Graine utilisée pour l’étape de génération de la géométrie (par défaut : 42). | INT | Non | 0 à 2147483647 |
| `orientation` | Réglage d’orientation appliqué au modèle généré (par défaut : DEFAULT). | COMBO | Non | Options d’orientation Tripo, par défaut `DEFAULT` |
| `texture_seed` | Graine utilisée pour l’étape de génération de texture (par défaut : 42). | INT | Non | 0 à 2147483647 |
| `texture_quality` | detailed = textures HD, extreme = textures 8K Ultra (par défaut : "standard"). | COMBO | Non | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Comment les textures sont alignées sur la géométrie générée (par défaut : "original_image"). | COMBO | Non | "original_image"<br>"geometry" |
| `face_limit` | Nombre maximal de faces. -1 laisse Tripo choisir de manière adaptative (environ 1,4 M de faces sur v3.x standard, 2 M sur detailed). Tripo limite silencieusement : les maillages quad à 150 000 (par défaut : -1). | INT | Non | -1 à 2000000 |
| `quad` | Sortie de maillage quad. Tripo livre les maillages quad au format FBX, donc le résultat arrive sur la sortie FBX et la sortie GLB reste vide (par défaut : false). | BOOLEAN | Non | true<br>false |
| `geometry_quality` | Niveau de qualité de la géométrie générée (par défaut : "standard"). | COMBO | Non | "standard"<br>"detailed" |
| `smart_low_poly` | Maillage low-poly avec une topologie propre de style fait main (500-20 000 faces, quad 500-10 000). Idéal pour les sujets simples ; les sujets complexes peuvent échouer (par défaut : false). | BOOLEAN | Non | true<br>false |
| `auto_size` | Met à l’échelle les modèles texturés à leur taille réelle en mètres. Tripo stocke la taille comme transformation de scène du modèle et l’intègre lors de la conversion, du rigging ou du retargeting ; ignoré sans texture (par défaut : true). | BOOLEAN | Non | true<br>false |

**Remarques :**

- `image` est requis ; le nœud lève une erreur si aucune image n’est fournie.
- Lorsque `smart_low_poly` est activé et que `face_limit` est défini à une valeur autre que -1, la limite doit être comprise entre 500 et 20 000 pour les maillages triangulaires, ou entre 500 et 10 000 lorsque `quad` est activé. D’autres valeurs lèvent une erreur.
- Lorsque `texture` est désactivé, `pbr` est forcé désactivé quel que soit son réglage, et `auto_size` n’a aucun effet.
- Un `face_limit` de -1 est envoyé à Tripo comme "no limit", laissant le service choisir de manière adaptative.
- Un nouveau format de fichier 3D que le nœud ne peut pas renvoyer (autre que GLB ou FBX) provoque une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `model task_id` | L’ID de tâche Tripo de la tâche de génération. | MODEL_TASK_ID |
| `GLB` | Le modèle généré sous forme de fichier GLB. Vide lorsque `quad` est activé. | FILE3DGLB |
| `FBX` | Le modèle généré sous forme de fichier FBX. Rempli uniquement lorsque `quad` est activé. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `c8c069432f67a019995b9f4dedbf5ca3f7594ae4004104277068106821189c11`
