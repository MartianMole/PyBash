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
    
        C:\Desktop<br>

    >`cd ..`<br>
        
        C:\<br>

### `ls` <br>
_Command showing list of directories and files_<br>
- Usage<br>
`ls [keys]`<br>
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
    
    >`ls -h`<br>
        
        *recursion*
### `exit`
_Exit PyBash_