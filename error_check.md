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
