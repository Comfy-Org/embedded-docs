Cliquez avec le bouton droit sur le nœud et sélectionnez **Ouvrir dans l'Éditeur de Masque** dans le menu pour ouvrir l'éditeur de masque de l'image chargée.

> Tutoriel officiel de l'éditeur de masque : [https://docs.comfy.org/interface/maskeditor](https://docs.comfy.org/interface/maskeditor)

> Les images téléchargées sont sauvegardées par défaut dans le dossier *ComfyUI/input*, et les images sont chargées par défaut depuis le dossier **input**.

Le nœud Charger Image est conçu pour charger et prétraiter des images à partir d'un chemin spécifié. Il gère les formats d'image avec plusieurs images, applique les transformations nécessaires telles que la rotation basée sur les données EXIF, normalise les valeurs des pixels et génère éventuellement un masque pour les images avec un canal alpha.

## Étapes d'utilisation
1. Glissez-déposez les fichiers image dans l'interface ComfyUI, ou copiez-les manuellement dans le dossier `ComfyUI/input`
2. Ajoutez le nœud Charger Image à votre workflow
3. Dans le menu déroulant `IMAGE` du nœud, sélectionnez le fichier image à charger
4. Connectez les sorties aux nœuds suivants (comme VAEEncode, etc.)

## Formats de fichiers supportés
- Formats courants : PNG, JPG, JPEG, BMP, TIFF, WEBP
- Prend en charge les images avec canal alpha (PNG, TIFF, etc.)
- Prend en charge les séquences d'images multi-images (GIF, TIFF, etc.)

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|----------------|-------------|
| `IMAGE`   | COMBO[STRING]  | Le paramètre `IMAGE` spécifie l'identifiant de l'image à charger et traiter. Il est crucial pour déterminer le chemin vers le fichier image et charger ensuite l'image pour la transformation et la normalisation. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|----------------|-------------|
| `IMAGE`   | IMAGE          | L'image traitée, avec des valeurs de pixels normalisées et des transformations appliquées si nécessaire. Prête pour un traitement ou une analyse ultérieure. |
| `MASQUE`  | MASK           | (Optionnel) Fournit un masque pour l'image, utile lorsque l'image inclut un canal alpha pour la transparence. |

## Détails de la sortie du masque
- **Avec canal alpha** : extrait automatiquement les informations de transparence comme masque
- **Mode palette avec transparence** : convertit en RGBA et extrait le masque
- **Sans information de transparence** : génère un masque vide 64x64
- Plage de valeurs du masque : 0-1 (0 = transparent, 1 = opaque)

## Mise à jour de fichier
- Le nœud détecte automatiquement les changements de contenu du fichier (via le hash SHA256)
- Après avoir remplacé un fichier du même nom, le workflow se rechargera automatiquement
- Pas besoin de redémarrer ComfyUI pour utiliser l'image mise à jour

## FAQ
**Q : Pourquoi mon image n'apparaît-elle pas dans la liste déroulante ?**
R : Assurez-vous que le format de fichier est correct et que le fichier est placé dans le dossier `ComfyUI/input`

**Q : Comment gérer les images de grande taille ?**
R : Charger Image conserve la taille d'origine ; pour redimensionner, connectez un nœud ImageScale

**Q : Comment utiliser l'éditeur de masque ?**
R : Faites un clic droit sur le nœud et sélectionnez "Ouvrir dans l'Éditeur de Masque" pour éditer directement le masque de l'image

Tutoriel officiel de l'éditeur de masque : [https://docs.comfy.org/interface/maskeditor](https://docs.comfy.org/interface/maskeditor)

## Conseils de performance
- Les images sont automatiquement pivotées selon les informations EXIF
- Les valeurs de pixels sont normalisées dans la plage 0-1, adaptées aux modèles d'apprentissage profond
- Pour les images multi-images, seules les images de même taille sont conservées
