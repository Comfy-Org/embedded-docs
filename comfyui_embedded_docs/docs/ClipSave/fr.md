Le nœud `CLIPSave` est conçu pour sauvegarder les modèles d'encodeur de texte CLIP au format SafeTensors. Ce nœud fait partie des flux de travail avancés de fusion de modèles et est généralement utilisé en conjonction avec des nœuds comme `CLIPMergeSimple` et `CLIPMergeAdd`. Les fichiers sauvegardés utilisent le format SafeTensors pour assurer la sécurité et la compatibilité.

## Entrées

| Paramètre | Type de Donnée | Requis | Valeur par Défaut | Description |
|-----------|----------------|---------|------------------|-------------|
| clip | CLIP | Oui | - | Le modèle CLIP à sauvegarder |
| filename_prefix | STRING | Oui | "clip/ComfyUI" | Le chemin préfixe pour le fichier sauvegardé |
| prompt | PROMPT | Masqué | - | Informations du prompt du flux de travail (pour les métadonnées) |
| extra_pnginfo | EXTRA_PNGINFO | Masqué | - | Informations PNG supplémentaires (pour les métadonnées) |

## Sorties

Ce nœud n'a pas de types de sortie définis. Il sauvegarde les fichiers traités dans le dossier `ComfyUI/output/`.

### Stratégie de Sauvegarde Multiple

Le nœud sauvegarde différents composants selon le type de modèle CLIP :

| Type de Préfixe | Suffixe du Fichier | Description |
|-----------------|-------------------|-------------|
| `clip_l.` | `_clip_l` | Encodeur de texte CLIP-L |
| `clip_g.` | `_clip_g` | Encodeur de texte CLIP-G |
| Préfixe vide | Sans suffixe | Autres composants CLIP |

## Notes d'Utilisation

1. **Emplacement des Fichiers** : Tous les fichiers sont sauvegardés dans le répertoire `ComfyUI/output/`
2. **Format de Fichier** : Les modèles sont sauvegardés au format SafeTensors pour la sécurité
3. **Métadonnées** : Inclut les informations du flux de travail et les métadonnées PNG si disponibles
4. **Convention de Nommage** : Utilise le préfixe spécifié plus les suffixes appropriés selon le type de modèle
