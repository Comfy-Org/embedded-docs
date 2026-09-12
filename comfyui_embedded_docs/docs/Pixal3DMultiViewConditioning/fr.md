# Pixal3DMultiViewConditioning

## Aperçu

Le nœud Pixal3D Multi-View Conditioning est un cadre d'orbitation fixe qui génère des vues avant, gauche, arrière et droite d'un objet à des intervalles de 90 degrés. Il est utilisé pour créer des vues encadrées pour les applications Pixal3D, où l'objet occupe environ 1/1.1 de la frame à son plus large, en maintenant la même échelle dans chaque vue.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision avec des poids NAF inclus. | MODEL | Oui | N/A |
| `fov` | Champ de vision horizontal en degrés des vues encadrées. | FLOAT | Oui | 1.0 - 170.0 |
| `front` | Vue carrée du côté avant de l'objet, avec alpha ou sur un fond noir. | IMAGE | Non | N/A |
| `left` | Vue carrée du côté gauche de l'objet, avec alpha ou sur un fond noir. | IMAGE | Facultatif | N/A |
| `back` | Vue carrée du côté arrière de l'objet, avec alpha ou sur un fond noir. | IMAGE | Facultatif | N/A |
| `right` | Vue carrée du côté droit de l'objet, avec alpha ou sur un fond noir. | IMAGE | Facultatif | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `positive` | La sortie de conditionnement positive pour le nœud Pixal3D Multi-View Conditioning. | CONDITIONING |
| `negative` | La sortie de conditionnement négative pour le nœud Pixal3D Multi-View Conditioning. | CONDITIONING |

## Notes

- Le paramètre `fov` contrôle le champ de vision horizontal des vues encadrées. Une valeur de 20 degrés est typique pour les rendus de cadre et la plupart des générateurs de vue multi-vues.
- La première vue connectée (avant, gauche, arrière, droite dans cet ordre) est considérée comme la vue avant, et le maillage est posé pour cette vue.
- Si aucune vue avant n'est fournie, un avertissement est enregistré, et le maillage sera posé avec la première vue connectée comme sa vue avant.
- Le nœud suppose que les vues sont carrées et encadrées comme le cadre. L'objet devrait occuper environ 1/1.1 de la frame à son plus large, et la même échelle devrait être maintenue dans chaque vue.
- Le nœud produit deux objets de conditionnement, l'un pour le conditionnement positif et l'autre pour le conditionnement négatif. Ces derniers peuvent être utilisés pour conditionner des modèles Pixal3D ou d'autres nœuds qui acceptent des entrées de conditionnement.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`
