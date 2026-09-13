# Post-traitement Marigold V2

Ce nœud convertit une prédiction Marigold V2 décodée en une image affichable. Il prend le tenseur de prédiction brut et le formate selon le type de prédiction : profondeur normalisée (les objets proches apparaissent clairs), normales de surface de longueur unitaire, ou albédo sRGB.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | La prédiction Marigold V2 décodée à convertir en image affichable. | IMAGE | Oui | - |
| `prediction` | Le type de prédiction contenu dans l'entrée, qui détermine la façon dont les données sont converties. `"depth"` normalise les valeurs de profondeur de sorte que les surfaces proches soient claires et les surfaces éloignées sombres, puis copie le résultat dans les trois canaux de couleur. `"normals"` remet les valeurs à l'échelle sur la plage -1..1, les normalise en normales de surface de longueur unitaire, puis les ramène à 0..1. `"albedo"` applique une conversion linéaire vers sRGB aux valeurs. | COMBO | Oui | `"depth"`<br>`"normals"`<br>`"albedo"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image traitée dans la représentation sélectionnée : profondeur normalisée (niveaux de gris répétés sur les trois canaux), normales de surface de longueur unitaire, ou albédo sRGB. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MarigoldV2PostProcess/fr.md)

---
**Source fingerprint (SHA-256):** `848b29e2dfcd34c44cf9707b9b26cb13c18e82bb16618a15afbe477a1d620e1e`
