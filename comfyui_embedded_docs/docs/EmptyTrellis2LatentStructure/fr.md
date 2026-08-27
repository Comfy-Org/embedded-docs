# EmptyTrellis2LatentStructure

Ce nœud crée une structure latente vide pour le modèle Trellis2, où toutes les valeurs sont définies sur zéro. Il produit un tenseur latent 3D vierge avec 32 canaux à une résolution de 16×16×16, dimensionné pour le nombre d’éléments spécifié dans le lot.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `batch_size` | Le nombre d’images latentes dans le lot (défaut : 1). | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `LATENT` | Une structure latente Trellis2 vide. Les échantillons sont un tenseur rempli de zéros avec la forme (batch_size, 32, 16, 16, 16), et le type de latent est défini sur « trellis2 ». | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/fr.md)

---
**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`
