# Tripo : Multivue vers Modèle

Ce nœud génère des modèles 3D de manière synchrone en utilisant l'API de Tripo, en traitant jusqu'à quatre images montrant différentes vues d'un objet (face, gauche, arrière, droite). Il nécessite une image de face et au moins une vue supplémentaire (gauche, arrière ou droite) pour construire le modèle 3D. La texture, le matériau PBR, la qualité de la géométrie et le format de sortie peuvent être contrôlés depuis le nœud.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Image de vue de face de l'objet. | IMAGE | Oui | - |
| `image_gauche` | Image de vue de gauche de l'objet. | IMAGE | Non | - |
| `image_arrière` | Image de vue arrière de l'objet. | IMAGE | Non | - |
| `image_droite` | Image de vue de droite de l'objet. | IMAGE | Non | - |
| `version_modèle` | Version du modèle à utiliser pour la génération. | COMBO | Non | Plusieurs options disponibles |
| `orientation` | Réglage de l'orientation pour le modèle 3D (par défaut : `"default"`). | COMBO | Non | Plusieurs options disponibles |
| `texture` | Générer les cartes de texture. Désactivé, renvoie la géométrie brute et ignore `pbr`. (par défaut : True) | BOOLEAN | Non | - |
| `pbr` | Cartes de matériau PBR (couleur de base, métallique, rugosité, normale). Nécessite `texture`. (par défaut : True) | BOOLEAN | Non | - |
| `graine_modèle` | Graine aléatoire pour la génération du modèle (par défaut : 42). | INT | Non | 0 à 2,147,483,647 |
| `graine_texture` | Graine aléatoire pour la génération de texture (par défaut : 42). | INT | Non | 0 à 2,147,483,647 |
| `qualité_texture` | Niveau de qualité pour la génération de texture (par défaut : `"standard"`). `"detailed"` = textures HD, `"extreme"` = textures Ultra 8K. | COMBO | Non | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `alignement_texture` | Méthode utilisée pour aligner les textures sur le modèle (par défaut : `"original_image"`). | COMBO | Non | `"original_image"`<br>`"geometry"` |
| `limite_visage` | Nombre maximal de faces. -1 laisse Tripo choisir de manière adaptative (environ 1,4 M de faces sur v3.x standard, 2 M sur detailed). Tripo limite silencieusement : les maillages quad à 150 000. (par défaut : -1) | INT | Non | -1 à 2,000,000 |
| `quad` | Sortie de maillage quad. Tripo livre les maillages quad au format FBX, donc le résultat arrive sur la sortie FBX et la sortie GLB reste vide. (par défaut : False) | BOOLEAN | Non | - |
| `geometry_quality` | Niveau de qualité pour la génération de géométrie (par défaut : `"standard"`). | COMBO | Non | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Maillage low-poly avec une topologie propre, de style fait main (500 à 20 000 faces, quad 500 à 10 000). Idéal pour les sujets simples ; les sujets complexes peuvent échouer. (par défaut : False) | BOOLEAN | Non | - |
| `auto_size` | Redimensionne les modèles texturés à leur taille réelle en mètres. Tripo stocke la taille sous forme de transformation de scène du modèle et l'intègre lorsque le modèle est converti, riggé ou retargeté ; ignoré sans texture. (par défaut : False) | BOOLEAN | Non | - |

**Remarque :** L'image de face (`image`) est toujours requise, et au moins une parmi `image_left`, `image_back` ou `image_right` doit également être fournie. Désactiver `texture` désactive automatiquement `pbr` aussi, car `pbr` nécessite une texture. Lorsque `smart_low_poly` est activé et que `face_limit` n'est pas laissé à -1, `face_limit` doit être compris entre 500 et 20 000 pour les maillages triangulaires, ou entre 500 et 10 000 pour les maillages quad.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `fichier_modèle` | Chemin de fichier ou identifiant pour le modèle 3D généré (uniquement pour la compatibilité ascendante). | STRING |
| `modèle task_id` | Identifiant de tâche pour le suivi du processus de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Le fichier de modèle 3D généré au format GLB. Vide lorsque `quad` est activé. | FILE3DGLB |
| `FBX` | Le fichier de modèle 3D généré au format FBX. Rempli uniquement lorsque `quad` est activé. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `b66df4cad6167fa27edf1fe21b96cb47af90027b3fbe0a3c9c14101506281ed7`
