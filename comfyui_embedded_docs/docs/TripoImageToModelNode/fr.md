# Tripo : Image vers Modèle

Génère des modèles 3D de manière synchrone à partir d'une seule image à l'aide de l'API de Tripo. Fournissez une image d'entrée, et le nœud crée un modèle 3D fini à partir de celle-ci, avec des contrôles facultatifs pour la version du modèle, la génération de textures, le niveau de détail et le format de sortie. Il s'agit de la version héritée du nœud image-to-model, conservée pour les anciens workflows.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée utilisée pour générer le modèle 3D. Une image doit être fournie, sinon le nœud lève une erreur. | IMAGE | Oui | - |
| `version_modèle` | Version du modèle à utiliser pour la génération. | COMBO | Non | `"v3.1-20260211"`<br>`"v3.0-20250812"` |
| `style` | N'est plus pris en charge par Tripo et est ignoré. Conservé pour les anciens workflows. (par défaut : `"None"`) | COMBO | Non | `"None"`<br>`"realistic"`<br>`"cartoon"`<br>`"sculpture"`<br>`"low_poly"` |
| `texture` | Génère des cartes de texture. Désactivé, renvoie une géométrie brute et ignore `pbr`. (par défaut : True) | BOOLEAN | Non | True<br>False |
| `pbr` | Cartes de matériau PBR (couleur de base, métallique, rugosité, normale). Nécessite `texture`. (par défaut : True) | BOOLEAN | Non | True<br>False |
| `graine_modèle` | Graine aléatoire pour la génération du modèle. (par défaut : 42) | INT | Non | 0 à 2147483647 |
| `orientation` | Paramètre d'orientation du modèle généré. (par défaut : `"default"`) | COMBO | Non | `"default"`<br>`"front"`<br>`"back"`<br>`"left"`<br>`"right"`<br>`"top"`<br>`"bottom"` |
| `graine_texture` | Graine aléatoire pour la génération de la texture. (par défaut : 42) | INT | Non | 0 à 2147483647 |
| `qualité_texture` | Niveau de qualité pour la génération de texture : `detailed` = textures HD, `extreme` = textures ultra 8K. (par défaut : `"standard"`) | COMBO | Non | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `alignement_texture` | Méthode d'alignement pour le mappage de texture. (par défaut : `"original_image"`) | COMBO | Non | `"original_image"`<br>`"geometry"` |
| `limite_faces` | Nombre maximal de faces. -1 laisse Tripo choisir de manière adaptative (environ 1,4 M de faces sur v3.x standard, 2 M sur detailed). Tripo plafonne silencieusement : les maillages quad à 150 000. (par défaut : -1) | INT | Non | -1 à 2000000 |
| `quad` | Sortie de maillage quad. Tripo fournit les maillages quad au format FBX, donc le résultat arrive sur la sortie FBX et la sortie GLB reste vide. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `geometry_quality` | Niveau de qualité pour la génération de la géométrie. (par défaut : `"standard"`) | COMBO | Non | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Maillage low-poly avec une topologie propre de style artisanal (500 à 20 000 faces, quad 500 à 10 000). Idéal pour les sujets simples ; les sujets complexes peuvent échouer. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `auto_size` | Met à l'échelle les modèles texturés à leur taille réelle en mètres. Tripo stocke la taille comme transformation de scène du modèle et l'intègre lorsque le modèle est converti, riggé ou retargeté ; ignoré en l'absence de texture. (par défaut : True) | BOOLEAN | Non | True<br>False |

Remarque : une `image` est requise ; si elle est absente, le nœud lève une RuntimeError. Lorsque `texture` est False, le modèle contient uniquement une géométrie brute et `pbr` est forcé à False. Lorsque `smart_low_poly` est activé, `face_limit` doit être compris entre 500 et 20 000 pour les maillages triangulaires, ou entre 500 et 10 000 lorsque `quad` est également activé ; si la limite est invalide, le nœud lève une ValueError. Définir `face_limit` sur -1 (valeur par défaut) n'envoie aucune limite de faces explicite à l'API, ce qui laisse Tripo choisir de manière adaptative.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `fichier_modèle` | Le fichier de modèle 3D généré (uniquement pour la rétrocompatibilité). | STRING |
| `modèle task_id` | L'ID de tâche pour le suivi du processus de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. Vide lorsque `quad` est activé. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format FBX. Rempli uniquement lorsque `quad` est activé. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `3b278abfd13329ee58ebab1bfeb47d32d09f4797f3d8628a35a028c3d15a7314`
