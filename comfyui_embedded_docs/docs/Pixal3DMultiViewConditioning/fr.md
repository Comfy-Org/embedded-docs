# Pixal3D Conditionnement multi-vues

Le nœud Pixal3D Multi-View Conditioning construit des données de conditionnement à partir d’un rig de caméra à orbite fixe : vues avant, gauche, arrière et droite placées à 90 degrés d’écart, utilisées exactement telles qu’elles sont cadrées. Connectez au moins une vue carrée de l’objet et il prépare un conditionnement positif et négatif correspondant pour les modèles Pixal3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision avec poids NAF intégrés. | CLIP_VISION | Oui | N/A |
| `fov` | FOV horizontal en degrés des vues telles qu’elles sont cadrées : 20 pour les rendus de rig et la plupart des générateurs multi-vues, ou MoGeGeometryToFOV sur l’une des vues pour les photos. Par défaut : 20.0. | FLOAT | Oui | 1.0 - 170.0 |
| `front` | Vue carrée du côté avant de l’objet, avec canal alpha ou sur fond noir, cadrée comme le rig : l’objet occupe environ 1/1.1 de la largeur de l’image à son point le plus large, à la même échelle dans chaque vue. La première vue connectée (dans l’ordre avant, gauche, arrière, droite) est l’avant vers lequel le maillage est orienté. | IMAGE | Non | N/A |
| `left` | Vue carrée du côté gauche de l’objet, avec canal alpha ou sur fond noir, cadrée comme le rig : l’objet occupe environ 1/1.1 de la largeur de l’image à son point le plus large, à la même échelle dans chaque vue. La première vue connectée (dans l’ordre avant, gauche, arrière, droite) est l’avant vers lequel le maillage est orienté. | IMAGE | Non | N/A |
| `back` | Vue carrée du côté arrière de l’objet, avec canal alpha ou sur fond noir, cadrée comme le rig : l’objet occupe environ 1/1.1 de la largeur de l’image à son point le plus large, à la même échelle dans chaque vue. La première vue connectée (dans l’ordre avant, gauche, arrière, droite) est l’avant vers lequel le maillage est orienté. | IMAGE | Non | N/A |
| `right` | Vue carrée du côté droit de l’objet, avec canal alpha ou sur fond noir, cadrée comme le rig : l’objet occupe environ 1/1.1 de la largeur de l’image à son point le plus large, à la même échelle dans chaque vue. La première vue connectée (dans l’ordre avant, gauche, arrière, droite) est l’avant vers lequel le maillage est orienté. | IMAGE | Non | N/A |

### Remarques

- Au moins une vue doit être connectée ; le nœud lève une erreur si les quatre entrées de vue sont vides.
- La première vue connectée, dans l’ordre avant, gauche, arrière, droite, est traitée comme l’avant, et le maillage est orienté vers cette vue. Si la première vue connectée n’est pas `front`, un avertissement est consigné indiquant que le maillage sera orienté avec cette vue comme avant.
- Les vues sont lues dans l’ordre avant, gauche, arrière, droite et sont placées sur l’orbite à leurs azimuts fixes par rapport à la première vue connectée.
- Les vues d’entrée avec un canal alpha voient leur canal alpha appliqué sur du noir. Les vues qui ne sont pas en 1024 x 1024 sont redimensionnées en 1024 x 1024.
- La taille de lot est reprise de la première vue connectée. Si les vues connectées ont des tailles de lot différentes, les plus petites sont répétées en boucle pour correspondre.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | La sortie de conditionnement positive, construite à partir des vues encodées et de leurs caractéristiques projetées. | CONDITIONING |
| `negative` | La sortie de conditionnement négative, construite à partir d’embeddings mis à zéro avec les mêmes caractéristiques projetées. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`
