# Fusionner les Splats

Le nœud Fusionner les Splats combine plusieurs modèles de splats gaussiens en un seul splat en concaténant leurs données. Ceci est utile pour fusionner plusieurs décodages d'un même latent généré avec différentes graines, ce qui peut densifier la surface et améliorer la qualité lors de la création de maillages 3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `splat0` | Premier splat gaussien à fusionner | SPLAT | Oui | Au moins 1 splat requis |
| `splat1` | Deuxième splat gaussien à fusionner | SPLAT | Oui | Au moins 1 splat requis |
| `splat2` | Splat gaussien supplémentaire à fusionner (optionnel) | SPLAT | Non | Jusqu'à 32 splats au total |
| `splat3` | Splat gaussien supplémentaire à fusionner (optionnel) | SPLAT | Non | Jusqu'à 32 splats au total |
| ... | Splats supplémentaires (jusqu'à splat31) | SPLAT | Non | Jusqu'à 32 splats au total |

**Remarque :** La liste d'entrées crée automatiquement de nouveaux emplacements au fur et à mesure que vous connectez des splats. Vous devez connecter au moins un splat. Le nœud accepte un minimum de 2 et un maximum de 32 splats.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `splat` | Le splat gaussien fusionné contenant tous les splats d'entrée concaténés ensemble | SPLAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeSplat/fr.md)

---
**Source fingerprint (SHA-256):** `597671a3c37d1a4fb7b5a772396e08b7041b3fe8f04120891b1382d42e409d26`
