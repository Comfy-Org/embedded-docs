# TripoSmartSegmentNode

Divise un modèle 3D en parties sémantiquement significatives et donne un nom à chaque partie. Il peut soit segmenter un modèle existant (fourni via un ID de tâche), soit générer d'abord un modèle à partir d'une image, puis le segmenter. Le `segment task_id` résultant peut être utilisé par d'autres nœuds Tripo, tels que Complete Mesh Parts, Retopology, Texture model et Convert model, de la même manière qu'un résultat Tripo: Segment Model.

<Note>
Tripo conserve les enregistrements de tâches sur ses serveurs pendant 7 jours (à compter du 1er décembre 2026). Un ID de tâche plus ancien ne peut plus être résolu, donc relancer un workflow enregistré après ce délai échoue sur ce nœud. Pour continuer, relancez le nœud Tripo précédent pour créer un nouvel ID de tâche, ou réimportez le modèle que vous avez déjà téléchargé avec **Tripo : Importer un modèle**.
</Note>

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `source` | Segmenter un modèle existant, ou générer un modèle à partir d'une image puis le segmenter. L'option sélectionnée détermine quelles entrées supplémentaires apparaissent. | DYNAMIC_COMBO | Oui | `"model"`<br>`"image"` |

### Entrées du modèle

Affichées lorsque `source` est défini sur `"model"`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model_task_id` | Un résultat GLB. Les maillages quad (FBX) doivent d'abord passer par Tripo: Convert model (GLTF). | MODEL_TASK_ID | Oui | - |
| `granularity` | Niveau de finesse de la découpe du modèle en parties (par défaut : "medium"). | COMBO | Non | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | Texte facultatif nommant les parties à rechercher, par ex. 'personnage de jeu avec épée et armure' (par défaut : vide). | STRING | Non | - |

### Entrées d'image

Affichées lorsque `source` est défini sur `"image"`. Tripo génère d'abord un modèle à partir de l'image, puis le segmente.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `image` | L'image utilisée pour générer le modèle qui sera segmenté. | IMAGE | Oui | - |
| `granularity` | Niveau de finesse de la découpe du modèle en parties (par défaut : "medium"). | COMBO | Non | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | Texte facultatif nommant les parties à rechercher, par ex. 'personnage de jeu avec épée et armure' (par défaut : vide). | STRING | Non | - |

**Remarques :**

- `granularity` et `hint` sont partagés par les deux options de `source` et sont facultatifs. Lorsque `hint` est laissé vide, aucun indice n'est envoyé au service.
- Lorsque `source` vaut `"model"`, seuls les modèles GLB sont acceptés. Les autres formats, tels que les maillages quad (FBX), doivent d'abord être convertis avec Tripo: Convert model (GLTF).
- La tâche est interrogée périodiquement jusqu'à ce qu'elle atteigne un état final, avec une durée estimée d'environ 180 secondes. Si Tripo renvoie un résultat de segmentation incomplet, le nœud signale une erreur.
- Badge de prix : environ 0,85 USD lorsque `source` vaut `"image"` et environ 0,55 USD lorsque `source` vaut `"model"` (valeurs affichées à titre approximatif).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `segment task_id` | ID de tâche de la tâche de segmentation, utilisable comme entrée pour d'autres nœuds Tripo. | SEGMENT_TASK_ID |
| `model task_id` | Le modèle qui a été segmenté (généré à partir de l'image, ou importé). | MODEL_TASK_ID |
| `GLB` | Le fichier de modèle 3D segmenté. | FILE3DGLB |
| `part_names` | Noms des parties séparés par des virgules. | STRING |
| `parts` | Description par Tripo des parties trouvées. | STRING |
| `mask` | Image de masque produite par la segmentation. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartSegmentNode/fr.md)

---
**Source fingerprint (SHA-256):** `ba041da49e20b1ac085770078cce6ac87ef70eee927ba0ee9e5655a058893f1c`
