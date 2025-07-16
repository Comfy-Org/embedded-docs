`CLIPTextEncodeFlux` est un nœud avancé d'encodage de texte dans ComfyUI, spécialement conçu pour l'architecture Flux. Il utilise un mécanisme à double encodeur (CLIP-L et T5XXL) pour traiter à la fois des mots-clés structurés et des descriptions détaillées en langage naturel, offrant au modèle Flux une compréhension textuelle plus précise et complète pour améliorer la qualité de la génération d'images à partir de texte.

Ce nœud repose sur la collaboration de deux encodeurs :

1. L'entrée `clip_l` est traitée par l'encodeur CLIP-L, extrayant des caractéristiques telles que le style et le thème, idéale pour des descriptions concises.
2. L'entrée `t5xxl` est traitée par l'encodeur T5XXL, spécialisé dans la compréhension de descriptions complexes et détaillées en langage naturel.
3. Les résultats des deux encodeurs sont fusionnés et, combinés avec le paramètre `guidance`, génèrent un embedding conditionnel unifié (`CONDITIONNEMENT`) pour les nœuds de sampling Flux, contrôlant le degré de correspondance entre le contenu généré et la description textuelle.

## Entrées

| Nom du paramètre | Type de donnée | Méthode d'entrée | Valeur par défaut | Plage | Fonction |
|------------------|----------------|------------------|-------------------|-------|----------|
| `clip`           | CLIP           | Entrée de nœud   | Aucun             | -     | Doit être un modèle CLIP compatible Flux, incluant les encodeurs CLIP-L et T5XXL |
| `clip_l`         | STRING         | Champ texte      | Aucun             | Jusqu'à 77 tokens | Adapté pour des descriptions concises de mots-clés, comme le style ou le thème |
| `t5xxl`          | STRING         | Champ texte      | Aucun             | Pratiquement illimité | Adapté pour des descriptions détaillées en langage naturel, exprimant des scènes et des détails complexes |
| `guidance`       | FLOAT          | Curseur          | 3.5               | 0.0 - 100.0 | Contrôle l'influence des conditions textuelles sur le processus de génération ; des valeurs plus élevées signifient un respect plus strict du texte |

## Sorties

| Nom de sortie      | Type de donnée   | Fonction |
|--------------------|------------------|----------|
| `CONDITIONNEMENT`  | CONDITIONING     | Contient l'embedding fusionné des deux encodeurs et le paramètre de guidance, utilisé pour la génération conditionnelle d'images |

## Exemples d'utilisation

### Exemples de prompts

- **Entrée clip_l** (mots-clés) :
  - Utilisez des combinaisons structurées et concises de mots-clés
  - Exemple : `masterpiece, best quality, portrait, oil painting, dramatic lighting`
  - Concentrez-vous sur le style, la qualité et le sujet principal

- **Entrée t5xxl** (description en langage naturel) :
  - Utilisez des descriptions complètes et fluides de la scène
  - Exemple : `A highly detailed portrait in oil painting style, featuring dramatic chiaroscuro lighting that creates deep shadows and bright highlights, emphasizing the subject's features with renaissance-inspired composition.`
  - Concentrez-vous sur les détails de la scène, les relations spatiales et les effets de lumière

### Remarques

1. Assurez-vous d'utiliser un modèle CLIP compatible avec l'architecture Flux
2. Il est recommandé de remplir à la fois `clip_l` et `t5xxl` pour profiter de l'avantage du double encodeur
3. Notez la limite de 77 tokens pour `clip_l`
4. Ajustez le paramètre `guidance` selon les résultats générés
