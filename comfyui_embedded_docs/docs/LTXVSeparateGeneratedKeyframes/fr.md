# LTXV Séparer les images clés générées

## Aperçu

Le nœud LTXV Separate Generated Keyframes extrait les images clés générées ajoutées par LTXV Add Generated Keyframes d’un latent échantillonné et les retire du conditionnement. Utilisez-le avant de suréchantillonner spatialement le latent vidéo. N’exécutez pas LTXV Crop Guides d’abord — il traite les images clés générées comme des guides jetables et les supprime.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | Conditionnement positif qui contient les métadonnées des images clés générées. Les métadonnées en sont retirées en sortie. | CONDITIONING | Oui | N/A |
| `negative` | Conditionnement négatif qui contient les métadonnées des images clés générées. Les métadonnées en sont retirées en sortie. | CONDITIONING | Oui | N/A |
| `latent` | Latent vidéo qui contient les images clés générées. Les images clés en sont supprimées en sortie. | LATENT | Oui | N/A |
| `keyframes_to_batch` | Renvoie les images clés sous forme de lot de latents mono-image. Laissez désactivé pour les obtenir sous forme d’un latent multi-image, ce qu’attendent le suréchantillonneur de latent et un futur Add Generated Keyframes. | BOOLEAN | Non | par défaut : False |

### Remarques sur les entrées

- `positive` doit contenir les métadonnées d’images clés générées, sinon le nœud lève une erreur vous invitant à les ajouter d’abord avec LTXV Add Generated Keyframes.
- `latent` doit être un latent vidéo simple (un tenseur 5D). Si les latents vidéo et audio sont encore combinés, séparez-les d’abord avec Separate AV Latent.
- Le nombre de tokens par image de latent enregistré lors de l’ajout des images clés doit correspondre au nombre de tokens par image du `latent` fourni. Si le latent a été remis à l’échelle après l’ajout des images clés, elles ne s’alignent plus et le nœud lève une erreur — séparez-les avant de suréchantillonner le latent.
- La plage d’images des images clés enregistrée doit tenir à l’intérieur du `latent` fourni, sinon le nœud lève une erreur indiquant que les images clés ont été enregistrées pour un autre latent.
- L’index d’entrée d’attention de guide enregistré doit toujours exister dans le conditionnement. Si le conditionnement a été reconstruit après l’ajout des images clés, le nœud lève une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement positif avec les métadonnées d’images clés générées retirées. | CONDITIONING |
| `negative` | Conditionnement négatif avec les métadonnées d’images clés générées retirées. | CONDITIONING |
| `latent` | Latent vidéo avec les images clés générées supprimées. | LATENT |
| `keyframes` | Les images clés extraites, étiquetées avec generated_keyframe_indices et generated_keyframe_num_frames. Fournissez-les à un futur Add Generated Keyframes pour initialiser de nouveaux emplacements, ou à Generated Keyframes To Guides pour les épingler comme guides d’image figés (les indices sont remappés si la longueur du canevas a changé). | LATENT |

## Remarques

- Le paramètre `keyframes_to_batch` détermine si les images clés sont renvoyées sous forme de lot de latents mono-image ou sous forme d’un latent multi-image.
- Le nœud garantit que les images clés générées sont retirées du conditionnement et du latent avant tout traitement ultérieur.
- La sortie `keyframes` peut être utilisée pour initialiser de nouveaux emplacements pour les images clés générées ou pour les épingler comme guides d’image figés.
- Le nœud lève une `ValueError` si le latent ne contient pas d’images clés générées ou si les images clés ne correspondent pas au format attendu.
- Le nœud suppose que les images clés générées ont été ajoutées à l’aide du nœud LTXV Add Generated Keyframes et qu’elles sont compatibles avec le latent actuel.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/fr.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
