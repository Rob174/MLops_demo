# MLops_demo
A project designed to setup a full deep learning environment with virtualization, data and code versionning and mlops principles


TODO:
- [x] Setup docker
- [x] Setup python 3.9
- [x] Install basic environments
- [x] Make a environment.txt file
- [ ] Make git accessible from inside
    - [ ] Allow internet connection both ways
    - [ ] Add git
- [ ] Possible to make a bridge with dvc outside?
- [] Test moving from one remote to another (migrating data version control remote)

## DVC cheat sheet

`dvc remote add C:/...`: Add a local remote
`dvc unprotect ...`: remove the protection of a file / folder **only required with hardlink and symlink**
`dvc push`: push elements on the remote
`dvc config cache.type reflink,copy;dvc checkout --relink`: change the mode of storage of the cache

|cache.type	|speed|	space|	editable|
|reflink| 	x|	x|	x
|hardlink| 	x|	x|	
|symlink |	x|	x|	
|copy |			x|

reflink (linux only): Copy-on-write* links or "reflinks" are the best possible link type, when available. They're is as efficient as hard/symlinks, but don't carry any risk of cache corruption since the file system takes care of copying the file if you try to edit it in place, thus keeping the linked cache file intact.

    Unfortunately reflinks are currently supported on a limited number of file systems only (Linux: Btrfs, XFS, OCFS2; macOS: APFS), but in the future they will be supported by the majority of file systems in use.

hardlink: Hard links are the most efficient way to link your data to cache if both your repo and your cache directory are located on the same partition or storage device. The number of hardlinks to one file can be limited by the file system (NTFS: 1024, EXT4: 65,000). DVC will fall back to the next available linking strategy when the number of links exceeds this limit which can happen for repos with very many identical files.

    Note that hard-linked data files can't be edited in place, so DVC avoids these by default. It's however possible to unlink or delete them, and then replace them with a new file.

symlink: Symbolic (a.k.a. "soft") links are the most efficient way to link your data to cache if your repo and your cache directory are located on different file systems/drives (i.e. repo is located on SSD for performance, but cache dir is located on HDD for bigger storage).

    Note that symlinked data files can't be edited in place, so DVC avoids these by default. It's however possible to unlink or delete them, and then replace them with a new file.

copy: An inefficient "linking" strategy, yet supported on all file systems. Using copy means there will be no file links, but that the tracked files will be duplicated as copies existing in both the cache and workspace. Suitable for scenarios with relatively small data files, where copying them is not a storage performance concern 

`dvc gc --not-in-remote --workspace`: remove objects that have already been pushed to the remote from the cache
