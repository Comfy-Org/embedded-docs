# Tripo : Texte vers Modèle

Ce nœud hérité génère des modèles 3D finis à partir d'une description textuelle en utilisant l'API de Tripo. Il attend la fin de la génération, puis renvoie le fichier du modèle, avec éventuellement des textures et des matériaux PBR. Il est marqué comme obsolète et conservé pour les anciens workflows.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `invite` | Description textuelle du modèle 3D à générer (multiligne). Ce paramètre est obligatoire et ne peut pas être vide. | STRING | Oui | - |
| `invite_négative` | Description textuelle de ce qu'il faut éviter dans le modèle généré (multiligne). Jusqu'à 255 caractères. Envoyée à l'API uniquement lorsqu'elle n'est pas vide. | STRING | Non | Jusqu'à 255 caractères |
| `version_modèle` | Version du modèle Tripo à utiliser pour la génération (par défaut : v3_1_20260211). | COMBO | Non | Plusieurs options disponibles |
| `style` | N'est plus pris en charge par Tripo et est ignoré. Conservé pour les anciens workflows (par défaut : "None"). | COMBO | Non | Plusieurs options disponibles |
| `texture` | Génère des cartes de texture. Désactivé, renvoie une géométrie brute et ignore `pbr` (par défaut : True). | BOOLEAN | Non | true / false |
| `pbr` | Cartes de matériaux PBR (couleur de base, métallique, rugosité, normale). Nécessite `texture` ; désactivé de force lorsque `texture` est désactivé (par défaut : True). | BOOLEAN | Non | true / false |
| `graine_image` | Graine utilisée pour l'étape de génération d'image (par défaut : 42). | INT | Non | 0 à 2147483647 |
| `modèle_graine` | Graine utilisée pour l'étape de génération de modèle (par défaut : 42). | INT | Non | 0 à 2147483647 |
| `texture_graine` | Graine utilisée pour l'étape de génération de texture (par défaut : 42). | INT | Non | 0 à 2147483647 |
| `qualité_texture` | Qualité des textures générées. detailed = textures HD, extreme = textures Ultra 8K (par défaut : standard). | COMBO | Non | "standard"<br>"detailed"<br>"extreme" |
| `limite_visage` | Nombre maximal de faces. -1 laisse Tripo choisir de manière adaptative (environ 1,4 M de faces sur v3.x standard, 2 M sur detailed). Tripo plafonne silencieusement : les maillages quad à 150 000. (par défaut : -1) | INT | Non | -1 à 2000000 |
| `quad` | Sortie de maillage quad. Tripo livre les maillages quad au format FBX, donc le résultat arrive sur la sortie FBX et la sortie GLB reste vide. (par défaut : False) | BOOLEAN | Non | true / false |
| `geometry_quality` | Qualité de la géométrie générée (par défaut : standard). | COMBO | Non | "standard"<br>"detailed" |
| `smart_low_poly` | Maillage low-poly avec une topologie propre et de style artisanal (500 à 20 000 faces, quad 500 à 10 000). Idéal pour les sujets simples ; les sujets complexes peuvent échouer. (par défaut : False) | BOOLEAN | Non | true / false |
| `auto_size` | Met à l'échelle les modèles texturés à leur taille réelle en mètres. Tripo stocke la taille sous forme de transformation de scène du modèle et l'intègre lorsque le modèle est converti, riggé ou retargeté ; ignoré sans texture. (par défaut : True) | BOOLEAN | Non | true / false |

**Remarques :**
- Ce nœud est obsolète et marqué comme nœud hérité. Il est conservé pour la rétrocompatibilité avec les anciens workflows.
- Le paramètre `prompt` est obligatoire : un prompt vide provoque une erreur du nœud.
- `pbr` nécessite `texture`. Lorsque `texture` est désactivé, le nœud force la désactivation de `pbr` et ignore sa valeur. `auto_size` n'a également aucun effet sans `texture`.
- Lorsque `smart_low_poly` est activé et que `face_limit` est défini sur une valeur autre que -1, la limite de faces doit être comprise entre 500 et 20 000 pour une sortie triangle, ou entre 500 et 10 000 lorsque `quad` est activé ; sinon, le nœud lève une erreur.
- Lorsque `quad` est activé, le maillage quad généré est livré au format FBX, donc la sortie FBX est renseignée et la sortie GLB reste vide.
- Le paramètre `style` est accepté mais ignoré.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `fichier_modèle` | Nom de fichier du modèle 3D généré au format `<task_id>.<format>`, conservé uniquement pour la rétrocompatibilité. | STRING |
| `modèle task_id` | Identifiant unique de tâche pour le processus de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. Vide lorsque `quad` est activé. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format FBX. Renseigné uniquement lorsque `quad` est activé. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `c26c8437ea66d08f7f39865fedeaaf4cf8583ca64b368f3b767ea18918dd6c08`
