# PyBash
PyBash is a shell and command language written using Python <br>
## Manual
### `cd` <br>
_Command to navigate directories_ <br>
- Usage<br>
`cd [path]`<br>
Use `..` to navigate up one directory<br>
- Examples<br>
    >`cd Desktop`<br>
    
        C:\Desktop

    >`cd ..`<br>
        
        C:\

### `ls` <br>
_Command showing list of directories and files_<br>
- Usage<br>
`ls [keys] [path]`<br>
- Keys<br>
`-h` manual for noobs<br>
`-a` shows hidden files and folders<br>
`-l` shows pretty list with numbers, sizes and types(folder or file)<br>
- Examples<br>
    >`ls -a`<br>
    
        folder file

    >`ls -l`<br>
    
        .hidden folder file

    >`ls -la:`<br>
    
        1) .hidden_________file____4
        2) folder__________folder__0
        3) file____________file____4096
    
    >`ls ..\folder.txt`<br>
    
        file1 file2
    
    >`ls -h`<br>
        
        *recursion*

### `cat`
_Read file contents_<br>
- Usage<br>
`cat [keys] [path]`<br>
- Keys<br>
`-h` help<br>
`-n` number each line<br>
- Examples<br>
    >`cat ..\file.txt`<br>
    
        Cold frost and sunshine: day of wonder!
        But you, my friend, are still in slumber-
        Wake up, my beauty, time belies:
        You dormant eyes, I beg you, broaden
        Toward the northerly Aurora,
        As though a northern star arise!
    
    >`cat -n ..\file.txt`<br>
        
        1) Cold frost and sunshine: day of wonder!
        2) But you, my friend, are still in slumber-
        3) Wake up, my beauty, time belies:
        4) You dormant eyes, I beg you, broaden
        5) Toward the northerly Aurora,
        6) As though a northern star arise!

cat -n ..\folder\file
### `clear`
_Clear PyBash console_
### `exit`
_Exit PyBash_