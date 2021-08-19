# Error Checking

## Examples

### Change to non-existent directory

```python
try:
    os.chdir(folder)
except FileNotFoundError:
    print(f'Folder needed but not found: "{folder}"')
    val = input('Create folder? [y]es or [n]o : ')
    if val == 'y':
        os.mkdir(folder)
        print(f'Created folder: "{folder}"')
    else:
      print('Check accuracy of folders in database.')
      print('Abnormal script termination.')
      sys.exit('Folder misspecified.')
```
### Change to non-existent directory with serialization

```python
if self._serialize:
    folder = self._folder
    abs_path = os.path.join(os.getcwd(), folder)
    if not os.path.isdir(abs_path):
        print(f'Folder needed but not found: "{abs_path}"')
        val = input('Create folder? [y]es or [n]o : ')
        if val == 'y':
            os.mkdir(folder)
            print(f'Created folder: "{folder}"')
        else:
            print('Check accuracy of folders in database.')
            print('Abnormal script termination.')
            sys.exit('Folder misspecified.')
 
    fig.savefig(os.path.join(abs_path, self._file), dpi=300)
    print('Figure saved to folder: ' + abs_path)
    print(f'Figure filename: {self._file}')
```
