# SaveGLB

Le nœud SaveGLB enregistre des données de maillage 3D ou des entrées de fichiers 3D dans le répertoire de sortie. Il accepte les données de maillage et les formats de fichiers 3D courants (GLB, GLTF, OBJ, FBX, STL, USDZ, PLY, SPLAT, SPZ, KSPLAT) et les exporte avec le préfixe de nom de fichier spécifié. Les entrées de maillage sont écrites sous forme de fichiers GLB, un par élément de lot, tandis que les entrées de fichiers 3D sont enregistrées dans leur format d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `maillage` | Maillage ou fichier 3D à enregistrer | MESH ou FILE3D | Oui | Mesh data<br>GLB<br>GLTF<br>OBJ<br>FBX<br>STL<br>USDZ<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT<br>Any splat format<br>Any point cloud format<br>Any 3D file format |
| `préfixe_du_nom_de_fichier` | Le préfixe du nom de fichier de sortie (par défaut : « 3d/ComfyUI »). Le préfixe peut inclure un chemin de sous-dossier, de sorte que les fichiers sont enregistrés dans le sous-dossier « 3d » du répertoire de sortie par défaut | STRING | Non | - |

Remarque : lorsque l'entrée `mesh` est un fichier 3D, le nœud l'enregistre en utilisant l'extension de son format d'origine (GLB est utilisé si le fichier n'a pas de format). Lorsqu'il s'agit de données de maillage, chaque élément du lot est enregistré sous la forme d'un fichier `.glb` distinct ; les éléments vides (sans sommets ni faces) sont ignorés avec un avertissement. Les noms de fichiers de sortie suivent le modèle `{filename_prefix}_{counter:05}_.{ext}` avec un compteur incrémental. Les métadonnées du workflow (prompt et informations PNG supplémentaires) sont intégrées dans les fichiers enregistrés lorsque les métadonnées sont activées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `ui` | Affiche les fichiers 3D enregistrés dans l'interface utilisateur avec le nom de fichier, le sous-dossier et le type d'information | UI |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/fr.md)

---
**Source fingerprint (SHA-256):** `366b56c4fd6e3c2f7783222990792a982857b3419a2becfa27ddfa37853bb22c`
