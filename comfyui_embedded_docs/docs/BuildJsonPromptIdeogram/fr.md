# Générer une invite JSON (Ideogram)

Ce nœud construit une invite JSON structurée, spécifiquement formatée pour le modèle de génération d'images Ideogram 4. Il organise vos instructions textuelles, vos préférences de style et votre palette de couleurs dans la structure JSON requise attendue par le modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `élément` | Éléments d'invite provenant du nœud Créer des boîtes englobantes. | ARRAY | Oui | - |
| `description_de_haut_niveau` | Description facultative de l'image en une ou deux phrases. Fortement recommandée. (par défaut : vide) | STRING | Non | - |
| `arrière-plan` | Description obligatoire de l'arrière-plan ou de l'environnement de l'image. (par défaut : vide) | STRING | Oui | - |
| `style` | Catégorie de style visuel pour l'image générée. (par défaut : "none") | COMBO | Oui | `"none"`<br>`"photo"`<br>`"art_style"` |
| `photo` | Détails de l'appareil photo ou de l'objectif pour les sorties photographiques (ex. 35mm, f/1.4, bokeh). Disponible uniquement lorsque le style est défini sur "photo". (par défaut : vide) | STRING | Non | - |
| `art_style` | Description du style artistique (ex. illustration vectorielle plate, contours épais). Disponible uniquement lorsque le style est défini sur "art_style". (par défaut : vide) | STRING | Non | - |
| `esthétique` | Mots-clés esthétiques obligatoires (ex. atmosphérique, cinématographique, désaturé). (par défaut : vide) | STRING | Oui | - |
| `éclairage` | Description obligatoire de l'éclairage (ex. heure dorée, contre-jour, ombres dramatiques). (par défaut : vide) | STRING | Oui | - |
| `support` | Type de support obligatoire (ex. photographie, illustration, rendu_3d, peinture, conception_graphique). Lorsque style = photo, définir sur photographie. (par défaut : vide) | STRING | Oui | - |
| `palette_de_couleurs` | Codes de couleur hexadécimaux qui orientent les couleurs dominantes de l'image. Jusqu'à 16 entrées. | COLORS | Non | - |

**Remarque :** Lorsque le paramètre `style` est défini sur "photo", l'entrée `photo` devient disponible et vous devez définir le paramètre `medium` sur "photographie". Lorsque `style` est défini sur "art_style", l'entrée `art_style` devient disponible.

## Sorties

| Nom de la sortie | Description | Type de données |
|------------------|-------------|-----------------|
| `invite` | Un dictionnaire JSON structuré contenant la description de haut niveau, la description du style (le cas échéant), et la décomposition compositionnelle avec l'arrière-plan et les éléments. | DICT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildJsonPromptIdeogram/fr.md)

---
**Source fingerprint (SHA-256):** `56a045e0c7c19531e6443696c0bdf3946df066d03eea7d2d217b7d92f052592f`
