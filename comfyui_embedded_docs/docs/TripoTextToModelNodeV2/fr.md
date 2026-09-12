# TripoTextToModelNodeV2

Génère un modèle 3D à partir d'une description textuelle en utilisant le service Tripo. Ce nœud envoie le prompt et les paramètres à Tripo, attend la fin de la tâche de génération, puis renvoie le fichier 3D terminé accompagné de l'identifiant de la tâche.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description textuelle du modèle à générer. Ne doit pas être vide. | STRING | Oui | Texte multiligne |
| `negative_prompt` | Texte décrivant ce qui ne doit pas apparaître dans le modèle généré. Jusqu'à 255 caractères. | STRING | Non | Texte multiligne, max 255 caractères |
| `model_version` | Version du modèle Tripo utilisée pour la génération (par défaut : `v3.1_20260211`). | COMBO | Non | Liste des versions de modèle Tripo prises en charge |
| `texture` | Générer les textures. Désactivé, renvoie la géométrie brute et ignore `pbr` (par défaut : True). | BOOLEAN | Non | True<br>False |
| `pbr` | Cartes de matériaux PBR (couleur de base, métallique, rugosité, normale). Nécessite `texture` (par défaut : True). | BOOLEAN | Non | True<br>False |
| `image_seed` | Valeur de graine pour la génération d'image (par défaut : 42). | INT | Non | 0 à 2147483647 |
| `model_seed` | Valeur de graine pour la génération du modèle (par défaut : 42). | INT | Non | 0 à 2147483647 |
| `texture_seed` | Valeur de graine pour la génération de texture (par défaut : 42). | INT | Non | 0 à 2147483647 |
| `texture_quality` | Niveau de détail des textures (par défaut : "standard"). "detailed" = textures HD, "extreme" = textures 8K Ultra. | COMBO | Non | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `face_limit` | Nombre maximal de faces. -1 laisse Tripo choisir de manière adaptative (environ 1,4 M de faces en v3.x standard, 2 M en detailed). Tripo limite silencieusement : v2.5 à 500 000, maillages quad à 150 000 (par défaut : -1). | INT | Non | -1 à 2000000 |
| `quad` | Sortie en maillage quad. Tripo livre les maillages quad au format FBX, le résultat arrive donc sur la sortie FBX et la sortie GLB reste vide (par défaut : False). | BOOLEAN | Non | True<br>False |
| `geometry_quality` | Niveau de détail de la géométrie (par défaut : "standard"). | COMBO | Non | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Maillage low-poly avec une topologie propre de style artisanal (500-20 000 faces, quad 500-10 000). Idéal pour les sujets simples ; les sujets complexes peuvent échouer (par défaut : False). | BOOLEAN | Non | True<br>False |
| `auto_size` | Met à l'échelle les modèles texturés à leur taille réelle en mètres. Tripo stocke la taille comme transformation de scène du modèle et l'intègre lors de la conversion, du rigging ou du retargeting du modèle ; ignoré sans texture (par défaut : True). | BOOLEAN | Non | True<br>False |

### Notes

- `prompt` est requis et ne peut pas être vide ni contenir uniquement des espaces.
- Lorsque `texture` est défini sur False, `pbr` est forcé à l'arrêt et `auto_size` n'a aucun effet.
- Lorsque `smart_low_poly` est activé et que `face_limit` n'est pas -1, `face_limit` doit être compris entre 500 et 20 000 pour les maillages triangulaires, ou entre 500 et 10 000 lorsque `quad` est activé.
- Lorsque `quad` est activé, Tripo renvoie un fichier FBX ; la sortie `GLB` reste donc vide et la sortie `FBX` est remplie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model task_id` | Identifiant de la tâche de génération Tripo ayant produit le modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle généré au format GLB. Vide lorsque `quad` est activé. | FILE3D_GLB |
| `FBX` | Le modèle généré au format FBX. Rempli uniquement lorsque `quad` est activé. | FILE3D_FBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `8af7044188c6dbb87d23298bf7b99fe826bdc7bd7ba0948db2066887274faa00`
